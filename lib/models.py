from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))  
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))  
    price = db.Column(db.Numeric(precision=3, asdecimal=True, decimal_return_scale=None))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validate_restaurantPizza_price(self, key, value):
        if 1 <= value <= 30:
            return value
        else:
            raise ValueError('Price is not within the required range')

    @validates('name')
    def validate_pizza_name(self, key, value):
        if len(value) >= 50:
            raise ValueError('Exceeded character limit for pizza name')
        return value
