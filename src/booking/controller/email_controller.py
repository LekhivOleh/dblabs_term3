from flask import Blueprint, request, jsonify
from src.booking.services.email_service import EmailService
from src.booking.dao.email_dao import EmailDao
from src import db


email_bp = Blueprint('email_bp', __name__)
email_dao = EmailDao(db.session)
email_service = EmailService(email_dao)


@email_bp.route('/email', methods=['POST'])
def create_email_route():
    data = request.get_json()
    new_email = email_service.create_email(data['address'], data['password'], data['is_registered'])
    return jsonify(new_email.serialize()), 201


@email_bp.route('/email', methods=['GET'])
def get_all_emails_route():
    emails = email_service.get_all_emails()
    return jsonify([email.serialize() for email in emails])


@email_bp.route('/email/<int:id>', methods=['GET'])
def get_email_route(id):
    email = email_service.get_email(id)
    return jsonify(email.serialize())


@email_bp.route('/email/<int:id>', methods=['PUT'])
def update_email_route(id):
    data = request.get_json()
    email = email_service.update_email(id, data['address'], data['password'], data['is_registered'])
    return jsonify(email.serialize())


@email_bp.route('/email/<int:id>', methods=['DELETE'])
def delete_email_route(id):
    email_service.delete_email(id)
    return 'Email is deleted', 204