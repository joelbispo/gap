from dao.researcher_dao import ResearcherDAO
from model.researcher import Researcher


class ResearcherLogic:
    def __init__(self):
        self.dao = ResearcherDAO()

    def save_researcher(self, researcher: Researcher) -> None:
        self.dao.add_researcher(researcher)
