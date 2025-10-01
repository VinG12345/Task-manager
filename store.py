class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # словарь "товар : цена"

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент"""
        self.items[item_name] = price
        print(f"Добавлен товар: {item_name} — {price} руб.")

    def remove_item(self, item_name):
        """Удалить товар из ассортимента"""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удалён из ассортимента.")
        else:
            print(f"Товар {item_name} не найден.")

    def get_price(self, item_name):
        """Получить цену товара по названию"""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновить цену товара"""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена до {new_price} руб.")
        else:
            print(f"Товар {item_name} не найден.")

    def show_items(self):
        """Вывести ассортимент магазина"""
        print(f"\nАссортимент магазина {self.name}:")
        for item, price in self.items.items():
            print(f"- {item}: {price} руб.")


# --- Создание магазинов ---
store1 = Store("Продукты у дома", "ул. Ленина, 10")
store2 = Store("Фруктовый рай", "ул. Садовая, 5")
store3 = Store("ТехноМаркет", "пр. Победы, 20")

# Добавляем товары
store1.add_item("Хлеб", 40)
store1.add_item("Молоко", 60)

store2.add_item("Яблоки", 100)
store2.add_item("Бананы", 120)

store3.add_item("Телефон", 25000)
store3.add_item("Ноутбук", 60000)

# --- Тестирование методов на одном магазине (например, store1) ---
print("\n=== Тестируем магазин:", store1.name, "===")

store1.show_items()

# Добавляем новый товар
store1.add_item("Сок", 80)
store1.show_items()

# Обновляем цену товара
store1.update_price("Хлеб", 45)
store1.show_items()

# Получаем цену товара
print("Цена молока:", store1.get_price("Молоко"))
print("Цена сыра:", store1.get_price("Сыр"))  # товара нет → None

# Удаляем товар
store1.remove_item("Молоко")
store1.show_items()


### 🔹 Что делает программа:
### 1. Создаёт класс `Store` с методами для работы с ассортиментом.
### 2. Создаёт **3 магазина** с разными товарами.
### 3. Тестирует методы **на первом магазине**:
###    - добавление товара,
###    - обновление цены,
###    - запрос цены,
###    - удаление товара.