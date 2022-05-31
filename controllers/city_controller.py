from flask import Flask, render_template, request, redirect
from repositories import city_repository, country_repository
from models.city import City
from models.country import Country
  

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)

# INDEX
# GET '/cities'
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/index.html", all_cities = cities)

#NEW
# GET '/cities/new'  this is selecting all countries to populate into the new city form
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)


# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    completed =bool(int(request.form['completed']))

    country = country_repository.select(country_id)
    city = City(name, country, completed)

    city_repository.save(city)
    return redirect('/cities')

# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

# EDIT
# GET '/cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

# UPDATE
# PUT not available with html only, so using POST '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']  #These are from the form get them right!!!
    country_id = request.form['country_id']
    completed =bool(int(request.form['completed']))

    country = country_repository.select(country_id)
    city = City(name, country, completed, id)

    city_repository.update(city)
    return redirect('/cities')

# DELETE
# DELETE '/cities/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect ('/cities')