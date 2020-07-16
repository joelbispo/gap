class Researcher:
    COLLECTION = "researchers"

    def __init__(self,  full_name="",  academic_level="", institution=""):
        self.full_name = full_name
        self.academic_level = academic_level
        self.institution = institution

    @classmethod
    def from_dict(cls, dictionary: dict):
        obj = cls()
        for key in dictionary:
            setattr(obj, key, dictionary[key])

        return obj

    def to_dict(self) -> dict:
        return self.__dict__
