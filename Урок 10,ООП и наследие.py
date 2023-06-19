


'''class Human:
    def __init__(self,name,color_of_hair,height,weight):
        self.name = name
        self.color_of_hair=color_of_hair
        self.height=height
        self.weight=weight
    def say(self):
        print(f"Меня зовут {self.name} и мой рост {self.height} при весе {self.weight}")

Human1 = Human(name="Ivan",color_of_hair="black",height=180,weight=86)
Human2 = Human(name="Dmitri",color_of_hair="black",height=190,weight=90)
Human1.say()
Human2.say()'''




'''class Tank:
    def __init__(self,model,amror,min_damage,max_damage,health):
        self.model=model
        self.amror=amror
        self.damage=random.randint(min_damage,max_damage)
        self.health=health
    def health_down(self,enemy_damage):
        self.health-=enemy_damage
        print(f"{self.model}")
        print(f"По танку попали,осталось {self.health} hp")

    def shot(self,enemy):
        if enemy.health <= 0 or self.damage >= enemy.health:
            enemy.health=0
            print(f"Экипаж танка {enemy.model} уничтожен!")
        else:
            enemy.health_down(self.damage)
            print(f"{self.model}")
            print(f"Есть пробитие,у противника  {enemy.model} осталось {enemy.health} здоровья")

class SuperTank(Tank):
    def __init__(self,model,amror,min_damage,max_damage,health):
        super().__init__(model,amror,min_damage,max_damage,health)
        self.forceAmrore = True

    def health_down(self,enemy_damage):
        super().health_down(enemy_damage/2)


tank1=Tank("T-34",90,10,40,40)
tank2=Tank("Tiger",90,10,30,60)
tank1.shot(tank2)
tank2.shot(tank1)'''


import random
class User:
    def __init__(self,name,hp,min_damage,max_damage):#self ссылка на экземпляр
        self.name=name
        self.hp=hp
        self.damage=random.randint(max_damage,min_damage)
        self.is_alive = True
    def attack(self,enemy_damage):
        self.hp-=enemy_damage
        print(f"{self.name} сделал выстрел,попадание есть!")
        print("-" * 100)
        print(f"{self.name} нанёс {enemy_damage} урона ")
        print("-" * 100)
        if self.hp <= 0:
            self.is_alive = False

    def shot(self,enemy):
        if not enemy.is_alive:#Обращаемся типо к экзкмпляру(Допустим Mag1) etc....
            print(f"Противник {enemy.name} уничтожен!FFFF")
        else:
            enemy.attack(self.damage)
            #print(self.damage) У других увеличен домаг,поэтому показатель тут меньше
            print(f"{self.name}")
            print(f"У противника осталось {enemy.hp} здоровья")#написал self.name
class Mage(User):
    def __init__(self, name, hp, min_damage, max_damage):
        super().__init__(name, hp, min_damage, max_damage)
        self.forceAmrore = True
    def attack(self,enemy_damage):
        super().attack(enemy_damage * 1.2)


class Warrior (User):
    def __init__(self, name, hp, min_damage, max_damage):
        super().__init__(name, hp, min_damage, max_damage)
        self.forceAmrore = True
    def attack(self,enemy_damage):
        super().attack(enemy_damage * 1.5)

class Archer(User):
    def __init__(self, name, hp, min_damage, max_damage):
        super().__init__(name, hp, min_damage, max_damage)
        self.forceAmrore = True
    def attack(self,enemy_damage):
        super().attack(enemy_damage * 2)




pl1=User("1 игрок",100,45,40)
mage1=Mage("Маг",100,50,10)
warrior1=Warrior("Воин",100,35,30)
archer1=Archer("Лучник",100,40,30)



pl1.shot(mage1)
mage1.shot(pl1)
mage1.shot(pl1)
pl1.shot(mage1)

pl1.shot(mage1)
mage1.shot(pl1)
mage1.shot(pl1)
pl1.shot(mage1)
'''warrior1.shot(archer1)
archer1.shot(warrior1)'''
#Всего наилучшего!Пока!))До встречи!




