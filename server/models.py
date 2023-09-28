from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()

class Author(db.Model, SerializerMixin):
    __tablename__ = "authors"

    serialize_rules = ('-books.author',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship('Book', backref='author')

    # def to_dict(self):
    #     # return {
    #     #     'id': self.id,
    #     #     'name': self.name
    #     # }
    def __repr__(self):
        return f"Author: {self.name}"
    
class Book(db.Model,SerializerMixin):
    __tablename__ = "books"

    serialize_rules = ('-author.books',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    # def to_dict(self):
    #     return{
    #         'id': self.id,
    #         'name': self.name
    #     }

    def __repr__(self):
        return f"Book: {self.name}"