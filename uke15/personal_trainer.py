from uuid import uuid4

class PersonalTrainer:
    def __init__(self, name):
        self.name = name
        self.id = uuid4()