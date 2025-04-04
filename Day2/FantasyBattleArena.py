
class Character:

    def __init__(self,name,health,attack_power,defense,speed):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defense=defense
        self.speed=speed

    def attack(self,target):
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name}")

    def take_damage(self,amount): 
        self.health -= amount
        print(f"{self.name} takes {amount} damage. remaining health {self.health} ")

    def is_alive(self):

        if self.health>0:
            True
        else:
            False

#single level inhertance
class Warrior(Character):

    def __init__(self, name, health, attack_power, defense, speed,rage):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage=rage
        
    def berserkMode(self):
        if self.health < 0.3:
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")


class Mage(Character):

    def __init__(self, name, health, attack_power, defense, speed,mana):
        super().__init__(name, health, attack_power, defense, speed)

        self.mana=mana
    def fireBall(self):
        pass


class Archer(Character):

    def __init__(self, name, health, attack_power, defense, speed,critical_chance):
        super().__init__(name, health, attack_power, defense, speed)

        self.critical_chance=critical_chance

    def predicationShot(self):
        pass


        