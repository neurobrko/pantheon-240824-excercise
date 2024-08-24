from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

engine = create_engine("sqlite://library.db", echo=True)
meta = MetaData()

book = Table(
    "book",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("author", String),
    Column("isbn", String),
    Column("published_date", Date),
)
