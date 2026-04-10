from uuid import uuid4

class Customer:
    def __init__(self, name):
        self.name = name
        self._id = uuid4()