"""Module for application routes."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import main

db = SQLAlchemy()

def create_app():
    """Creates Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'developer-geo-app'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geo_quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
