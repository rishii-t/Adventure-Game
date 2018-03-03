from random import randint
class Weapon:
    equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.

	def equip_text(self):
		return self.equip_description

	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]


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
