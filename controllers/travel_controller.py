from flask import Flask, render_template, request, redirect
from repositories import city_repository, country_repository
from models.city import City

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)