from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geo_quiz.db'
    app.config['SECRET_KEY'] = 'developer-geo-app'

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        from . import models
        db.create_all()

    return app