#!/usr/bin/env python3
from random import choice as rc

from app import app
from models import db, Restaurant, Pizza


with app.app_context():
    Restaurant.query.delete()

    addresses = ['Good Italian, Ngong Road, 5th Avenue', 'Westgate Mall, Mwanzi Road, Nrb 100', '456 Elm Street, Another City, USA']
    pizzaPlaces = ['Dominions', 'Pizza hut','Papa jones pizza' ]
    pizza = []
    for n in range(4):
        print('****Hello*****')
        pn = Restaurant(name=rc(pizzaPlaces), address=rc(addresses))
        pizza.append(pn)
    db.session.add_all(pizza)
    db.session.commit()
    print("****Done****")

    

