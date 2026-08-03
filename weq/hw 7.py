###13.1
# import codecs
# import re
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         text = file.read()
#
#     text = re.sub('<.*?>', '', text)
#
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(text)
###13.2
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}"
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# class Purchase:
#
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         text = f"User: {self.user}\nItems:\n"
#         for item, cnt in self.products.items():
#             text += f"{item.name}: {cnt} pcs.\n"
#         return text
#
#     def get_total(self):
#         total = 0
#         for item, cnt in self.products.items():
#             total += item.price * cnt
#         return total
#
#
# lemon = Item('lemon', 5, "yellow", "small")
# apple = Item('apple', 2, "red", "middle")
#
# print(lemon)
#
# buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
#
# assert isinstance(cart.user, User) is True
# assert cart.get_total() == 60
# assert cart.get_total() == 60
#
# cart.add_item(apple, 10)
# print(cart)
#
# assert cart.get_total() == 40