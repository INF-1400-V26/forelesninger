class Booking:
    def __init__(self, customer, personal_trainer, session):
        self.customer = customer
        self.personal_trainer = personal_trainer
        self.session = session
        self.price = 1000

    def __str__(self):
        return f"PT: {self.personal_trainer.name}\nCustomer: {self.customer.name}\nTime range: {self.session.start_time} - {self.session.end_time}"