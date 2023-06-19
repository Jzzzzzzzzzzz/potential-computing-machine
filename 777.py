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
    print("Проиграл(,попробуй еще, и у тебя обязательно получится!")