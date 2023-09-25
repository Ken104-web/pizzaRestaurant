#!/usr/bin/env python3
from random import choice as rc

from app import app
from models import db, Restaurant, Pizza


with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()

    addresses = ['Good Italian, Ngong Road, 5th Avenue', 'Westgate Mall, Mwanzi Road, Nrb 100', '456 Elm Street, Another City, USA']
    pizzaPlaces = ['Dominions', 'Pizza hut','Papa jones pizza' ]
    restaurant = []
    for n in range(10):
        print('****Hello*****')
        pn = Restaurant(name=rc(pizzaPlaces), address=rc(addresses))
        restaurant.append(pn)
    db.session.add_all(restaurant)
    db.session.commit()
    print("****Done****")

    pizzasNames = [ 'Mushroom Magic',
                    'Italian Stallion',
                    'Tandoori Temptation']
    
    pizzaIngredients = ['Buffalo sauce or ranch dressing Mozzarella cheese', 'Mozzarella cheeseParmesan cheeseRicotta cheese'
    'Kalamata olives Red onions Cherry tomatoes']
    pizzas = []
    for i in range(10):
        p = Pizza(name=rc(pizzasNames), ingredients=rc(pizzaIngredients))
        pizzas.append(p)
    db.session.add_all(pizzas)
    db.session.commit()
    print('***All Okay***')





