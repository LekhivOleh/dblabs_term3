from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from dotenv import load_dotenv
import os

db = SQLAlchemy()

load_dotenv()
db_uri = (
    os.getenv("db-uri")
    or os.getenv("DB_URI")
    or os.getenv("SQLALCHEMY_DATABASE_URI")
)

if not db_uri:
    raise RuntimeError("db-uri is not read correctly")

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)

    from src.booking.controller.email_controller import email_bp
    from src.booking.controller.location_controller import location_bp
    from src.booking.controller.credit_card_controller import credit_card_bp
    from src.booking.controller.room_has_amenity_controller import room_has_amenity_bp, amenity_has_room_bp


    app.register_blueprint(email_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(credit_card_bp)
    app.register_blueprint(room_has_amenity_bp)
    app.register_blueprint(amenity_has_room_bp)

    @app.route('/')
    def hello_world():
        return 'Hello, World! update again'

    @app.route('/ping')
    def ping():
        return 'pong'

    return app
