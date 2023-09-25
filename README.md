# Pizza Restaurant

An independent project that focuses on building API's and assigning various HTTP verbs.

# Key topics to learn
HTTP verbs
Flask-migrations
Flask Api
Validations and Constraint

#  How it's Made
Created the following relationships:
A '```Restaurant``` has many Pizzas through ```RestaurantPizza```

A ```Pizza``` has many ```Restaurants ```through ```RestaurantPizza```

A ```RestaurantPizza``` belongs to a Restaurant and belongs to a Pizza

# Routes
The project includes various routes each handling various Http verbs including ```GET```, ```POST``` showcasing data made in the database.


# Project Setup
 Clone the Repo

you can clone the repo using:

```git@github.com:Ken104-web/pizzaRestaurant.git```

navigate to the project directory

```cd pizzaRestaurant```

install project dependancies using pipenv including:

flask 
flask-migrate
flask-sqlalchemy
flask-restful 

# running the Api

Start the development server:
```flask run```

You can access the API in your web browser or use a tool like curl or Postman to send requests to the API endpoints.

# Api Endponts

 - `/`: Home route with a welcome message.
 - `/pizzaplace`: Get a list of restaurant names.
 - `/pizzas`: Get a list of available pizzas.
 - `/postpizza`: Create a new pizza by sending a POST request with JSON data.
 -  `/pizzaplace/<int:id>`: Get or delete a pizza by its ID.

# Author 
Kennth Mwangi