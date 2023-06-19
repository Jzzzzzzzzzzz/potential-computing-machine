'''class Item:
    def __init__(self,name,price,massa):
        self.name = name
        self.price = price
        self.massa = massa
    def __add__(self, other):
        if isinstance(other,Item):
            return self.price - other.price
        elif isinstance(other,int):
            return  self.price + other.price#

item1 = Item('Iphone',100000,0.3)
item2 = Item("Xiomi",50000,0.4)

print(item1 + item2)
print(item1 + 1000)'''




class Item_2:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price
    def __sub__(self,other):
        return  self.price - other.price
    def __mul__(self, other):
        return self.price * other.price
    def __div__(self,other):
        return self.price / other.price


I1 = Item_2("Tesla",10000000)
I2 = Item_2("Rolex",1000000)

print(I1+I2)
print(I1-I2)
print(I1*I2)
print(I1.__div__(I2))




#Удачи и до встречи!