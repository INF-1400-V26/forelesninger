class Universitet:
    def __init__(self, navn):
        self.navn = navn
        self.emner = []
        self._studenter = []
        self._ansatte = []

    def nytt_emne(self, emnekode):
        if self._valider_emnekode(emnekode):
            self.emner.append(emnekode)
        else:
            raise Exception(f"Ikke gyldig emnekode: {emnekode}") # fungerer nå
    
    def _valider_emnekode(self, emnekode):
        if len(emnekode) != 8:
            return False
        return True 

    def __str__(self):
        return f"{self.navn}\nEmner: {self.emner} \
            \nStudenter: {[student.navn for student in self._studenter ]} \
            \nAnsatte: {[ansatt.navn for ansatt in self._ansatte ]}"


if __name__ == "__main__":
    uit = Universitet("UiT Norges Arktiske Universitet")
    uit.nytt_emne("inf-1000") # Skal passere
    # uit.nytt_emne("inf-100") # Gir exception når du kjører den (kommenter ut), som den skal 
    print(uit)
