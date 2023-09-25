from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates



db = SQLAlchemy()


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingedients':self.ingredients
        }
    
    restaurants = db.relationship("Restaurant", secondary = "restaurant_pizzas" , back_populates="pizzas") 

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    pizzas = db.relationship("Pizza", secondary = "restaurant_pizzas" , back_populates = "restaurants")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
    @validates("name")
    def validate_name(self, key, name):
        if len(name) >50:
            raise ValueError ("Name's length too much!")
        return name

    
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer , db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer , db.ForeignKey("restaurants.id"))
    price = db.Column(db.Numeric(precision=8, asdecimal=True, decimal_return_scale=None))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates("price")
    def validate_price(self, key, price):
        if not(price >= 1 and price <=30):
            raise ValueError("Price range not met!")
        return price
            
    