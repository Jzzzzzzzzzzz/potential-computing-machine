def tabl():
    n = int(input("Таблица умножения до:"))
    a = int(input("Введите число,которое вы бы хотели умножить: "))
    b = 0
    for i in range(n):#пока i в цикле от n до N выполняется i,выполняется:тело цикла
        b += 1
        s=a*b
        print(b, "*", a, "=", s)
tabl()

while True:
    print ("введите 1,если хотите продолжить")
    print("введите 0,если хотите выйти")
    a=int(input("-"))
    if a==1:
       tabl()
    else:
        print("До свидания")
        break
