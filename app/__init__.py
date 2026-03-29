from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'developer-geo-app'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geo_quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # ВАЖНО: Импорт внутри функции, чтобы избежать циклических зависимостей
    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        from . import models
        db.create_all()

    return app