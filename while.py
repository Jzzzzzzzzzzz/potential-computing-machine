


'''i=1
while i<=10:
    print(i**2)
    i+=1'''
#123456
'''i = int(input())
leng=0
while i>0:
    i=i//10
    leng+=1
print(leng)'''

'''password=123456
a=3
while a>0:
    a-=1
    user=int(input("введите пароль:"))
    if user==password:
        print("Сейф открыт")
        break
    else:
        print("Не правильный пароль,попыток:",a)
    if a <= 0:
        print("попытки исчерпаны! До самоуничтожения")
        p = 0#a задать не получится,у нас цикл!!! Если задам,будет повтор,и тп
        while p < 5:
            p += 1
            print(p, "сек")

'''
summa=int(input("Сколько вам нужно накопить денег?"))
money=int(input("Сколько денег в день вы откладываете?"))
while summa>0:
    summa=summa/money
    if summa>0:
        print(summa)
        break










