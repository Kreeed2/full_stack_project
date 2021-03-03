import os
import sys
import uuid
from pathlib import Path
import falcon


class FileUpload:

    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, db, storage_path):
        self._storage_path = storage_path
        self.db = db
        Path(self._storage_path).mkdir(parents=True, exist_ok=True)

    """
    Accepts post request to this route of type multipart form

    Load the file in chunks (if needed) and saves it with a uuid name in the storage_path
    Lastly adds the file to the database
    """
    def on_post(self, req, resp):
        try:
            data = req.get_param('data')
            
            ext = data.filename.split('.')[-1]
            name = '{uuid}.{ext}'.format(uuid=uuid.uuid4(), ext=ext)
            file_path = os.path.join(self._storage_path, name)
            
            print(file_path)
            
            with open(file_path, 'wb') as data_file:
                while True:
                    chunk = data.file.read(self._CHUNK_SIZE_BYTES)
                    if not chunk:
                        break

                    data_file.write(chunk)

            self.db.add_file(self._storage_path + name)
            resp.status = falcon.HTTP_201
            resp.location = self._storage_path + name
        except:
            e = sys.exc_info()[0]
            print(e)
            resp.status = falcon.HTTP_400        