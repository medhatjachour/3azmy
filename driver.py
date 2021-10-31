from googleapiclient.http import MediaFileUpload
from google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': 'plumbing.db', #the file we want to uploead
    'parents': ['3azmy'] # the folder in the cloud which will wold the data file
}

media_content = MediaFileUpload('plumbing.db', mimetype='image/png') #searhc about that

file = service.files().create(
    body=file_metadata,

    media_body=media_content
).execute()

print(file)


# Replace Existing File on Google Drive
#file_id = '<file id>'

#media_content = MediaFileUpload('mp4.png', mimetype='image/png')

#service.files().update(
#    fileId=file_id,
#    media_body=media_content
#).execute()
