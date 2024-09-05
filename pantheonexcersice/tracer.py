from book_actions import get_book_detail, get_books_list, delete_book, update_book

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

book_details = {
    "id": 12,
    "author": "Terry Pratchett",
}
update_book(book_details)
book = get_book_detail(12)
print(book)
