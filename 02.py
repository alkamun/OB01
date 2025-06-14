class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add(self, name, price):
        if not name:
            return
        elif name not in self.items:
            self.items[name] = price
        else:
            print(f"Товар {name} уже есть в списке")

    def remove(self, name):
        return self.items.pop(name, None)

    def get_price(self, name):
        return self.items.get(name, None)

    def set_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price

    def print_list(self):
        print(f"Ассортимент магазина {self.name}, {self.address}")
        print(self.items)
        print()

store1 = Store("Магнит", "г. Москва")
store2 = Store("Пятёрка", "г. Казань")
store3 = Store("Универсам", "г. Оренбург")

store1.add("Яблоки", 160)
store1.add("Груши", 250)
store1.add("Картошка", 99)
store1.set_price("Яблоки", 180)
store1.remove("Груши")
print(f"Цена картошки в {store1.name} - {store1.get_price("Картошка")}")

store2.add("Яблоки", 130)
store2.add("Груши", 230)

store3.add("Яблоки", 180)
store3.add("Груши", 220)

store1.print_list()
store2.print_list()
store3.print_list()
