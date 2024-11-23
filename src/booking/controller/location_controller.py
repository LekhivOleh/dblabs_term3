from flask import Blueprint, request, jsonify
from src.booking.dao.location_dao import LocationDao
from src import db
from src.booking.services.location_service import LocationService

location_bp = Blueprint('location_bp', __name__)
location_dao = LocationDao(db.session)
location_service = LocationService(location_dao)

@location_bp.route('/location', methods=['POST'])
def create_location_route():
    data = request.get_json()
    new_location = location_service.create_location(data['country'], data['region'], data['city'], data['street'], data['house_number'])
    return jsonify(new_location.serialize()), 201

@location_bp.route('/location', methods=['GET'])
def get_all_locations_route():
    locations = location_service.get_all_locations()
    return jsonify([location.serialize() for location in locations])

@location_bp.route('/location/<int:id>', methods=['GET'])
def get_location_route(id):
    location = location_service.get_location(id)
    return jsonify(location.serialize())

@location_bp.route('/location/<int:id>', methods=['PUT'])
def update_location_route(id):
    data = request.get_json()
    location = location_service.update_location(id, data['country'], data['region'], data['city'], data['street'], data['house_number'])
    return jsonify(location.serialize())

@location_bp.route('/location/<int:id>', methods=['DELETE'])
def delete_location_route(id):
    location_service.delete_location(id)
    return 'Location is deleted', 204