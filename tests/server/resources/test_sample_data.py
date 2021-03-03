import falcon

from json import loads
from falcon import testing
from datetime import datetime

from server.app import StorageEngine
from server.resources.sampleData import SampleData

class TestSampleDataResource(testing.TestCase):
  
  def setUp(self):
    super().setUp()
      
    self.database = StorageEngine()
    self.resource = SampleData(self.database)
    self.app = falcon.API()
    self.app.add_route("/", self.resource)
    
  def test_fill_database_with_samples(self):
    sample_data = [
      ["2017-01-03T10:04:45", "TEMP", "35.79"],
      ["2017-01-03T10:01:18", "SPO2", "98.78"],
      ["2017-01-03T10:09:07", "TEMP", "35.01"],
      ["2017-01-03T10:03:34", "SPO2", "96.49"],
      ["2017-01-03T10:02:01", "TEMP", "35.82"],
      ["2017-01-03T10:05:00", "SPO2", "97.17"],
      ["2017-01-03T10:05:01", "SPO2", "95.08"]
    ]
          
    for entry in sample_data:
      self.database.add_thing(entry)
          
      self.assertEqual(self.database.has_data(), True)
          
  def test_sample_filter(self):
    test_filter = "TEMP"
    params = { "filter_type": test_filter }
    result = self.simulate_request(method="GET", path="/", params=params)

    self.assertTrue(len(loads(result.json).keys()) == 1)
    
  def test_limit(self):
    test_filter = 4
    params = { "limit": test_filter }
    result = self.simulate_request(method="GET", path="/", params=params)

    sum_entries = 0
    dic = loads(result.json)
    for key in dic:
      sum_entries += len(dic[key])
    
    self.assertTrue(sum_entries == test_filter)
    
  def test_full(self):
    result = self.simulate_request(method="GET", path="/")
    
    correct_data_response = { 
      "TEMP": [
        ["2017-01-03T10:10:00", "TEMP", "35.01"],
        ["2017-01-03T10:05:00", "TEMP", "35.79"]
      ],
      "SPO2": [
        ["2017-01-03T10:05:00", "SPO2", "97.17"],
        ["2017-01-03T10:10:00", "SPO2", "95.08"]
      ]
    }
    has_error = False
    dic = loads(result.json)
    for key in correct_data_response:
      # print(key)
      if key not in dic:
        has_error = True
    
      for sample in correct_data_response[key]:
        # print(str(sample))
        if sample not in dic[key]:
          has_error = True
      
    self.assertTrue(has_error)
