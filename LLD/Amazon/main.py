#!/bin/env python
import sys
from tracemalloc import start
from typing import Dict, List
from enum import Enum, auto
# category
class Category(Enum):
    BOOK = 1
    CAMERA = auto()
    COMPUTER = auto()

# user
user_id = 0
class User:
    def __init__(self, name: str, address: str, is_member: bool):
        user_id += 1
        self._id = user_id
        self._name = name
        self._address = address
        self._is_member = is_member
        self._shoppingcart: Dict[str, int] = {}
    
    def is_member(self) -> bool:
        return self._is_member

    def add_product_shopping_cart(self, product_name: str, count: int):
        if product_name in self._shoppingcart:
            raise Exception(f'product name: {product_name} is already in shopping cart')
        self._shoppingcart[product_name] = count
    
    def remove_product_shopping_cart(self, product_name: str):
        if product_name not in self._shoppingcart:
            raise Exception(f'product name: {product_name} not in shoppingcart')
        
        del self._shoppingcart[product_name]
    
    def modify_product_shopping_cart(self, product_name, count):
        if product_name not in self._shoppingcart:
            raise Exception(f'product name: {product_name} not in shoppingcart')
        self._shoppingcart[product_name] = count

class Review:
    def __init__(self, stars: int, msg: str):
        self.stars = start # 1,2,3,4,5
        self.msg = msg

# product
product_id = 0
class Product:
    def __init__(self, name: str, catetory: Category, seller: User, count: int):
        product_id += 1
        self._product_id = product_id
        self._name = name
        self._catetory = catetory
        self._seller = seller
        self._count = count
        self._reviews: Dict[str, Review]  # key: user name, value: Review
    
    def decrease_count(self, count: int):
        if self._count - count < 0:
            raise Exception("count can't not be minus")
        
        self._count -= count
    
    def add_review(self, user_name: str, review: Review):
        self._reviews[user_name] = review

# system
class Amazon:
    def __init__(self):
        self._products_by_name: Dict[str, Product] = {}
        self._products_by_category: Dict[Category, List[Product]] = {}

    def add_new_product_to_sell(self, new_product: Product):
        self._products_by_name[new_product._name] = new_product
        self._products_by_category[new_product._catetory] = new_product
    
    def search_product_by_name(self, name: str) -> Product:
        if name not in self._products_by_name:
            return None
        
        return self._products_by_name[name]
    
    def search_product_by_category(self, category: Category) -> List[Product]:
        if category not in self._products_by_category:
            return None
        
        return self._products_by_category[category]

    def buy_product_by_name(self, name: str, user: User):
        if not user.is_member:
            raise Exception(f'user {user} is not member')

        product = self.search_product_by_name(name)
        if not product:
            raise Exception(f'can not search product by name: {name}')

        product.decrease_count(1)

    def buy_items_in_shopping_cart(self, user: User):
        if not user.is_member():
            raise Exception(f'user {user} is not member')
        
        for product_name in user._shoppingcart:
            self.buy_product_by_name(product_name, user)
        
    def add_review(self, product_name: str, user: User, review: Review):
        product = self.search_product_by_name(product_name)
        product.add_review(user._name, review)
        

def main(argv):
    print('hello world!')


if __name__ == '__main__':
    main(sys.argv[1:])
