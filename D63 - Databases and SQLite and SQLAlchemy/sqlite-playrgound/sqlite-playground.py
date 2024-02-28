from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# Create database
Base = declarative_base()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)


# Create the table
class Book(db.Model):
    __tablename__ = "books" # Add this line to specify the table name

    id: int = db.Column(Integer, primary_key=True)
    title: str = db.Column(String(250), unique=True, nullable=False)
    author: str = db.Column(String(250), nullable=False)
    rating: float = db.Column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# # Create Record
with app.app_context():
    # Crate a new Book instance
    new_book = Book(id=1, title="Influence", author="Robert Cialdini", rating=9.3)
    # Add the new_book to the session
    db.session.add(new_book)
    # Commit the session to insert the record
    db.session.commit()
