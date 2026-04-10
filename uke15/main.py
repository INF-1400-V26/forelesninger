from BookingManager import BookingManager
from customer import Customer
from session import Session
from personal_trainer import PersonalTrainer

if __name__ == "__main__":
    manager = BookingManager()
    customer = Customer("Anne")
    pt = PersonalTrainer("Roger")
    sesh = Session("2026-04-08T12:00", "2026-04-08T13:00")
    manager.createBooking(customer, pt, sesh)
    print(manager.bookings[0])
