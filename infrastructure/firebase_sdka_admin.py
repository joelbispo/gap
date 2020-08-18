import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

__all__ = ['db', 'app']

cred = credentials.Certificate("../infrastructure/key_firebase.json")

app = firebase_admin.initialize_app(cred)

db = firestore.client()
