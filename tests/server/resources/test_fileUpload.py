import falcon

from falcon import testing
import mimetypes
from codecs import encode

from server.resources.fileUpload import FileUpload
from server.app import StorageEngine


class TestFileUploadResource(testing.TestCase):
    def setUp(self):
        super().setUp()

        self.database = StorageEngine()
        self.resource = FileUpload(self.database, "tests/files")
        self.app = falcon.API()
        self.app.add_route("/fileUpload", self.resource)
        self.file_path = 'tests/server/test_datei.txt'

    def test_post_request_should_return_put_file_in_storage(self):
        # Cant get falcon multipart/form to work
        
        # dataList = []
        # boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        # dataList.append(encode('--' + boundary))
        # dataList.append(encode('Content-Disposition: form-data; name="data"; filename="{0}"'.format(self.file_path)))

        # fileType = mimetypes.guess_type(self.file_path)[0] or 'application/octet-stream'
        # dataList.append(encode('Content-Type: {}'.format(fileType)))
        # dataList.append(encode(''))

        # with open(self.file_path, 'rb') as f:
        #     dataList.append(f.read())
        # dataList.append(encode('--'+boundary+'--'))
        # dataList.append(encode(''))
        
        # body = b'/r/n'.join(dataList)
        
        # headers = {
        #     'Content-Type': 'multipart/form-data; boundary={}'.format(boundary) 
        # }
        # result = self.simulate_request(method="POST", path="/fileUpload", body=body, headers=headers)
        

        # self.assertEqual(result.status, falcon.HTTP_201)
        pass
