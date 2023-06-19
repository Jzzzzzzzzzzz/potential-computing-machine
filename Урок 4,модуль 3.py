import time
import contextlib

import sys
import course

#my_iter = [time.sleep(x) for x in range(1,3)]

'''my_iter = (time.sleep(x) for x in range(1,3))#.обращаемся
print(my_iter)

for elem in my_iter:
    print(elem)


my_range=range(1,11)
print(type(my_range))
print(list(my_range))'''

'''def my_lazy_func():
    for i in  range(1,11):
        print(f"До {i}")
        yield i
        print(f"После {i}")


for i in my_lazy_func():
    print(i)


gen=my_lazy_func()
next(gen)'''

'''file = open("file.txt","w")
file.write("Hey")
file.close()

with open("file.txt","w") as f:
    f.write("hello")'''
'''
@contextlib.contextmanager
def str_reverse(my_str):
    print("Входим в контекстный менеджер")
    yield  my_str[::-1]
    print("Выходиммм из контекстного менеджера")


with str_reverse("hello") as reversed_str:#результат func
    print(reversed_str)'''

@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        print("Произиошло исключение")
with exc_handler(IndexError):
    my_l=[1,2]
    print(my_l[5])


"""
def func_args_kwargs(*args,**kwargs):
    print(f"Args:{args} kwargs:{kwargs}")
func_args_kwargs(1,2,3,b=3,c=4)"""


#Доступен для просмтора:Доллар(R01235),Евро(R01239),Фунт,Стерлинги Соединненого Королевства(R01035).(name не парсится)
@contextlib.contextmanager
def valute(id):
    try:
        #print("До")
        response = course.get_valute(id)
        #print("До2")
        yield response
        #print("После")
    except  Exception :
        yield ("Такая валюта не найдена!")

with valute("R01231") as VALUTE:
    print(VALUTE)





'''
def generation():
    for i in range(1000000):
        yield i**2

def examination(inlet=None):
    T1 = (time.strftime("%S"))
    T1 = float(T1.replace(",","."))
    print(T1)
    print(inlet)
    T2 = (time.strftime("%S"))
    T2 = float(T2.replace(",", "."))
    print(T2)
    return (f"{T1-T2} секунд"),(f"{sys.getsizeof(inlet)} байт")


print(examination(generation()))

generation_2 =(i**2 for i in range(1000000))
print(examination(generation_2))

list=[i**2 for i in range(10)#тут просто поставить 1000000,но я вам не советую
print(examination(list))'''


#До встречи,удачи!!!!)!!!!









