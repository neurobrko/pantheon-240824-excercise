from sqlalchemy import create_engine, MetaData, select, delete, update
from models import table_model
from pantheonexcersice.functions import fix_published_date

books_to_insert = [
    {
        "title": "Night Watch",
        "author": "Terry Pratchett",
        "isbn": "9780060957033",
        "published_date": "2005-05-07",
    },
    {
        "title": "Feet of Clay",
        "author": "Terry Pratchett",
        "isbn": "9780060957034",
        "published_date": "2007-05-07",
    },
    {
        "title": "Hitchhikers Guide to the Galaxy",
        "author": "Douglas Adams",
        "isbn": "9780060957035",
        "published_date": "1998-04-05",
    },
]

book_to_edit = {
    "id": 12,
    "title": "Night Watch",
    "author": "Terry Pratchett",
    "isbn": "9780060957033",
    "published_date": "2005-05-07",
}

engine = create_engine("sqlite:///library.db", echo=True)
meta = MetaData()
books = table_model("books", meta)

book_id = str(book_to_edit["id"])
del book_to_edit["id"]

with engine.connect() as conn:
    update_values = fix_published_date(book_to_edit)
    stmt = update(books).where(books.c.id == book_id).values(update_values)
    conn.execute(stmt)
    conn.commit()
