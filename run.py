from classes import *

print("Hi!")

store_1 = Store(items={"cheese": 10, "milk": 10, "apple": 10})
store_2 = Store(items={"cheese": 10, "milk": 10, "onions": 10})
shop_1 = Shop(items={"cheese": 3, "milk": 3, "apple": 3})


test_text = "Bring 3 cheese from store_1 to shop_1"
req = Request(test_text)
req.move()
print(store_1)
# while True:
#     user_text = input("Your order:\n")
#     if user_text == "stop":
#         break
#     else:
#         req = Request(user_text)
#         req.move()
#


#
# print(store_1.get_free_space())
# print(store_1.get_items())
# print(store_1.get_unique_items_count())
# print(f"store_1 {store_1}\n")
#
# store_1.add("apple", 5)
# print("After add")
#
# print(store_1.get_free_space())
# print(store_1.get_items())
# print(store_1.get_unique_items_count())
# print(f"store_1 {store_1}\n")
#
# store_1.remove("cheese", 10)
# print("After remove")
#
# print(store_1.get_free_space())
# print(store_1.get_items())
# print(store_1.get_unique_items_count())
# print(f"store_1 {store_1}\n")

# shop_1 = Shop(items={"cheese": 2, "milk": 8})
#
# shop_1.add("apple", 2)
# print(shop_1.get_free_space())
# print(shop_1.get_items())
# print(shop_1.get_unique_items_count())
# print(f"shop_1 {shop_1}\n")
# shop_1.add("onions", 4)
# print(shop_1.get_free_space())
# print(shop_1.get_items())
# print(shop_1.get_unique_items_count())
# print(f"In the shop:\n{shop_1}")
# shop_1.add("grapes", 1)
# print(f"In the shop:\n{shop_1}")
# print(shop_1.get_free_space())
# shop_1.add("bananas", 1)
# print(f"In the shop:\n{shop_1}")
# print(shop_1.get_free_space())
# print(shop_1.get_unique_items_count())
