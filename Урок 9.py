'''def f(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
f(5,4,10,20,30,one=1,two=2)


def sum(*args):
    print(max(args))

sum(1,2,3,4)'''

#age=21

'''if age>=18:
    print(True)
else:
    print(False)'''

#is_allow = True if age>=18 else False
'''is_allow = age>=18
is_allow=22 if age >= 18 else 21
print(is_allow)'''

'''a=[1,2]
b=[1,2]
c=a
if a is c:
    print(True)
else:
    print(False)'''



'''val = {}
res=[]'''
'''if val is None:
    val= []

val=[] if val is None else print()'''

'''val =val or res
print(val)'''

'''a=100
b=[]
while a!=0:
    a=a//5
    b.append(a)
print(b)'''

'''list1=[]
for x in range(100):
    if x % 5==0:
        list1.append(x)
list1=[i**3 if i >50 else i for i in range(100) if i%5==0]
print(list1)
colors = ["orange",'green',"red","epic"]
a={i:len(i) for i in colors}
print(a)

dict={
    (1,2,3):"Hello"
}
print(dict[(1,2,3)])

tuple = (1,2,3)
print(tuple,type(tuple))
list= list(tuple)
print(list,type(list))'''

'''b=[]
l=[]
for i in range(1,11):
    a=int(input())
    d=a if a%2==0 else l.append(a)
    b.append(a)
print(b)
print(l)'''


a=(5, 3, 2, 1, 4)
list_a=list(a)
list_a=sorted(list_a)
print(tuple(list_a))

#До встречи!







