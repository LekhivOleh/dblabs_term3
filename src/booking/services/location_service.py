from src.booking.dao.location_dao import LocationDao


class LocationService:
    def __init__(self, location_dao: LocationDao):
        self.location_dao = location_dao

    def create_location(self, country: str, region: str, city: str, street: str, house_number: str):
        """Create a new location."""
        return self.location_dao.create_location(country, region, city, street, house_number)

    def get_all_locations(self):
        """Retrieve all locations."""
        return self.location_dao.get_all_locations()

    def get_location(self, id: int):
        """Retrieve a location by ID."""
        return self.location_dao.get_location(id)

    def update_location(self, id: int, country: str, region: str, city: str, street: str, house_number: str):
        """Update a location's details."""
        return self.location_dao.update_location(id, country, region, city, street, house_number)

    def delete_location(self, id: int):
        """Delete a location by ID."""
        return self.location_dao.delete_location(id)