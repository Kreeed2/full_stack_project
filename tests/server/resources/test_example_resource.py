# import falcon

# from falcon import testing

# from server.resources.example import ExampleResource


# class TestDevicePagesTreeResource(testing.TestCase):
#     def setUp(self):
#         super().setUp()

#         self.resource = ExampleResource()
#         self.app = falcon.API()
#         self.app.add_route("/example", self.resource)

#     def test_get_request_should_return_example_message(self):
#         result = self.simulate_get("/example")

#         self.assertEqual(result.json, { "message": "Hello World" })
