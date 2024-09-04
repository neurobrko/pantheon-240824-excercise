from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Date,
)


# create table
def table_model(table_name, metadata):
    table = Table(
        table_name,
        metadata,
        Column("id", Integer, primary_key=True),
        Column("title", String),
        Column("author", String),
        Column("isbn", String),
        Column("published_date", Date),
    )
    return table
