class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create a raw Weapon objects")

    def __str__(self):
        return self.name
class Pipe(Weapon):
    def __init(self)
        self.name = "Brass Pipe"
        self.description = "A jagged brass pipe from a broken piping system."
        self.damage = 50
        self.effect =


class Knife(Weapon):
    def __init(self)
        self.name = "Knife"
        self.description = "It's not an actual knife, instead its a jagged piece of metal you found in someones body."
        self.damage = 50
        self.effect = bleeding


class DemogorganTeeth(Weapon):
    def __init(self)
        self.name = "Dem Teeth"
        self.descirption = 'Teeth from a Doggerman. Etching in the handle says "use Wordplays"'
        self.damage = 7


class Gun(Weapon):
    def __init(self)
        self.name = "Snake Gun"
        self.description = "Gun that shoots black worms that crawl into the enemies mouth. Proceeds to eat the inside of the enemy. Yum"
        self.damage = 60


class OpSword(Weapon):
    def __init(self)
        self.name = "Ironically Op Sword"
        self.description = "Read the name"
        self.damage = 1000000000000000
        self.effect = "One use per battle"


class HandCannon(Weapon):
    def __init(self)
        self.name = "Hand Cannon"
        self.description = "A cannon that was shrunk to fit a human hand"
        self damage = 90
        self.effect = piercing
