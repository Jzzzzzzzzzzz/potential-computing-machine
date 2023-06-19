'''a=int(input())
b=int(input())
def add (a,b):
    s = a + b
    return s
print(add(a,b))'''

'''N = 0
N = int(input("Введите число:"))
def summa_n (N):
    p=1
    for i in range(1, N):
        N+=-1
        p+=1
        N = N + p
    return N
print(f"Я знаю, что сумма чисел от 1","до",N ,"=",summa_n(N))'''



'''def greeting ():
    b = print('Привет!')
    a = print('Добро пожаловать!')
    return b, a
for i in range(5):
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
        print('Следующий.\n')'''




def umn(a,b,c):
    u = a * b
    d=a/b
    v=a-b
    p=a+b
    if c=="*":
        return u
    elif c=="/":
        return d
    elif c=="+":
        return p
    else:
        return v
m=int(input("Сколько раз вы будете использовать калькулятор,напишите 5,сможете сделать вычисление 5 раз(и тп):"))
for i in range(m):
    a = int(input("Напишите 1-ое число:"))
    b = int(input("2-ое число:"))
    c = input("что нужно сделать?:(/;*;+;-):")
    print(umn(a,b,c))
txt=open("answer.txt","a")
txt.write(str(umn(a,b,c)))
txt.close()

#почему-то в блокноте выводится "none",пробовал функцию задавать в переменную,результаты лучше не стали,help)

