from person import Person
from universitet import Universitet


class Student(Person):
    def __init__(self, navn, br_navn, universitet, studieprogram):
        # super().__init__(navn, br_navn, universitet)
        self.studieprogram = studieprogram
        # self.universitet.studenter.append(self)

    def __str__(self):
        return "HEllo"
        # return f"Student: {self.navn},\nUniversitet: {self.universitet.navn}, \
        # \nStudieprogram: {self.studieprogram}\nEmner: {self.emner}"


if __name__ == "__main__":
    uio = Universitet("UiO")
    donald = Student("Donald Duck", "dondu9999", uio, "Lektorutdanning i Nordisk")
    # print(donald)
    # print("------------")
    # print(uio)
