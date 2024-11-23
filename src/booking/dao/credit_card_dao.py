from src.booking.domain.models import CreditCard


class CreditCardDao:
    def __init__(self, session):
        self.session = session

    def create_credit_card(self, is_blocked, cvv, number, expiration_date, provider, user_id):
        new_credit_card = CreditCard(is_blocked=is_blocked, cvv=cvv, number=number, expiration_date=expiration_date, provider=provider, user_id=user_id)
        self.session.add(new_credit_card)
        self.session.commit()
        return new_credit_card

    def get_all_credit_cards(self):
        return self.session.query(CreditCard).all()

    def get_credit_card(self, id):
        return self.session.query(CreditCard).get(id)

    def update_credit_card(self, id, is_blocked, cvv, number, expiration_date, provider, user_id):
        credit_card = self.session.query(CreditCard).get(id)
        if credit_card:
            credit_card.is_blocked = is_blocked
            credit_card.cvv = cvv
            credit_card.number = number
            credit_card.expiration_date = expiration_date
            credit_card.provider = provider
            credit_card.user_id = user_id
            self.session.commit()
        return credit_card

    def delete_credit_card(self, id):
        credit_card = self.session.query(CreditCard).get(id)
        if credit_card:
            self.session.delete(credit_card)
            self.session.commit()
        return credit_card

    def get_credit_cards_by_user(self, id):
        return self.session.query(CreditCard).filter_by(user_id=id).all()