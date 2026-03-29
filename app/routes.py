"""Module for application routes."""
from flask import Blueprint, render_template, url_for, flash, redirect, request, session
from app import db
from app.models import Country
from app.forms import CountryForm, QuizAnswerForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Render the home page."""
    return render_template('index.html', title='Главная')

@main.route('/countries')
def countries_list():
    """Render the all countries page."""
    all_countries = Country.query.all()
    return render_template('countries.html', countries=all_countries)

@main.route('/add_country', methods=['GET', 'POST'])
def add_country():
    """Render the page for adding new country."""
    form = CountryForm()
    if form.validate_on_submit():
        new_country = Country(
            name=form.name.data,
            capital=form.capital.data,
            continent=form.continent.data
        )
        db.session.add(new_country)
        db.session.commit()
        flash(f'Страна {form.name.data} успешно добавлена!', 'success')
        return redirect(url_for('main.countries_list'))
    return render_template('admin.html', title='Админка', form=form)


@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Render the page for quiz play."""
    form = QuizAnswerForm()

    country_id = session.get('quiz_country_id')
    country = None

    if country_id:
        country = Country.query.get(country_id)

    if not country:
        country = Country.query.order_by(db.func.random()).first()
        if country:
            session['quiz_country_id'] = country.id

    if form.validate_on_submit():
        user_answer = form.answer.data.strip().lower()
        correct_answer = country.capital.lower()

        if user_answer == correct_answer:
            flash(f'Правильно! Столица {country.name} — это {country.capital}.', 'success')
        else:
            flash(f'Ошибка! Столица {country.name} — {country.capital}.', 'danger')

        session.pop('quiz_country_id', None)
        return redirect(url_for('main.quiz'))

    return render_template('quiz.html', title='Викторина', country=country, form=form)
