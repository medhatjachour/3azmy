from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1ewefEhStDY3YnCKwA4K7_kS-YlCaajme'
file_name = 'plumbing.db'
mime_type = 'application/vnd.sqlite3' # application/x-sqlite3

file_metadata = {
    'name': file_name,
    'parents': [folder_id]
}

media = MediaFileUpload('./plumbing.db'.format(file_name), mimetype = mime_type)
 
service.files().create(
    body = file_metadata,
    media_body = media,
    fields = 'id'
).execute()
