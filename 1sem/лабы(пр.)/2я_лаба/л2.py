dash="----------------------------------------------"
print(dash)
#задача 1
def greet(name):
    print(f"Привет, {name}!")
def square(number):
    print(f"Квадрат числа: {number**2}")
def max_of_two(x, y):
    print(f"Максимальное число: {max(x, y)}")

#Задача 2
def describe(name, age=30):
    print(f"Вас зовут {name} и вам {age}")

#Задача 3
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num // 2):
            if (num % i) == 0:
                return False
        return True
#---------------------------------------------------------------------------------------
greet(str(input("Введите имя: ")))
square(float(input("Введите число (для возведения в кадрат): ")))
max_of_two(float(input("Введите первое число: ")), float(input("Введите второе число: ")))
print(dash)

describe(str(input("Введите имя: ")), int(input("Введите возраст: ")))
print(dash)

print(is_prime(int(input('Введите число:'))))
print(dash)