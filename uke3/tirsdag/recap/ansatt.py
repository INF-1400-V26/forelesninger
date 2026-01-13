from person import Person
from universitet import Universitet


class Ansatt(Person):
    def __init__(self, navn, br_navn, universitet, årslønn):
        super().__init__(navn, br_navn, universitet)
        self.årslønn = årslønn
        self.universitet.ansatte.append(self)
        self.sensur = []

    def ny_sensur(self, emnekode):
        self.sensur.append(emnekode)

    def __str__(self):
        return f"Ansatt: {self.navn},\
        \nUniversitet: {self.universitet.navn}, \
        \nÅrslønn: {self.årslønn} \
        \nEmner: {self.emner}"


if __name__ == "__main__":
    uib = Universitet("UiB")
    skrue = Ansatt("Onkel Skrue", "onksk3333", uib, "30000")

    print(skrue)
    print("-------------------")
    print(uib)
