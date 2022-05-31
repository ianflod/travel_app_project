from flask import Flask, render_template, request, redirect
from repositories import city_repository, country_repository
from models.city import City
from models.country import Country


from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

#Create
#GET '/cities/new_country'

@countries_blueprint.route("/countries/new_country", methods=['GET'])
def new_country():
    return render_template("countries/new_country.html")


@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    title = request.form['country_name']

    country = Country(title)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries", methods=['GET'])
def show_countries():
    countries = country_repository.select_all()
    return render_template('/countries/show.html', all_countries = countries)