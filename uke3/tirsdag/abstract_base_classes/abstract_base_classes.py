from person import Person
from universitet import Universitet
from student import Student
from ansatt import Ansatt

if __name__ == "__main__":
    uit = Universitet("UiT")

    ola = Student("Ola Nordmann", "olano4444", uit, "Informatikk")

    anne = Student("Anne", "abc123", uit, "Helseinformatikk")
    gunnar = Ansatt("Gunnar", "gunnar444", uit, 1)

    # linja nedenfor vil gi TypeError når vi kjører den
    # petter = Person("Petter Smart", "petts1234", uit) 

    uit.nytt_emne("hms-1000")

    liste = [anne, gunnar] 
    for p in liste:
        p.nytt_emne("hms-1000")
        print(p)
    print("-----------------")
    print(uit)