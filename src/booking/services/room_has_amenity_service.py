from src.booking.dao.room_has_amenity_dao import RoomHasAmenityDao

class RoomHasAmenityService:
    def __init__(self, room_has_amenity_dao: RoomHasAmenityDao):
        self.room_has_amenity_dao = room_has_amenity_dao

    def get_amenities_by_room(self, room_id: int):
        return self.room_has_amenity_dao.get_amenities_by_room(room_id)

    def get_rooms_by_amenity(self, amenity_id: int):
        return self.room_has_amenity_dao.get_rooms_by_amenity(amenity_id)