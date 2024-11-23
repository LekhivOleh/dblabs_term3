from src.booking.domain.models import Location

class LocationDao:
    def __init__(self, session):
        self.session = session

    def create_location(self, country, region, city, street, house_number):
        new_location = Location(country=country, region=region, city=city, street=street, house_number=house_number)
        self.session.add(new_location)
        self.session.commit()
        return new_location

    def get_all_locations(self):
        return self.session.query(Location).all()

    def get_location(self, id):
        return self.session.query(Location).get(id)

    def update_location(self, id, country, region, city, street, house_number):
        location = self.session.query(Location).get(id)
        if location:
            location.country = country
            location.region = region
            location.city = city
            location.street = street
            location.house_number = house_number
            self.session.commit()
        return location

    def delete_location(self, id):
        location = self.session.query(Location).get(id)
        if location:
            self.session.delete(location)
            self.session.commit()
        return location