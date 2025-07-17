class Store:
    def __init__(self, name, address, items:dict):
        self.name = name
        self.address = address
        self.items = items 
   
    def add_goods(self, goods_name, price):
        if goods_name in self.items:
            print(f"Товар {goods_name} уже есть")
        else:            
            self.items[goods_name] = price
        # Если без if/else, то в словарь self.items
        # по ключу goods_name положить значение price.
        # Если такого ключа не было — он бы создался.
        # Если уже был — его значение обновилось бы.
    
    def delete_goods(self, goods_name):
        if goods_name in self.items:
            del self.items[goods_name]
        # полностью удаляет пару значение-ключ 
        else:
            print("Такой товар не обнаружен")           
    
    def goods_price(self, goods_name):
        return self.items.get(goods_name, None)
        # возвращает цену товара по названию
        # если товара нет --None
   
    def update_price(self, goods_name, new_price):
        if goods_name in self.items:
            self.items[goods_name] = new_price
        else:
             print("Такой товар не обнаружен")
    
    def __str__(self):
        return (f"""Магазин: {self.name}, 
                Адрес: {self.address}, 
                Товары: {self.items}""")
    # тройные кавычки - многострочная f-строка
store1 = Store(("Продукты у дома", "ул. Ленина, 1",
         {"Хлеб": 40, "Молоко": 60}))
store2 = Store(("Техника+", "пр. Мира, 10", 
         {"Смартфон": 25000, "Наушники": 3000}))
store3 = Store(("Книжный мир", "ул. Пушкина, 5",
         {"Гарри Поттер": 800, "Война и мир": 1200}))

# Выводим инфо о магазине и товарах
print(store1)

# Добавляем товар
store1.add_goods("Сахар", 55)
print(store1)

# Пытаемся добавить уже существующий товар
# Должно выдать предупреждение
store1.add_goods("Хлеб", 45)  
# Обновляем цену товара
store1.update_price("Молоко", 65)
print(store1)

# Обновляем цену несуществующего товара
# Должно выдать предупреждение
store1.update_price("Мясо", 350)  

# Удаляем товар
store1.delete_goods("Хлеб")
print(store1)
# Удаляем несуществующий товар
# Должно выдать предупреждение
store1.delete_goods("Соль")  

# Запрашиваем цену товара (существующего)
price = store1.goods_price("Сахар")
print(f"Цена на Сахар: {price}")
# Запрашиваем цену несуществующего товара
price = store1.goods_price("Соль")
print(f"Цена на Соль: {price}")  
# Должно вывести None

