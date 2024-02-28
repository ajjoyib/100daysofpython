# main.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

# CREATE A DATABASE
Base = declarative_base()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    __tablename__ = "books"

    id: int = db.Column(Integer, primary_key=True)
    title: str = db.Column(String(250), unique=True, nullable=False)
    author: str = db.Column(String(250), nullable=False)
    rating: float = db.Column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}"


# Create table schema in the database.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL THE RECORDS
    # Construct a query to select from the database.
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.session.query(Book).filter_by(id=book_id).first()
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = db.session.query(Book).filter_by(id=book_id).first()
    return render_template("edit_rating.html", book=book_selected)



@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    # DELETE A RECORD BY ID
    book_to_delete = db.session.query(Book).filter_by(id=book_id).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
