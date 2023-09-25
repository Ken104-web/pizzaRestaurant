#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Define a Resource for the Home route
class Home(Resource):
    def get(self):
        resp_dict = {
            "Home": 'Welcome to Pizza-restaurant RESTful API',
        }
        resp = make_response(
            jsonify(resp_dict),
            200
        )
        return resp

api.add_resource(Home, '/')

# Define a Resource for retrieving restaurant names
class RestauranrtNames(Resource):
    def get(self):
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        
        resp = make_response(
            restaurants,
            200,
        )
        return resp

api.add_resource(RestauranrtNames, '/pizzaplace')

# Define a Resource for retrieving pizza data
class GetPizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]

        resp = make_response(
            jsonify(pizzas),
            200,
        )
        return resp

api.add_resource(GetPizzas, '/pizzas')

# Define a Resource for creating a new pizza
class PostPizzas(Resource):
    def post(self):
        data = request.get_json()

        new_pizza = Pizza(
            id=data['id'],
            name=data['name'],
            ingredients=data['ingredients'],
        )
        db.session.add(new_pizza)
        db.session.commit()
        return make_response(new_pizza.to_dict(), 201)

api.add_resource(PostPizzas, '/postpizza')

# Define a Resource for retrieving and deleting pizza data by ID
class RestaurantNamesWithId(Resource):
    def get(self, id):
        pizza_name = Pizza.query.filter_by(id=id).first()
        if pizza_name:
            pizza_data = pizza_name.to_dict()
            resp = make_response(
                pizza_data,
                200,
            )
            return resp
        else:
            raise ValueError('Restaurant not found!')
    
    def delete(self, id):
        pizza_name = Pizza.query.filter_by(id=id).first()
        db.session.delete(pizza_name)
        db.session.commit()
        resp = make_response(
            '',
            204,
        )
        return resp

api.add_resource(RestaurantNamesWithId, '/pizzaplace/<int:id>')

if __name__ == '__main__':
    app.run()
