from person import Person

class Ansatt(Person):
    def __init__(self, navn, br_navn, universitet, årslønn):
        super().__init__(navn, br_navn, universitet)
        self.årslønn = årslønn
        self.universitet.ansatte.append(self)
        self.sensur = []

    def ny_sensur(self, emnekode):
        self.sensur.append(emnekode)

    def nytt_emne(self, emnekode):
        self.emner.append(emnekode)
        self.sensur.append(emnekode)
        print(f"Du er foreleser i {emnekode}, og er meldt opp til sensur")

    def __str__(self):
        return f"Ansatt: {self.navn},\
        \nUniversitet: {self.universitet.navn}, \
        \nÅrslønn: {self.årslønn} \
        \nEmner: {self.emner}"

