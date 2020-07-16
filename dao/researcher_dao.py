from infrastructure.firebase_sdka_admin import db
from model.researcher import Researcher


class ResearcherDAO:
    def __init__(self):
        self._collection = db.collection(Researcher.COLLECTION)

    def add_researcher(self, researcher: Researcher):
        self._collection.add(researcher.to_dict())
