from random import randint 	# Used to generate random integers.

class Item:
	name = "Do not create raw Item objects!"

	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."

	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.

	value = 0		# Used to establish value if item is for sale.


	def __init__(self, description = "", value = 0):
		if(description):
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description

		if(self.value == 0):
			self.value = value

	def __str__(self):
		return self.name

	def room_text(self):
		if(not self.is_dropped):					# We may want to have a different description for a weapon the first time it is encountered vs. after it has been dropped.
			return self.intro_description
		else:
			return self.dropped_description

	def check_text(self):
		return self.description

	def drop(self):
		self.is_dropped = True

	def pick_up(self):
		self.is_dropped = False

	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Pipe(Weapon):
    def __init(self)
        name = "Brass Pipe"
        description = "A jagged brass pipe from a broken piping system."
        damage = 50



class Knife(Weapon):
    def __init(self)
        name = "Knife"
        description = "It's not an actual knife, instead its a jagged piece of metal you found in someones body."
        damage = 50



class DemogorganTeeth(Weapon):
    def __init(self)
        name = "Dem Teeth"
        descirption = 'Teeth from a Doggerman. Etching in the handle says "use Wordplays"'
        damage = 7


class Gun(Weapon):
    def __init(self)
        name = "Snake Gun"
        description = "Gun that shoots black worms that crawl into the enemies mouth. Proceeds to eat the inside of the enemy. Yum"
        damage = 60


class OpSword(Weapon):
    def __init(self)
        name = "Ironically Op Sword"
        description = "Read the name"
        damage = 1000000000000000
        effect = "One use per battle"


class HandCannon(Weapon):
    def __init(self)
        name = "Hand Cannon"
        description = "A cannon that was shrunk to fit a human hand"
        damage = 90
