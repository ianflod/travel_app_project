from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id, completed) VALUES (?, ?, ?) RETURNING *"
    values = [city.name, city.country.id, city.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        completed = True if row['completed'] == 1 else False
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, completed, row['id'] )
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        completed = True if result['completed'] == 1 else False
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, completed, result['id'] )
    return city

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country_id, completed) = (?, ?, ?) WHERE id = ?"
    values = [city.name, city.country.id, city.completed, city.id]
    run_sql(sql, values)