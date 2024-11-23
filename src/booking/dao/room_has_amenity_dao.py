from src.booking.domain.models import RoomHasAmenity, Room, Amenity

class RoomHasAmenityDao:
    def __init__(self, session):
        self.session = session

    def get_amenities_by_room(self, room_id):
        return self.session.query(Amenity).join(RoomHasAmenity, Amenity.id == RoomHasAmenity.amenity_id).filter(RoomHasAmenity.room_id == room_id).all()

    def get_rooms_by_amenity(self, amenity_id):
        return self.session.query(Room).join(RoomHasAmenity, Room.id == RoomHasAmenity.room_id).filter(RoomHasAmenity.amenity_id == amenity_id).all()