from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, DevelopmentConfig

# Initialize extensions
# SQLAlchemy for ORM
db = SQLAlchemy()
# Migrate for database migrations
migrate = Migrate()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so that they are registered with SQLAlchemy
    from app.models import ClassModel, BookingModel

    # Register blueprints
    from app.routes.class_routes import class_bp
    from app.routes.booking_routes import booking_bp
    app.register_blueprint(class_bp, url_prefix='/api/classes')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')

    # You can add other blueprints in a similar fashion

    # Error handlers, middleware, or any additional configuration can go here

    return app
