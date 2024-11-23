from flask import Blueprint, request, jsonify
from src.booking.dao.credit_card_dao import CreditCardDao
from src import db
from src.booking.services.credit_card_service import CreditCardService
from datetime import datetime


credit_card_bp = Blueprint('credit_card_bp', __name__)
credit_card_dao = CreditCardDao(db.session)
credit_card_service = CreditCardService(credit_card_dao)

@credit_card_bp.route('/credit_card', methods=['POST'])
def create_credit_card_route():
    data = request.get_json()
    expiration_date = datetime.strptime(data['expiration_date'], '%a, %d %b %Y').date()
    new_credit_card = credit_card_service.create_credit_card(data['is_blocked'], data['cvv'], data['number'], expiration_date, data['provider'], data['user_id'])
    return jsonify(new_credit_card.serialize()), 201

@credit_card_bp.route('/credit_card', methods=['GET'])
def get_all_credit_cards_route():
    credit_cards = credit_card_service.get_all_credit_cards()
    return jsonify([credit_card.serialize() for credit_card in credit_cards])

@credit_card_bp.route('/credit_card/<int:id>', methods=['GET'])
def get_credit_card_route(id):
    credit_card = credit_card_service.get_credit_card(id)
    return jsonify(credit_card.serialize())


from datetime import datetime


@credit_card_bp.route('/credit_card/<int:id>', methods=['PUT'])
def update_credit_card_route(id):
    data = request.get_json()
    expiration_date = datetime.strptime(data['expiration_date'], '%a, %d %b %Y').date()
    credit_card = credit_card_service.update_credit_card(
        id,
        data['is_blocked'],
        data['cvv'],
        data['number'],
        expiration_date,
        data['provider'],
        data['user_id']
    )
    return jsonify(credit_card.serialize())


@credit_card_bp.route('/credit_card/<int:id>', methods=['DELETE'])
def delete_credit_card_route(id):
    credit_card_service.delete_credit_card(id)
    return 'Credit card is deleted', 204

@credit_card_bp.route('/credit_card/<int:id>/user', methods=['GET'])
def get_credit_cards_by_user_route(id):
    credit_cards = credit_card_service.get_credit_cards_by_user(id)
    return jsonify([credit_card.serialize() for credit_card in credit_cards])