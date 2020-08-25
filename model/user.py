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

    def from_dict(self, dictionary: dict):
        obj = self
        for key in dictionary:
            setattr(obj, key, dictionary[key])

        return obj

    def to_dict(self) -> dict:
        return self.__dict__


user_logged: User = User()
