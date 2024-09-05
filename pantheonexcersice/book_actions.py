from sqlalchemy import create_engine, insert, MetaData, select, delete, update
from functions import fix_published_date
from models import table_model

engine = create_engine("sqlite:///library.db", echo=True)
meta = MetaData()
table = table_model("books", meta)


def insert_single_book(book, eng=engine, tbl=table):
    with eng.connect() as conn:
        book = fix_published_date(book)
        stmt = insert(tbl).values(book)
        conn.execute(stmt)
        conn.commit()


def insert_multiple_books(books, eng=engine, tbl=table):
    with eng.connect() as conn:
        for book in books:
            book = fix_published_date(book)
            stmt = insert(tbl).values(book)
            conn.execute(stmt)
        conn.commit()


def get_books_list(eng=engine, tbl=table):
    with eng.connect() as conn:
        stmt = select(tbl.c["id", "title", "author"])
        result = conn.execute(stmt).fetchall()
        conn.commit()
    return result


def get_book_detail(book_id, eng=engine, tbl=table):
    book_id = str(book_id)
    with engine.connect() as conn:
        stmt = select(tbl).where(tbl.c.id == book_id)
        result = conn.execute(stmt).fetchone()
        conn.commit()
    return result


def delete_book(book_id, eng=engine, tbl=table):
    book_id = str(book_id)
    with engine.connect() as conn:
        stmt = delete(tbl).where(tbl.c.id == book_id)
        conn.execute(stmt)
        conn.commit()


def update_book(book, eng=engine, tbl=table):
    book_id = str(book["id"])
    del book["id"]

    with engine.connect() as conn:
        update_values = fix_published_date(book)
        stmt = update(tbl).where(tbl.c.id == book_id).values(update_values)
        conn.execute(stmt)
        conn.commit()
