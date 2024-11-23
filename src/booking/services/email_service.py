from src.booking.dao.email_dao import EmailDao


class EmailService:
    def __init__(self, email_dao: EmailDao):
        self.email_dao = email_dao

    def create_email(self, address: str, password: str, is_registered: bool):
        """Create a new email."""
        return self.email_dao.create_email(address, password, is_registered)

    def get_all_emails(self):
        """Retrieve all emails."""
        return self.email_dao.get_all_emails()

    def get_email(self, id: int):
        """Retrieve an email by ID."""
        return self.email_dao.get_email(id)

    def update_email(self, id: int, address: str, password: str, is_registered: bool):
        """Update an email's details."""
        return self.email_dao.update_email(id, address, password, is_registered)

    def delete_email(self, id: int):
        """Delete an email by ID."""
        return self.email_dao.delete_email(id)