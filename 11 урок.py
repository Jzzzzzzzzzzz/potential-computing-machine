from datetime import  datetime

'''print(type(1),id(1))
print(id(len),type(id))
print(type(input))'''



'''class A:
    def public(self):
        return 40
    def _protected(self):
        return True

    def _private(self):
        return "test"

    def wrappep_protected(self):
        return self._protected()

a=A()
print(a.public())
print(a.wrappep_protected())
print(a._private())'''



'''class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,"instance"):

            cls.instance=super(Singleton,cls).__new__(cls)
        return cls.instance

s=Singleton()
print(s,id(s))
s1=Singleton()
print(s,id(s))


def repair_deco(func):
    def wrapper(a,b):
        return func(a,b)-1
    return wrapper

@repair_deco
def wrong_func(a,b):
    return  a+b+1
print(f"2+2={wrong_func(2,2)}")'''


def time(func):
    def wrapper(val):
        start=datetime.now()
        res=func(val)
        end=datetime.now()
        print(f"time {end-start}")
        return  res

    return wrapper

@time
def get_list1(val):
    return [x for x in range (val+1) if x%2]


@time
def get_list2(val):
    new_list=[]
    for x in range(val):
        if x%2:
            new_list.append(x)
    return  new_list

val=1
l1=get_list1(val)
l2=get_list2(val)
N=datetime.now()








