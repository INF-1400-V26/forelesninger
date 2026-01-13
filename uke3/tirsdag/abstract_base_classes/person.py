from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, navn, br_navn, universitet):
        self.navn = navn
        self.br_navn = br_navn
        self.universitet = universitet
        self.emner = []

    @abstractmethod
    def nytt_emne(self, emnekode):
        pass

    def __str__(self):
        return str(self.__dict__) # denne verdien kommer med object-klassen
        # return f"Person: {self.navn},\nUniversitet: {self.universitet.navn},\nEmner: {self.emner}"
    
