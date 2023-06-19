'''def calculator():
    a=float(input("1 число:"))
    b=float(input("2 число:"))
    viachesl=input("Что нужно сделать?:")
    opers=["+","-","*","/","**","//","%"]
    while viachesl not in opers:
        viachesl = input("Введите операцию(/,*,+,-,//,%,**):")
    if viachesl == "+":
        print(a + b)
    elif viachesl == "-":
        print(a - b)
    elif viachesl == "/":
        if b == 0:  # разветление идет,поэтому такие пироги)
            print("на ноль делить нельзя!!!")
        else:
            print(a / b)
    elif viachesl == "*":
        print(a * b)
    elif viachesl =="**":
        print(a**b)
    elif viachesl == "//":
        print(a // b)
    elif viachesl == "%":
        print(a % b)
while True:
    try:
        count = int(input("Сколько раз вы хотите произвести вычесление?:"))
    except ValueError:
        print("До свидания!")
    else:
        for i in range(count):
            print(f"вычисление № {i + 1}")
            calculator()
            print("_-------------------____-------____-------------_----------___________-")
'''

def func(a, b, c):
    D = (b ** 2) - (4 * a * c)
    return D
while True:
    try:
        a = int(input("1 значение:"))
        b = int(input("2 значение:"))
        c = int(input("3 значение:"))
    except ValueError:
        pass
    else:
        print(f"дискриминант равен:{func(a, b, c)}")
        break







'''import math
print("Квадратнрый корень числа~(даже не целого)")
X=float(input("Введите это число:"))
operation_with_X=math.sqrt(X)
print(operation_with_X)'''
'''До встречи и удачи!I love programming languages and know them best!!!! I am a genius in every field!)'''







