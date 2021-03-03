from server.app import ApiService, StorageEngine
from waitress import serve
from falcon_cors import CORS
from falcon_multipart.middleware import MultipartMiddleware

# Add allow all origins to prevent CORS errors
cors = CORS(allow_all_origins=True)

# Create StorageEngine instance
db = StorageEngine()

# Create falcon API
api_service = ApiService(db, middleware=[cors.middleware, MultipartMiddleware()])

# Start waitress server
serve(api_service, host='116.203.251.218', port=3333)
