from functions import convert_date

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

for book in books_to_insert:
    data = {
        key: (convert_date(value) if key == "published_date" else value)
        for (key, value) in book.items()
    }
    print(data)
