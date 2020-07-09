#!/usr/bin/env python
import os
if '.env' in os.listdir('./'):
    from dotenv import load_dotenv
    # load environment variables
    APP_ROOT = os.path.join(os.path.dirname('__file__'),'.')
    dotenv_path = os.path.join(APP_ROOT,'.env')
    load_dotenv(dotenv_path)

class EnvVars:
    def get_config(self):
        return self.load_config()

    def load_config(self):
        CLIENT_SECRET_FILE = {
            "type": os.getenv('TYPE'),
            "project_id": os.getenv('PROJECT_ID'),
            "private_key_id": os.getenv('PRIVATE_KEY_ID'),
            "private_key": os.getenv('PRIVATE_KEY').replace('\\n', '\n'),
            "client_email": os.getenv('CLIENT_EMAIL'),
            "client_id": os.getenv('CLIENT_ID'),
            "auth_uri": os.getenv('AUTH_URI'),
            "token_uri": os.getenv('TOKEN_URI'),
            "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
            "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL')
        }
        return CLIENT_SECRET_FILE

    def get_scope(self,SCOPE_NAME):
        return self.load_scope(SCOPE_NAME)

    def load_scope(self,SCOPE_NAME):
        GSHEETS_SCOPE = [self.get_var(SCOPE_NAME)]
        return GSHEETS_SCOPE

    def get_var(self,PROP):
        return self.load_var(PROP)

    def load_var(self,PROP):
        SPREADSHEET_ID = os.getenv(PROP)
        return SPREADSHEET_ID
