from booking import Booking

class BookingManager:
    def __init__(self):
        self.bookings = []

    def createBooking(self, customer, personal_trainer, session):
        booking = Booking(customer, personal_trainer, session)
        self.bookings.append(booking)