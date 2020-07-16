import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

__all__ = ['db']

cred = credentials.Certificate("infrastructure/key_firebase.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

# if __name__ == '__main__':
#     emp_ref = db.collection('participants')
#     docs = emp_ref.stream()
#     for doc in docs:
#         print('{} => {} '.format(doc.id, doc.to_dict()))