#!/bin/env python
import sys
from enum import Enum, auto
from typing import List

# data class
class User:
    def __init__(self, id: str, name: str, address: str):
        self.id = id
        self.name = name
        self.address = address

class Category(Enum):
    SCIENCE = 0
    TECH = auto()
    ENGLISH = auto()

# data class
class Book:
    def __init__(self, title: str, author: str, category: Category, rack_number: int, publication_date: int):
        self.title = title
        self.author = author
        self.category = category
        self.rack_number = rack_number
        self.pulication_date = publication_date

class BookShelve:
    def __init__(self):
        self.books: List[Book] = []
    
    def search_book_by_title(self, title: str) -> List[Book]:
        return list(filter(lambda x:x.title==title, self.book))

    def search_book_by_subject(self, subject: str) -> List[Book]:
        return list(filter(lambda x:x.subject==subject, self.book))

    def search_book_by_category(self, category: Category) -> List[Book]:
        return list(filter(lambda x:x.category==category, self.book))

    def search_book_by_publication_date(self, publication_date: int) -> List[Book]:
        return list(filter(lambda x:x.publication_date==publication_date, self.book))


def main(argv):
    print('hello world!')


if __name__ == '__main__':
    main(sys.argv[1:])
