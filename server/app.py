#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Author, Book

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
            "Home": 'Welcome to My world',
        }
        resp = make_response(
            jsonify(resp_dict),
            200
        )
        return resp
api.add_resource(Home, '/')

class GetAuthor(Resource):
    def get(self):
        authorsNames = [author.to_dict() for author in Author.query.all()]

        resp = make_response(
            jsonify(authorsNames),
            200,
        )
        return resp
   
api.add_resource(GetAuthor, '/authors')

class GetBook(Resource):
     def get(self):
        bookNames = [book.to_dict() for book in Book.query.all()]

        resp = make_response(
            jsonify(bookNames),
            200,
        )
        return resp
api.add_resource(GetBook, '/books')
if __name__ == '__main__':
    app.run()