import random

'''animals=['cat','dog']
call=["чудесный","прекрасный"]
a=call+animals
for an in animals:
    print(random.choice (animals), end='')
    print(random.choice(call))'''
import random
print("Сейчас вам надо будет ввести сначала 3 названия животных---")
print(" ------------------Затем 3 описания")
animal1 =(input('Введи название животного:'))
animal2=(input('Введи название животного:'))
animal3=(input('Введи название животного:'))
call1=(input('Введи описание:'))
call2=(input('Введи описание:'))
call3=(input('Введи описание:'))
animals=[animal1,animal2,animal3]
calls=[call1,call2]
all=animals+calls
for an in animals:
    print(random.choice(animals),end="-")
    print((random.choice(calls)))

















