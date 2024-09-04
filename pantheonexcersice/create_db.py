from sqlalchemy import create_engine, insert, MetaData
from functions import convert_date
from models import table_model

# create db
engine = create_engine("sqlite:///library.db", echo=True)
meta = MetaData()
# create table
books = table_model("books", meta)
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
