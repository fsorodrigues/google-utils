# import google authentication modules
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from googleapiclient.discovery import build

class AuthGoogle:
    def __init__(self,CLIENT_SECRET_FILE):
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE

    def credentials(self,SCOPE,delegate=False):
        CREDS = ServiceAccountCredentials.from_json_keyfile_dict(self.CLIENT_SECRET_FILE,SCOPE)
        if delegate:
            CREDS = CREDS.create_delegated(delegate)
        return CREDS

    def authenticate_http(self,CREDS):
        HTTP = CREDS.authorize(httplib2.Http())
        return HTTP

    def service(self,api_dict,http):
        service = build(api_dict['api'],api_dict['version'],http=http,cache_discovery=False)
        return service
