from app import app
from models import db, Author, Book
from random import randint, choice as rc
with app.app_context():
    Author.query.delete()
    # Book.query.delete()

    authors = [
        "William Shakespeare",
        "Jane Austen",
        "Charles Dickens",
        "F. Scott Fitzgerald",
        "Mark Twain",
        "George Orwell",
        "J.K. Rowling",
        "Ernest Hemingway",
        "Agatha Christie",
        "Toni Morrison",
        "Leo Tolstoy",
        "Gabriel García Márquez",
        "Harper Lee",
        "Stephen King",
        "J.R.R. Tolkien",
        "Virginia Woolf",
        "Maya Angelou",
        "Oscar Wilde",
        "John Steinbeck",
        "Emily Brontë"
 ]
    book_names = [
    "To Kill a Mockingbird",
    "1984" ,
    "Pride and Prejudice", 
    "The Great Gatsby", 
    "The Catcher in the Rye", 
    "Harry Potter and the Sorcerer's Stone", 
    "The Lord of the Rings", 
    "War and Peace", 
    "Brave New World", 
    "The Hobbit", 
    "Moby-Dick", 
    "The Hunger Games", 
    "Crime and Punishment",
    "The Odyssey", 
    "The Alchemist", 
    "Frankenstein", 
    "The Road", 
    "To the Lighthouse", 
    "The Da Vinci Code", 
    "The Shining"
    ]
    known_authors = []
    for a in range(21):
        print('all good')
        place_authors = Author(name=rc(authors))
        known_authors.append(place_authors)
    db.session.add_all(known_authors)
    db.session.commit()
    print('***print***')

    known_books = []
    for bk in range(21):
        print('all good')
        place_books = Book(name=rc(book_names), author_id=randint(1,21))
        known_books.append(place_books)
        print('All good here')
    db.session.add_all(known_books)
    db.session.commit()