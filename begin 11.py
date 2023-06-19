#begin 11
import random
a=random.randint(-100000,10000)
b=random.randint(-100000,10000)
print("Модуль первого числа:",abs(a))
print("Модуль второго числа:",abs(b))
print("сумма этих чисел:")
print(f"{abs(a)}+{abs(b)}={abs(a+b)}")
print("произведение этих чисел:")
print(f"{abs(a)}*{abs(b)}={abs(a*b)}")
print("частное модулей этих чисел:")
#(abs) Чтобы перевести любое число в ранг положительных, нужно написать abs(num)
print(f"{abs(a)}/{abs(b)}={abs(a/b)}")