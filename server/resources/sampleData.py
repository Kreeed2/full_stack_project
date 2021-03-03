import falcon
from json import dumps
from datetime import datetime, timedelta

class SampleData:

    def __init__(self, db):
        self.db = db

    """ 
    Accepts get requests to the route

    Retrieves data from the database and applies filters based upon get parameters
    """
    def on_get(self, req, resp):
        filtered = req.get_param('filtered') or True
        start_time = req.get_param('start_time')
        selected_type = req.get_param('filter_type')
        limit = req.get_param_as_int('limit') or 50

        if self.db.has_data() and filtered:
            result = { }
            # Allow for dynamic inclusion of new sample_types
            if (selected_type):
                sample_types = [ selected_type ]
            else:
                sample_types = self.db.get_sample_types() 
            
            for sample_type in sample_types:
                sample_points = self.db.get_things(start_time, sample_type, limit)
                time_slice_mesurements = [ ]
                visited_measurements = [ ]

                if start_time:
                    time_slice = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
                else:
                    time_slice =  datetime.strptime("2017-01-03T10:05:00", "%Y-%m-%dT%H:%M:%S")
                    
                while True: 
                    # Find all sample_elements that fit into the current time_slice and are not visited before
                    valid_samples = [ elem for elem in sample_points if elem[0] <= time_slice and elem not in visited_measurements ]
                    if (len(valid_samples)) != 0:
                        # Then find the one sample point that is closest to the slice
                        max_value = max(valid_samples, key=lambda elem: elem[0])
                        visited_measurements.extend(valid_samples)
                        time_slice_mesurements.append([ time_slice, max_value[1], max_value[2]])
                    else:
                        break
                    time_slice += timedelta(minutes=5)
                result[sample_type] = time_slice_mesurements
        else:            
            result = self.db.get_things(start_time, selected_type, limit)        

        resp.media = dumps(result, default=self.serialize)
        resp.status = falcon.HTTP_200

    # Helper function to serialize datetime
    def serialize(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return dumps(obj)