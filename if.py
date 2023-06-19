'''rating=int(input("РЕЙТИНГ ФИЛЬМА???:"))
a=input("Запиши актера:")
if a=="Леонардо Ди Каприо" and rating>=int7:
    print("Красава")
elif a=="Том Холланд" or "Tom"
    print('Впринципе норм')
else:
    print("Сочувствую")


import random
win=False
for i in range(5):
    b = int(input())
    a = random.randint(0, 10)
    diff = a - b
    print(a)
    if a == b:
        print("Молодец!")
        win=True
        break
    elif diff == 1 or -1:
        print("Почти!!")
    else:
        print("Не получилось(")
if win==False:
    print('Проигрышь')




a=int(input('Введите кол-во градусов:'))
if a>=30:
    print("Очень Жарко")
elif a>=25:
    print("Жарко")
elif a>=15:
    print("Тепло")
elif a>=5:
    print('Прохладно')
elif a>=-5:
    print("Холодно")
elif a>=-15:
    print('Очень холодно')

x=[]
n=int(input("Сколько цифр??:"))
if n>2:
    for i in range(n):
        b=int(input( f" {i+1} число:"))
        x.append(b)
        x=(sorted(x))
        print(x)
else:
    print("Должно быть больше 2-х числел")# я так решил сделать,надеюсь вы засчитаете

import random
a=input('Орел или решка:')
w=['Орел','Решка']
b=random.choice(w)
if a==b:
    print("Ты выиграл",",это-",b,sep='')
else:
    print("Ты проиграл")
'''





