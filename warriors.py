class Warrior():
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Type: {self.__class__.__name__}, Health: {self.health}, Attack: {self.attack}"

# warrior + N — увеличивает здоровье и атаку на N

    def __add__(self, other):
        if isinstance(other, int):
            return Warrior(self.health + other, self.attack + other)
        else:
            return other
        return NotImplemented

# warrior * N — увеличивает здоровье и атаку в N раз

    def __mul__(self, other):
        if isinstance(other, int):
            return Warrior(self.health * other, self.attack * other)
        else:
            return other
        return NotImplemented


print(Warrior())
warrior_exam = Warrior(health=45, attack=7)
print(warrior_exam)
print(warrior_exam.is_alive())
warrior_kill = Warrior(health=0, attack=2)
print(warrior_kill)
print(warrior_kill.is_alive())
warrior_recov = warrior_kill + 3
print(warrior_recov)
warrior_prime = warrior_exam * 2
print(warrior_prime)
warrior_prime = warrior_exam * -2
print(warrior_prime)
warrior_prime = warrior_exam * 'a'
print(warrior_prime)


class Orc(Warrior):

    def __init__(self, health=55, attack=6, fury=2):
        super().__init__(health, attack)
        self.fury = fury

    def __str__(self):
        return f"Type: {self.__class__.__name__}, Health: {self.health}, Attack: {self.attack}, Fury: {self.fury}"

    def __add__(self, other):
        if isinstance(other, int):
            if self.is_alive():
                self.fury += other
                return f"Type: {self.__class__.__name__}, Health: {self.health}, Attack: {self.attack}, Fury: {self.fury}"
            else:
                return other
        return NotImplemented


print(Orc())
orc = Orc()
print(orc.is_alive())
orc2 = orc + 3
print(orc2)


# 3. Функция fight() — бой между двумя воинами

def fight(warrior, orc):

    while warrior.is_alive() and orc.is_alive():
        damage_from_1 = warrior.attack
        orc.health = orc.health - damage_from_1
        if orc.health <= 0:
            print("Результат боя: Воин победил")
            return True
        damage_from_2 = orc.attack + orc.fury
        warrior.health = warrior.health - damage_from_2
        if warrior.health <= 0:
            print("Результат боя: Орк победил")
            return False


boris = Warrior()
emelya = Orc()
print(fight(boris, emelya))
