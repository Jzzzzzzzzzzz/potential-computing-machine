import random
import time
"""
class RunningCodeJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start =time.time()
        return  self


    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f"time:{t}")
        if exc_type is TypeError:
            return True



with RunningCodeJudge() as t1:
    my_list = [x for x in range (10000000)]
    print(t1)
    my_list-="s"
"""



'''my_list = [1,2,3,4,5]
list_iteration = iter(my_list)
print(next(list_iteration))
'''



class RandomIter:
    def __init__(self,limit=None):#self ссылка на экземпляр
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit = True
        self.limit = self.__reload
        return self#Зачем мы тут self возращаем.Без него ошибка!


    def __next__(self):
        if self.limit == False:
            raise StopIteration

        self.limit+=1
        return  self.limit


rand_iter = list(RandomIter(10))
'''print(rand_iter)
print(rand_iter)'''

for rand in rand_iter:
    print(rand)


'''print("end")
iter(rand_iter)
print(next(rand_iter))'''





'''class MyFile:
    def __init__(self,name,mode,unicode="utf-8"):
        self.name = name
        self.mode = mode
        self.unicode = unicode

    def __enter__(self):

        self.a = open(self.name,self.mode)
        return self.a

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.a.close()


with MyFile("file.txt","w") as f:
    f.write("Win")'''

#До встречи!Удачи и успехов!!!!