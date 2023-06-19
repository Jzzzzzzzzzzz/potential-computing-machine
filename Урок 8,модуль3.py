from pprint import pprint



l = [
    {
        "name" : "Apple",
        "brand" : "Apple",
        "price" : 1200
    },
    {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 500,
},
    {
        'name': 'REALME C25s',
        'brand': 'REALME',
        'price': 400,
    }

]


#def item_price(item):
  #  return item["price"]

#pprint(sorted(l,key=lambda item:item["price"] ))

def testFunction(item):
    return item["brand"] =="Apple"

apple_list = filter(lambda item:item["brand"] =="Apple",l)

print(list(apple_list))

number_list = ["1","2","3","4"]

number_list = map(int,number_list)
print(int)

print(list(number_list))

names_list = ["Кирилл","Дмитрий","Николай","Александр","Кирилл"]

surnames_list = ["Иванов","Петров","Данилов","Александров"]

full_names_list = map(lambda name,surname: f"{name} {surname}",names_list,surnames_list)

print(list(full_names_list))

#print(len(l))

#for i in range(len(l)):
    #print(f"{i}) {l[i]}")

#for i,item in enumerate(l):
    #print(f"{i}),{item}")

patronomic_list = ["Данилович","Никитович","Иванович"]
for name,surname,patronomic in zip(names_list,surnames_list,patronomic_list):
    print (name,surname,patronomic)



class Item:
    def __init__(self,price=None,brand=None):
        self.price = price
        self.brand = brand
    def __repr__(self):
        return self.brand


item_list = [
    Item(999,"Apple"),
    Item(1200, "Apple"),
    Item(777,"Samsung")
]


result = list(filter(lambda b:b.brand =="Apple",item_list))
print(result)
price_list = [i.price for i in item_list]
print(price_list)
map_=map(lambda resu,price:f"{resu} {price}",price_list,result)
print(list(map_))


dict={}

for i in item_list:
    print(i.price)


names_list = ['кирилл','данил','кирилл','кирилл', 'артём', 'никита', 'влад',]

a = map(lambda a:a.capitalize(),names_list)
print(list(a))

#Удачи!До встречи!!