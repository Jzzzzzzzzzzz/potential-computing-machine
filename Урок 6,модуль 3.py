'''class Year:
    def __init__(self,days,season):
        self.__days = days
        self.__season = season
    @property
    def get_days(self):
        return self.__days
    @get_days.setter
    def get_days(self,days):
        if days==365 or days==366:
            self.__days = days
        else:
            raise Exception("False")
    @property
    def season(self):
        return self.__season
    @season.setter
    def season(self,season):
        a=["Зима","Осень","Лето","Весна"]
        if season in a:
            self.__season = season
        else:
            raise Exception("Такого время года не существует!")
year = Year(365,"Зима")
year.get_days = 366
print(year.get_days)
year.season = "Осень"
print(year.season)'''



class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age <= 0 :
            raise ValueError("ErrorrrrrrrrrrrrrfffffFFFFFPressssFFFF")
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

person = Person("Дмитрий",19)
print(person.name)
person_ = Person("None",False)
print(person_.age)
del person_.name
del person_.age
person_.name = "Марк Цукерберг"
person_.age = 38
print(f"{person.name}(-у,-e,-ю) {person.age} лет")
print(f"{person_.name}(-у,-e,-ю) {person_.age} лет")









#Успехов и удачи!!!!








