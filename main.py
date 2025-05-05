from test_task6 import *
import unittest

class TestFunctions(unittest.TestCase):
    
    # Тесты для функции f4()
    def test_f4_even_greater(self):
        self.assertEqual(f4([2, 4, 1, 3]), "Среднее четных больше")
    
    def test_f4_odd_greater(self):
        self.assertEqual(f4([1, 3, 2, 4, 5]), "Среднее нечетных больше")
    
    def test_f4_equal(self):
        self.assertEqual(f4([2, 1, 3, 4]), "Средние равны")
    
    def test_f4_empty(self):
        self.assertEqual(f4([]), "Средние равны")  # Оба списка пустые
    
    # Тесты для функции f5() (с выявлением ошибки)
    def test_f5_positive(self):
        self.assertEqual(f5(10), "Положительное")
    
    def test_f5_negative(self):
        self.assertEqual(f5(-5), "Отрицательное")
    
    def test_f5_zero(self):
        # Этот тест выявит логическую ошибку
        self.assertEqual(f5(0), "Отрицательное")  # Ожидается специальная обработка 0
    
    def test_f5_float_positive(self):
        self.assertEqual(f5(3.14), "Положительное")
    
    def test_f5_float_negative(self):
        self.assertEqual(f5(-2.71), "Отрицательное")

if __name__ == '__main__':
    print('Выполнил Михель Д.В. ст.гр. ИВТ-223. Вариант 14.')
    while True:
        print("1. Каталог товаров")
        print("2. Поиск всех натуральных чисел для варианта 14. Маска числа = 1?*157?4. n = 506")
        print("3. Проверка функций от f1() до f5()")
        print("4. Unittest. Тестирование функций f4() и f5()")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
    
        if cmd == "1":
            products = create_products()
            # Вывод всех товаров
            display_all_products(products)
            # Поиск товаров для конкретного возраста
            find_products_by_age(products, 10)
            # Поиск товаров в возрастном диапазоне
            find_products_in_age_range(products, 3, 6)

        elif cmd == "2":
            print(exercise1())
        elif cmd == '3':
            try:
                f1(5)
            except ZeroDivisionError:
                print('f1(5): Произошло деление на ноль')
                print(f"Пример правильного вычисления при x=6: {(6**2 + 3*6 + 2) / (6 - 5)}")
                try:
                    f1(int(input('Введите число ')))
                except TypeError:
                    print("\nИсключение в f1(): TypeError - неверный тип данных")
                    print("Рекомендация: Введите числовое значение для x")

            try:
                f2(2,3)
            except NameError:
                print('f2(2,3): Ошибка - переменная z не определена')
                print("Рекомендация: Добавьте определение переменной z в функцию")
            except TypeError:
                print("\nИсключение в f2(): TypeError - неверный тип данных")
                print("Рекомендация: Убедитесь, что x и y - числа")

            try:
                f3('Hello')
            except TypeError:
                print("\nИсключение в f3(): TypeError - ожидалась строка")
                print("Рекомендация: Передайте строковый аргумент в функцию")
    
            sp1 = exercise1()
            f4(sp1)
            f5(0)
        elif cmd == "4":
            unittest.main()
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")