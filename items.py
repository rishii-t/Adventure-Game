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

class Knife(Weapon):
    def __init(self)
        self.name = "Knife"
        self.description = "It's not an actual knife, instead its a jagged piece of metal you found in someones body."
        self.damage = 50


class DemogorganTeeth(Weapon):
    def __init(self)
        self.name = "Dem Teeth"
        self.descirption = "Teeth from a Demogorgan,lul"
        self.damage = 7

class Gun(Weapon):
    def __init(self)
        self.name = "Snake Gun"
        self.description = "Gun that shoots black worms that rawl into the enemies mouth. Proceeds to eat the inside of the enemy. Yum"
        self.damage = 100
