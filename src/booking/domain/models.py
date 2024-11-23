from sqlalchemy import BigInteger, Column, Date, Float, ForeignKey, Integer, String, DECIMAL, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Amenity(Base):
    __tablename__ = 'amenity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)
    description = Column(String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(45), nullable=False, unique=True)
    password = Column(String(45), nullable=False)
    is_registered = Column(TINYINT(1), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'password': self.password,
            'is_registered': bool(self.is_registered)
        }


class HotelsFranchise(Base):
    __tablename__ = 'hotels_franchise'

    id = Column(Integer, primary_key=True, autoincrement=True)
    foundation_date = Column(Date, nullable=False)
    founder = Column(String(45), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'foundation_date': self.foundation_date.isoformat(),
            'founder': self.founder
        }


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(45), nullable=False)
    region = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    street = Column(String(45), nullable=False)
    house_number = Column(String(45), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'country': self.country,
            'region': self.region,
            'city': self.city,
            'street': self.street,
            'house_number': self.house_number
        }


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, index=True)
    foundation_date = Column(Date, nullable=False)
    head_manager = Column(String(45), nullable=False)
    hotels_franchise_id = Column(ForeignKey('hotels_franchise.id'), nullable=False, index=True)
    location_id = Column(ForeignKey('location.id'), nullable=False, index=True)

    hotels_franchise = relationship('HotelsFranchise')
    location = relationship('Location')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'foundation_date': self.foundation_date,
            'head_manager': self.head_manager,
            'hotels_franchise': self.hotels_franchise.serialize(),
            'location': self.location.serialize()
        }


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), nullable=False, unique=True)
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)
    email_id = Column(ForeignKey('email.id'), nullable=False, unique=True)

    email = relationship('Email')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email.serialize()
        }


class CreditCard(Base):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_blocked = Column(TINYINT(1), nullable=False)
    cvv = Column(String(3), nullable=False)
    number = Column(BigInteger, nullable=False, unique=True)
    expiration_date = Column(Date, nullable=False)
    provider = Column(String(45), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, unique=True)

    user = relationship('User')

    def serialize(self):
        return {
            'id': self.id,
            'is_blocked': bool(self.is_blocked),
            'cvv': self.cvv,
            'number': self.number,
            'expiration_date': self.expiration_date,
            'provider': self.provider,
            'user_id': self.user_id
        }


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(45), nullable=False, unique=True)
    type = Column(String(45), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False, index=True)
    is_available = Column(TINYINT(1), nullable=False)
    when_available = Column(String(45))
    hotel_id = Column(ForeignKey('hotel.id'), nullable=False, index=True)

    hotel = relationship('Hotel')

    def serialize(self):
        return {
            'id': self.id,
            'number': self.number,
            'type': self.type,
            'price': self.price,
            'is_available': self.is_available,
            'when_available': self.when_available,
            'hotel_id': self.hotel_id
        }


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255))
    score = Column(TINYINT, nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    room_id = Column(ForeignKey('room.id'), nullable=False, index=True)

    room = relationship('Room')
    user = relationship('User')

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'score': self.score,
            'user': self.user.serialize(),
            'room': self.room.serialize()
        }


class RoomHasUser(Base):
    __tablename__ = 'room_has_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(ForeignKey('room.id'), nullable=False, index=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    room = relationship('Room')
    user = relationship('User')

    def serialize(self):
        return {
            'id': self.id,
            'room_id': self.room_id,
            'user_id': self.user_id
        }


class RoomHasAmenity(Base):
    __tablename__ = 'room_has_amenity'
    room_id = Column(Integer, ForeignKey('room.id'), primary_key=True)
    amenity_id = Column(Integer, ForeignKey('amenity.id'), primary_key=True)

    room = relationship('Room', backref='room_has_amenities')
    amenity = relationship('Amenity', backref='room_has_amenities')

    def serialize(self):
        return {
            'room_id': self.room_id,
            'amenity_id': self.amenity_id
        }