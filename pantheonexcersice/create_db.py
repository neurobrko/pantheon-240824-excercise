from sqlalchemy import (
    create_engine,
    insert,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Date,
)
from datetime import datetime


def convert_date(dateString, dateFormat="%Y-%m-%d"):
    dt = datetime.strptime(dateString, dateFormat)
    return dt


# create db
engine = create_engine("sqlite:///library.db", echo=True)
meta = MetaData()

# create table
books = Table(
    "books",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("author", String),
    Column("isbn", String),
    Column("published_date", Date),
)
meta.create_all(engine)

# insert test data
stmt = insert(books).values(
    title="A Voyage for Madman",
    author="Peter Nichols",
    isbn="9780060957032",
    published_date=convert_date("2002-06-04"),
)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
