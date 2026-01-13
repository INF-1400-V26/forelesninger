from universitet import Universitet


class Person(object):
    def __init__(self, navn, br_navn, universitet):
        self.navn = navn
        self.br_navn = br_navn
        self.universitet = universitet
        self.emner = []

    def nytt_emne(self, emnekode):
        if emnekode in self.universitet.emner:
            self.emner.append(emnekode)

    def __str__(self):
        return str(self.__dict__)
        # return f"Person: {self.navn},\nUniversitet: {self.universitet.navn},\nEmner: {self.emner}"


if __name__ == "__main__":
    uit = Universitet("UiT Norges Arktiske Universitet")
    petter = Person("Petter Smart", "petts1234", uit)

    uit.nytt_emne("hms-1000")
    petter.nytt_emne("hms-1000")
    print(petter)
