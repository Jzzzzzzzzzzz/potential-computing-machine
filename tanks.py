import random
class Tank:
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
        super().__init__(self,model,amror,min_damage,max_damage,health)

        self.forceAmrore = True

    def health_down(self,enemy_damage):
        super().health_down(enemy_damage/2)








tank1=Tank("T-34",90,10,40,40)
tank2=Tank("Tiger",90,10,30,60)

tank1.shot(tank2)
tank2.shot(tank1)