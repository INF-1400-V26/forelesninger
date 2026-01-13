class Universitet:
    def __init__(self, navn):
        self.navn = navn
        self.emner = []
        self.studenter = []
        self.ansatte = []

    def nytt_emne(self, emnekode):
        self.emner.append(emnekode)

    def __str__(self):
        return f"{self.navn}\nEmner: {self.emner} \
            \nStudenter: {[student.navn for student in self.studenter ]} \
            \nAnsatte: {[ansatt.navn for ansatt in self.ansatte ]}"



