from person import Person
from datetime import datetime


class Student(Person):
    def __init__(self, navn, br_navn, universitet, studieprogram):
        super().__init__(navn, br_navn, universitet)
        self.studieprogram = studieprogram
        self.universitet.studenter.append(self)
        self.eksamener = {}

    def __str__(self):
        return f"Student: {self.navn},\nUniversitet: {self.universitet.navn}, \
        \nStudieprogram: {self.studieprogram}\nEmner: {self.emner}"
    
    def nytt_emne(self, emnekode):
        self.emner.append(emnekode)
        print("Du er meldt på ", emnekode)
        # self.meld_til_eksamen(emnekode, datetime.now())
    
    # def meld_til_eksamen(self, emnekode, meldetidspunkt):
    #     self.eksamener[emnekode] = meldetidspunkt


