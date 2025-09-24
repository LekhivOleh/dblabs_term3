from flask import Blueprint, request, jsonify
from src.booking.dao.location_dao import LocationDao
from src import db
from src.booking.services.location_service import LocationService
from flasgger import swag_from

location_bp = Blueprint('location_bp', __name__)
location_dao = LocationDao(db.session)
location_service = LocationService(location_dao)

@location_bp.route('/location', methods=['POST'])
@swag_from({
    'tags': ['Location'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'country': {'type': 'string'},
                    'region': {'type': 'string'},
                    'city': {'type': 'string'},
                    'street': {'type': 'string'},
                    'house_number': {'type': 'string'}
                },
                'required': ['country', 'region', 'city', 'street', 'house_number']
            }
        }
    ],
    'responses': {
        201: {'description': 'Location created'}
    }
})
def create_location_route():
    data = request.get_json()
    new_location = location_service.create_location(data['country'], data['region'], data['city'], data['street'], data['house_number'])
    return jsonify(new_location.serialize()), 201

@location_bp.route('/location', methods=['GET'])
@swag_from({
    'tags': ['Location'],
    'responses': {
        200: {'description': 'List all locations'}
    }
})
def get_all_locations_route():
    locations = location_service.get_all_locations()
    return jsonify([location.serialize() for location in locations])

@location_bp.route('/location/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Location'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Get location by ID'}
    }
})
def get_location_route(id):
    location = location_service.get_location(id)
    return jsonify(location.serialize())

@location_bp.route('/location/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Location'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'country': {'type': 'string'},
                    'region': {'type': 'string'},
                    'city': {'type': 'string'},
                    'street': {'type': 'string'},
                    'house_number': {'type': 'string'}
                },
                'required': ['country', 'region', 'city', 'street', 'house_number']
            }
        }
    ],
    'responses': {
        200: {'description': 'Location updated'}
    }
})
def update_location_route(id):
    data = request.get_json()
    location = location_service.update_location(id, data['country'], data['region'], data['city'], data['street'], data['house_number'])
    return jsonify(location.serialize())

@location_bp.route('/location/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Location'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        204: {'description': 'Location deleted'}
    }
})
def delete_location_route(id):
    location_service.delete_location(id)
    return 'Location is deleted', 204