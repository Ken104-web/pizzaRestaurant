from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship('Book', backref='author')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name
        }