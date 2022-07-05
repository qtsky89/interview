#!/bin/env python
from collections import defaultdict
import sys
from enum import Enum, auto
from typing import List, DefaultDict, Dict

# data class
class User:
    def __init__(self, id: str, name: str, address: str):
        self.id = id
        self.name = name
        self.address = address
        self.checkout_count: int = 0
        self.fine: int = 0 

class Category(Enum):
    SCIENCE = 0
    TECH = auto()
    ENGLISH = auto()

# data class
book_id = 0
class Book:
    def __init__(self, title: str, author: str, category: Category, rack_number: int, publication_date: int, count: int):
        book_id += 1
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.rack_number = rack_number
        self.pulication_date = publication_date
        self.count = count

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

class CheckoutInfo:
    def __init__(self, book: Book, date: int):
        self.book = book
        self.date = int


class CheckoutSystem:
    def __init__(self):
        self.checkoutinfos: DefaultDict[User:List[CheckoutInfo]] = defaultdict()
        
    def checkout_book(self, user: User, book: Book):
        if user.checkout_count > 5:
            raise Exception(f'user {user} checkout count is larget than 5')
        elif book.count == 0:
            raise Exception('book is not available')

        book.count -= 1
        user.checkout_count += 1
        self.checkoutinfos[user].append(book)
    
    # run once a day
    def put_fine(self):
        current_date = curret_date()
        for user in self.checkoutinfos:
            if self.checkoutinfos[user] + 1000 < current_date:
                user.fine += 10
            
class ReserveSystem:
    def __init__(self):
        self.reserve_user_book: Dict[User, Book] = {}
        self.reserve_book_user: Dict[Book, User] = {}
    
    def reserve_book(self, user: User, book: Book):
        if book.count != 0:
            raise Exception('book count is not zero. checkout instead')
    
        self.reserve_user_book[user] = book
        self.reserve_book_user[book] = user


def main(argv):
    print('hello world!')


if __name__ == '__main__':
    main(sys.argv[1:])
