#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


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

class RestauranrtNames(Resource):
    def get(self):
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        
        resp = make_response(
            restaurants,
            200,
        )
        return resp
api.add_resource(RestauranrtNames, '/pizzaplace')

class GetPizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]

        resp = make_response(
            jsonify(pizzas),
            200,
        )
        return resp
api.add_resource(GetPizzas, '/pizzas')

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