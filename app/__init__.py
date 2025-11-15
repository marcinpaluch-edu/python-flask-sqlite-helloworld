from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="development"):
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(f"app.config.{config_name.capitalize()}Config")
    
    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    
    return app