from abc import ABC, abstractmethod

class Weapon (ABC):
    @abstractmethod
    def __init__(self, accuracy):
        self.accuracy = accuracy

    @abstractmethod
    def attack(self, Monster):
        pass

class Sword(Weapon):
    def __init__(self, accuracy):
        self.accuracy = accuracy
        self.name = "меч"
    def attack(self, Monster):
        print("Боец атаковал "+Monster.name+" порезав его.")
        Monster.lives -= self.accuracy

class Bow(Weapon):
    def __init__(self, accuracy):
        self.accuracy = accuracy
        self.name = "лук"
    def attack(self, Monster):
        print("Боец атаковал "+Monster.name+" прострелив его.")
        Monster.lives -= self.accuracy
class Fighter():
    def __init__(self, name, lives):
        self.name = name
        self.weapon = None
        self.lives = lives

    def changeWeapon(self, Weapon):
        self.weapon = Weapon
        print("Боец выбират "+Weapon.name+".")

class Monster():
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
    def attack(self, Fighter):
        print(self.name+ " атаковал "+Fighter.name+" укусив его.")
        Fighter.lives -= 1

def TheDuel (Fighter , Monster):
    print("Начался бой "+Fighter.name+" с "+Monster.name)
    while True :
        if Monster.lives <= 0 :
            print(Monster.name + " метрв.")
            break
        if Fighter.lives <= 0 :
            print(Fighter.name + " метрв.")
            break
        Monster.attack(Fighter)
        Fighter.weapon.attack(Monster)


f = Fighter("Петя", 2)
m = Monster("паук", 3)

f.changeWeapon(Bow(1))
TheDuel (f, m)

f = Fighter("Петя", 2)
f.changeWeapon(Sword(3))
TheDuel (f, m)