# Функция input
# Функция input свитывает значения, которые пользователь ввел в консоль(поле ввода) и
# записывает в указаную переменую

# a = input()
# print(type(a))  # -> <class 'str'>
# a + 2  -> Error

# print(int(a) + 10)  # -> a + 10 , перевели тип значения из str в int

# a = int(input()) # <- 20
# print(a)  # -> 20
# print(type(a))  # -> <class 'int'>

# a = int(input())  # <- 20h
# print(a)  # -> Error
# print(type(a))

# a = float(input())  # <- 20.3
# print(a)  # -> 20.3
# print(type(a))  # -> <class 'float'>


# Находим Периметр Треугольник
# Значения a , b , с вводит пользователь в консоли через enter ->
# a
# b
# c

# 1) Первое Решение
# a = float(input("Введите значение а -> "))
# b = float(input("Введите значение b -> "))
# c = float(input("Введите значение с -> "))
# # сщитаем периметр
# perimeter = a + b + c
# print(perimeter)
# print(type(perimeter))  # -> <class 'float'>

# 2) Воторое Решение
# Значения a, b, c вводит пользователь в консоли через пробел ->
# a b c
a, b, c = map(float, input().split())
perimeter = a + b + c
print(perimeter)
print(type(perimeter))  # -> <class 'float'>
