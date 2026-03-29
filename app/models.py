"""Module for application routes."""
from app import db

class Country(db.Model):
    """Models for countries."""
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    capital = db.Column(db.String(100), nullable=False)
    continent = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Страна {self.name}>'

class QuizResult(db.Model):
    """Models for quiz results."""
    __tablename__ = 'quiz_results'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_played = db.Column(db.DateTime, server_default=db.func.now())
