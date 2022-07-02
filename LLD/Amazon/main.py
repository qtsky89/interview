#!/bin/env python
import sys
from typing import Dict
from enum import Enum
# category
class Category:
    BOOK, CAMERA, COMPUTER = 1, 2, 3

# user
user_id = 0
class User:
    def __init__(self, name, address):
        user_id += 1
        self._id = user_id
        self._name = name
        self._address = address

# product
product_id = 0
class Product:
    def __init__(self, name: str, catetory: Category, seller: User):
        product_id += 1
        self._product_id = product_id
        self._name = name
        self._catetory = catetory
        self._seller = seller

# system
class Amazon:
    def __init__(self):
        self._products_by_name: Dict[str, Product] = {}
        self._products_by_category: Dict[Category, Product] = {}

    def add_new_product_to_sell(self, name: str, category: Category, seller: User):
        new_product = Product(name, category, seller)

        self._products_by_name[name] = new_product
        self._products_by_category[name] = new_product
    
    def search_product_by_name(self, name: str) -> Product:
        if name not in self._products_by_name:
            return None
        
        return self._products_by_name[name]
    
    def search_product_by_category(self, category: Category) -> Product:
        if category not in self._products_by_category:
            return None
        
        return self._products_by_category[category]


def main(argv):
    print('hello world!')


if __name__ == '__main__':
    main(sys.argv[1:])
