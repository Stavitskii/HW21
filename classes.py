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
                print("Not enough space in the storage")
                return "Not enough space in the storage"
        else:
            if self.get_free_space() >= count:
                self.__items[name] = count

            else:
                print("Not enough space in the storage")
                return "Not enough space in the storage"

    def remove(self, name, count):
        if self.__items[name] >= count:
            self.__items[name] -= count
            print(f"Goods in the store are enough")
        else:
            print("Not enough goods in the storage")
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
            goods_in_store += f"{key}:{value}\n"
        return goods_in_store


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print("Adds impossible, to many different items at the shop")
            return "Adds impossible, to many different items at the shop"
        else:

            super().add(name, count)


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        self.__to = req_list[6]
        self.__from = req_list[4]

    def move(self):
        try:
            eval(self.__from).remove(self.__item, self.__count)
            print(f"A courier took {self.__count} {self.__item} from {self.__from}")
            print(f"A courier is getting {self.__count} {self.__item} from {self.__from} to {self.__to}")
        except:
            print("Something is wrong with the order")
        try:
            eval(self.__to).add(self.__item, self.__count)
            print(f"A courier have taken {self.__count} {self.__item} to {self.__to}")
        except:
            print("Something is wrong with the shop")
        print(self.__from)







