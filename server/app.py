import falcon
import uuid
from datetime import datetime

from server.resources.fileUpload import FileUpload
from server.resources.sampleData import SampleData


class StorageEngine(object):
    is_dirty = True
    database = []

    def datetime_filter(self, start_time, elem):
        if start_time:
            time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
        else:
            time = datetime.min
        return time <= elem[0]

    def type_filter(self, sample_type, elem):
        return elem[1] == sample_type


    def has_data(self):
        return len(self.database) != 0

    def get_sample_types(self):
        return { s_type[1] for s_type in self.database }

    """
    Return a filtered and sorted list based upon the arguments
    """
    def get_things(self, start_time, sample_type, limit):
        if self.is_dirty:
            self.database.sort(key=lambda elem: elem[0])
            self.is_dirty = False

        # Filter database with datetime and type filter
        filtered_list = [ elem for elem in self.database if self.type_filter(sample_type, elem) ]

        return filtered_list[:limit]


    def add_thing(self, thing):
        self.database.append([ datetime.strptime(thing[0], "%Y-%m-%dT%H:%M:%S"), thing[1], float(thing[2]) ])
        self.is_dirty = True

    """
    Accepts file path

    Each line of the file is split by comma and fed into add:thing
    """
    def add_file(self, thing_file):
        with open(thing_file, "r") as readonly_file:
            for line in readonly_file.readlines():
                self.add_thing([ item.strip() for item in line.strip()[1:-1].split(',') ])


class ApiService(falcon.API):
    def __init__(self, db, **kwargs):
        super().__init__(**kwargs)

        self.db = db
        self.add_route('/fileUpload', FileUpload(self.db, 'server/files/'))
        self.add_route('/', SampleData(self.db))