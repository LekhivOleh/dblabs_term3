from datetime import date
from src.booking.dao.credit_card_dao import CreditCardDao


class CreditCardService:
    def __init__(self, credit_card_dao: CreditCardDao):
        self.credit_card_dao = credit_card_dao

    def create_credit_card(self, is_blocked: bool, cvv: str, number: str, expiration_date: date, provider: str, user_id: int):
        """Create a new credit card."""
        return self.credit_card_dao.create_credit_card(is_blocked, cvv, number, expiration_date, provider, user_id)

    def get_all_credit_cards(self):
        """Retrieve all credit cards."""
        return self.credit_card_dao.get_all_credit_cards()

    def get_credit_card(self, id: int):
        """Retrieve a credit card by ID."""
        return self.credit_card_dao.get_credit_card(id)

    def update_credit_card(self, id: int, is_blocked: bool, cvv: str, number: str, expiration_date: date, provider: str, user_id: int):
        """Update a credit card's details."""
        return self.credit_card_dao.update_credit_card(id, is_blocked, cvv, number, expiration_date, provider, user_id)

    def delete_credit_card(self, id: int):
        """Delete a credit card by ID."""
        return self.credit_card_dao.delete_credit_card(id)

    def get_credit_cards_by_user(self, user_id: int):
        """Retrieve all credit cards by user."""
        return self.credit_card_dao.get_credit_cards_by_user(user_id)