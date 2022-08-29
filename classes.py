from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage, ABC):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                self.__items[name] += count
            else:
                return "Not enough space in the storage"
        else:
            if self.get_free_space() >= count:
                self.__items[name] = count
            else:
                return "Not enough space in the storage"

    def remove(self, name, count):
        if self.__items[name] >= count:
            self.__items[name] -= count

        else:
            return "Not enough goods in the storage"

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __repr__(self):
        goods_in_store = ""
        for key, value in self.__items.items():
            goods_in_store += f"{key}:{value}, "
        return goods_in_store

class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() > 5:
            return "Adds impossible, to many different items at shop"
        else:
            super().add(self, name, count)

    # def __repr__(self):
    #     goods_in_shop = ""
    #     for key, value in self.__items.items():
    #         goods_in_shop += f"{key}:{value}, "
    #     return goods_in_shop



        # if name in self.__items.keys():
        #     if self.get_free_space() >= count:
        #         self.__items[name] += count
        #     else:
        #         return "Not enough space in the storage"
        # else:
        #     if self.get_free_space() >= count:
        #         self.__items[name] = count
        #     else:
        #         return "Not enough space in the storage"




# store_1 = Store(items={"cheese": 10, "milk": 70}, capacity=90)
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

shop_1 = Shop(items={}, capacity=0)

shop_1.add("apple", 5)

print(f"shop_1 {shop_1}\n")
