from sqlalchemy import create_engine, MetaData, select
from models import table_model

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

engine = create_engine("sqlite:///library.db", echo=True)
meta = MetaData()
books = table_model("books", meta)
book_id = 1
book_id = str(book_id)

with engine.connect() as conn:
    stmt = select(books).where(books.c.id == book_id)
    result = conn.execute(stmt)
    conn.commit()

print(result.fetchone())
