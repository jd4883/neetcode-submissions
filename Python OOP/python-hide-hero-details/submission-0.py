class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    def get_health(self):
        return self.__health

    def get_power_level(self):
        return self.__power_level
    
    def set_health(self, health):
        if health > 100:
            print("You can't set the health to more than 100")
        elif health < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = health
        
    def set_power_level(self, power_level):
        if power_level > 10:
            print("You can't set the power level to more than 10")
        elif power_level < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = power_level

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health())
super_hero.set_health(110)
super_hero.set_health(-10)
super_hero.set_health(70)

print(super_hero.get_power_level())
super_hero.set_power_level(11)
super_hero.set_power_level(0)
super_hero.set_power_level(7)

print(f"{super_hero.name} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level")