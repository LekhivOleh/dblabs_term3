from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import yaml

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    with open('config/app.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']

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
        return 'Hello, World!'

    @app.route('/ping')
    def ping():
        return 'pong'

    return app
