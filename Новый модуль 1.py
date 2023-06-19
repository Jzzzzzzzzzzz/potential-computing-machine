'''name=input("name:")
salary=int(input("salary/mounth:"))'''



'''emloyee={
    "name":"Ivan",
    "salary":200000,
    "age":20,
}


print(f"Cash of 1 year {emloyee['salary']*12} dollars")'''


emloyees_list=[
    {
        "name":"Ivan",
        "salary":100000000,
        "age":20,
    },
    {
        "name":"Iv",
        "salary":20000000000,
        "age":30,
    },
    {
        "name":"Iva",
        "salary":30000000000,
        "age":25,
    }
]
#for i in emloyees_list:
   # print(f"{i['name']} cash of 1 year-{i['salary']}")
'''for i in emloyees_list:
    if i["name"]=="Ivan":
        emloyees_list.remove(i)
        break
#print(emloyees_list)

nem_empoyees={
    "name":"Dima",
    "salary":2000000,
    "age":21
}
emloyees_list.append(nem_empoyees)
#print(emloyees_list)
#print(emloyees_list[0])'''



class Employee:
    def __init__(self,name="IvanАРГУМЕНТ",salary=10000000000000,on_vacation=True,is_good_employee=True): #Я по стандарту сделал True      #сначала объявить аргумент,потом писать ...
        self.name=name
        self.salary=salary
        self.on_vacation=on_vacation
        self.is_good_employee=is_good_employee
    def get_info(self):
        print(f"Cash of 1 year{self.salary*12} name-{self.name}")
        if self.on_vacation==False:
            print("В отпуске")
        else:
            print("На рабочей смене")#Пусть False в отпуске,а True на работе
        if self.is_good_employee==False:
            print()
            print(f"Я тебя предупреждал!!!!Всё,ты уволен!{self.name}")
            print()





employees=[
    Employee("Sasha",10000000),
    Employee("Dima",20000000),
    Employee("Maksim",30000000),
    Employee("Egor",40000000),
    Employee("Shrek",50000000,False,False)

]

for i in employees:
    i.get_info()
    if i.is_good_employee==False:
        employees.remove(i)



#До встречи!Всего наилучшего,удачи!!!!)!!!!