# CRUD Operations with SQLAlchemy

---

## Create A New Record
```python
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
```

---

## **Read** All Records
```python
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
```
To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database sesion we get back the rows in the database ( ``Result`` object). We then use ``scalars()`` to get the individual elements rather than entire rows.

---

## Read A Particular Record By Query
```python
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Influence")).scalar()
```
To get a single element we can use ``scalar()`` instead of ``scalars()``.

---

## Update A Particular Record By Query
```python
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Influence")).scalar()
    book_to_update.title = "Harry Potter"
    db.session.commit()
```

---

## Update A Record By PRIMARY KEY
```python
book_id = 1
with app.app_contex():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter"
    db.session.commit()
```
Flask-SQLAlchemy also has some handy extra query methods ``like get_or_404()`` that we can use Since Flask-SQLAlchemy version 3.0 the previous query methods like ``Book.query.get()`` have been deprecated.

---

## Dete A Particular Record By PRIMARY KEY
```python
book_id = 1
with app.app_contex():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
```
You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the ``get_or_404()`` method is quite handy.