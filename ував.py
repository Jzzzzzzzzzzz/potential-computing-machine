'''class A:
    def __init__(self,name = None,age = 27):
        self.name = name
        self.age = age
    def plus_odin_god(self):
        self.age+=1
        return (f"{self.name} {self.age} лет,было ему {self.age-1} лет ")



def plus_odin_god(age):
    age+=1
    return (f" {age}")
#print(plus_odin_god.__call__(20))


#a=A("Dmitriy")
#print(a.plus_odin_god())#тут как обычно просто определён экземпляр класса,и всё ок
#print(A.plus_odin_god)#1.Почему если я сделаю plus_odin_god() со скобками мне выдаст ошибку. 2.Почему мне выводит(если без скобок соответсвенно)-<function A.plus_odin_god at 0x00000269F0A49EA0>.
# 3.Почему я не могу сделать A.name и тп(тоесть обратиться к атрибутам)4.Почему я не могу использовать сам класс как объект?Спасибо!


#a = str(Apple)#Почему я не могу сделать так с строчкой? С числами могу допустим - a = str(10)

name_of_company = ["Apple","Xiaomi","Xiaomi","Xiaomi","Apple","Apple","Samsung"]

for i in name_of_company:
    if i =="Apple" or i == "Samsung":
        pass
        #print(i)



def test_1(a):
    if a>=0:
        True
    if a==True:
        return True


a=int(input(":"))
def test_2(a):
    if a >= 0:
        b=True
    if b == True:
        return True

print(test_2(a))

print(test_1(1))






class User:
    def __init__(self,name):
        self.name = name




tuple_ = (1,2,3,)
print(tuple(tuple_))'''


slovary = {1:"a",2:"b",3:"v",}
print(slovary[1])

#for i in "assff":
 #   slovary[i] = slovary.get(i,0)+1
  #  print(slovary)



#До встречи!Удачи!!

