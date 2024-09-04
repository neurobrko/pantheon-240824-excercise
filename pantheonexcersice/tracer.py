from book_actions import get_book_detail

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
book = get_book_detail("1")
print(book)
