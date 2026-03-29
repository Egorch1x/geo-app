"""Module for application routes."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models import Country


class CountryForm(FlaskForm):
    """Form for country"""
    name = StringField('Название страны', validators=[
        DataRequired(message="Введите название страны"),
        Length(min=2, max=100, message="Название должно быть от 2 до 100 символов")
    ])

    capital = StringField('Столица', validators=[
        DataRequired(message="Введите название столицы"),
        Length(min=2, max=100, message="Название должно быть от 2 до 100 символов")
    ])

    continent = SelectField('Континент', choices=[
        ('Европа', 'Европа'),
        ('Азия', 'Азия'),
        ('Африка', 'Африка'),
        ('Северная Америка', 'Северная Америка'),
        ('Южная Америка', 'Южная Америка'),
        ('Океания', 'Океания')
    ])

    submit = SubmitField('Сохранить')

    def validate_name(self, name):
        """Validate name."""
        country = Country.query.filter_by(name=name.data).first()
        if country:
            raise ValidationError('Такая страна уже есть')

class QuizAnswerForm(FlaskForm):
    """Quiz answer form"""
    answer = StringField('Ваш ответ',
                         validators=[DataRequired(message="Поле не может быть пустым")])
    submit = SubmitField('Проверить')
