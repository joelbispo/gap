user_logged = None


class User:
    # need to ignore common case because it is a Firebase standard.
    COLLECTION = "user"

    def __init__(self, kind="", localId="", email="", displayName="", idToken="", registered=""):
        self.kind = kind
        self.localId = localId
        self.email = email
        self.displayName = displayName
        self.idToken = idToken
        self.registered = registered

    @classmethod
    def from_dict(cls, dictionary: dict):
        obj = cls()
        for key in dictionary:
            setattr(obj, key, dictionary[key])

        return obj

    def to_dict(self) -> dict:
        return self.__dict__