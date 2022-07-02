#!/bin/env python
import sys
from tracemalloc import start
from typing import Deque, Dict, List
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

class ShippingStatus(Enum):
    Prepare = 1
    Shipping = auto()
    Delivered = auto()

order_id = 0
class Order:
    def __init__(self, status: ShippingStatus, order_date: str, shipping_address: str, product_name_and_count: Dict[str, int]):
        order_id += 1
        self.order_id = order_id
        self.status = status
        self.order_date = order_date
        self.shipping_address = shipping_address
        self.product_name_and_count = product_name_and_count

from collections import deque
# system
class Amazon:
    def __init__(self):
        self._products_by_name: Dict[str, Product] = {}
        self._products_by_category: Dict[Category, List[Product]] = {}
        self._orders: Deque[Order]
        self._delevered_order: Deque[Order]

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

    def buy_product_by_name(self, name: str, user: User, date: str, shipping_address: str):
        if not user.is_member:
            raise Exception(f'user {user} is not member')

        product = self.search_product_by_name(name)
        if not product:
            raise Exception(f'can not search product by name: {name}')

        order = Order(ShippingStatus.Prepare, date, shipping_address, {name: 1})
        self._orders.append(order)
    
    def handler_order(self):
        tmp = deque()
        while self._orders:
            order = self._orders.popleft()
    
            if order.status == ShippingStatus.Prepare:
                for name, count in self.product_name_and_count:
                    # self._products_by_category[]
                    if self._products_by_name[name]._count < count:
                        raise Exception('out of stock!')
                    self._products_by_name[name]._count -= count
            elif order.status == ShippingStatus.Shipping:
                order.status = ShippingStatus.Delivered
                self._delevered_order.append(order)
                continue

            tmp.append(order)
        
        while tmp:
            self._orders.append(tmp.popleft())
        
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
