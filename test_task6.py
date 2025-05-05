from sympy import product
from itertools import product
import time
from functools import wraps

class Product():
    def __init__(self, name, price, min_age, max_age):
        self.name = name
        self.price = price
        self.min_age = min_age
        self.max_age = max_age

    def display_info(self):
        print(f'Название: {self.name}')
        print(f'Цена: {self.price}')
        print(f"Возраст: от {self.min_age} до {self.max_age} лет")

    def is_suitable_for_age(self, age):
        return self.min_age <= age <= self.max_age
    
class Toy(Product):
    def __init__(self, name, price, manufacturer, material, min_age, max_age):
        super().__init__(name, price, min_age, max_age)
        self.manufacturer = manufacturer
        self.material = material

    def display_info(self):
        print("\n=== Игрушка ===")
        super().display_info()
        print(f"Производитель: {self.manufacturer}")
        print(f"Материал: {self.material}")

class Book(Product):
    def __init__(self, name, author, price, publisher, min_age, max_age):
        super().__init__(name, price, min_age, max_age)
        self.author = author
        self.publisher = publisher

    def display_info(self):
        print("\n=== Книга ===")
        super().display_info()
        print(f"Автор: {self.author}")
        print(f"Издательство: {self.publisher}")

class SportsEquipment(Product):
    def __init__(self, name, price, manufacturer, min_age, max_age):
        super().__init__(name, price, min_age, max_age)
        self.manufacturer = manufacturer

    def display_info(self):
        print("\n=== Спорт инвентарь ===")
        super().display_info()
        print(f"Производитель: {self.manufacturer}")

def logger(func):
    """Декоратор для логирования вызовов функций и времени выполнения"""
    @wraps(func) # Здесь сохраняются метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\nВызов функции {func.__name__} с аргументами:")
        print(f"Позиционные: {args}")
        print(f"Именованные: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            
            print(f"Функция {func.__name__} выполнена успешно за {end_time - start_time:.4f} сек")
            print(f"Результат: {result}")
            
            return result
        except Exception as e:
            end_time = time.time()
            print(f"Ошибка в функции {func.__name__}: {type(e).__name__} - {str(e)}")
            print(f"Время выполнения до ошибки: {end_time - start_time:.4f} сек")
            raise
    
    return wrapper

@logger
def create_products():
    products = [
        Toy("Конструктор Lego", 2499, "Lego Group", "пластик", 6, 12),
        Toy("Кукла Barbie", 1599, "Mattel", "пластик", 3, 10),
        Book("Гарри Поттер", "Дж.К. Роулинг", 899, "Росмэн", 12, 18),
        Book("Маленький принц", "А. де Сент-Экзюпери", 499, "Эксмо", 6, 99),
        SportsEquipment("Футбольный мяч", 1999, "Nike", 8, 99),
        SportsEquipment("Велосипед", 15999, "Stels", 5, 14),
    ]
    return products
 
@logger
def display_all_products(products):
    print("\n=== Все товары ===")
    for product in products:
        product.display_info()

@logger
def find_products_by_age(products, age):
    print(f"\n=== Товары для возраста {age} лет ===")
    suitable_products = [p for p in products if p.is_suitable_for_age(age)]
    
    if not suitable_products:
        print("Товары для указанного возраста не найдены")
    else:
        for product in suitable_products:
            product.display_info()

@logger
def find_products_in_age_range(products, min_age, max_age):
    print(f"\n=== Товары для возраста от {min_age} до {max_age} лет ===")
    suitable_products = [
        p for p in products 
        if p.max_age >= min_age and p.min_age <= max_age
    ]
    
    if not suitable_products:
        print("Товары для указанного возрастного диапазона не найдены")
    else:
        for product in suitable_products:
            product.display_info()

@logger
def exercise1():
    n = 506
    sp1 = []
    # Разбираем маску "1?*157?4":
    # 1 - первая цифра
    # ? - вторая цифра (любая от 0 до 9)
    # * - любое количество цифр (включая 0)
    # 157 - фиксированная часть
    # ? - предпоследняя цифра (любая)
    # 4 - последняя цифра

    # Генерируем возможные числа:
    # Формат: 1 + [0-9] + * + 157 + [0-9] + 4
    min_len = 6
    max_len = 9
    print('Работа начата')
    for length in range(min_len, max_len + 1):
        # Количество символов между 1? и 157?4: length - 6 (так как 1?157?4 уже 6 символов)
        for middle_len in range(0, length-5):
            # Общая длина: 1 (1) + 1 (?) + middle_len + 3 (157) + 1 (?) + 1 (4) = 6 + middle_len
            # Проверяем, что общая длина == length
            if 6 + middle_len != length:
                continue
        # Генерируем все возможные варианты:
        # Вторая цифра (?) - любая от 0 до 9
        for d1 in range(10):
            # Средняя часть (*) - любая последовательность длины middle_len
            for middle in product('0123456789', repeat=middle_len):
                # Предпоследняя цифра (?) - любая от 0 до 9
                for d2 in range(10):
                    middle_str = ''.join(middle)
                    num_str = f'1{d1}{middle_str}157{d2}4'
                    num = int(num_str)
                    if num > 10**9:
                        continue
                    if num % n == 0:
                        sp1.append(num//n)
    return(sorted(sp1))

@logger
def f1(x):
    return (x**2 + 3*x + 2) / (x - 5)

@logger
def f2(x,y):
    return x + y * z

@logger
def f3(s):
    return len(s)

@logger
def f4(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    
    avg_even = sum(even) / len(even) if even else 0
    avg_odd = sum(odd) / len(odd) if odd else 0
    
    if avg_even > avg_odd:
        return "Среднее четных больше"
    elif avg_odd > avg_even:
        return "Среднее нечетных больше"
    else:
        return "Средние равны"

@logger
def f5(x):
    if x > 0:
        return "Положительное"
    else:
        return "Отрицательное"

