from datetime import datetime


def convert_date(date_string, date_format="%Y-%m-%d"):
    dt = datetime.strptime(date_string, date_format)
    return dt


def fix_published_date(book_dict):
    fixed_book = {
        key: (convert_date(value) if key == "published_date" else value)
        for (key, value) in book_dict.items()
    }
    return fixed_book
