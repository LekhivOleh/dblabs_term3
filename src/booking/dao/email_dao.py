from src.booking.domain.models import Email

class EmailDao:
    def __init__(self, session):
        self.session = session

    def create_email(self, address, password, is_registered):
        new_email = Email(address=address, password=password, is_registered=is_registered)
        self.session.add(new_email)
        self.session.commit()
        return new_email

    def get_all_emails(self):
        return self.session.query(Email).all()

    def get_email(self, id):
        return self.session.query(Email).get(id)

    def update_email(self, id, address, password, is_registered):
        email = self.session.query(Email).get(id)
        if email:
            email.address = address
            email.password = password
            email.is_registered = is_registered
            self.session.commit()
        return email

    def delete_email(self, id):
        email = self.session.query(Email).get(id)
        if email:
            self.session.delete(email)
            self.session.commit()
        return email