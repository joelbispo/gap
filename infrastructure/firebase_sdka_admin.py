import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

__all__ = ['db', 'app', 'api_key']

with open('infrastructure\web_api_key.json') as config_file:
    web_key_file = json.load(config_file)

cred = credentials.Certificate('infrastructure\key_firebase.json')
app = firebase_admin.initialize_app(cred)
api_key = web_key_file['key']

db = firestore.client()
