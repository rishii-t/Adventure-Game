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


class Pipe(Item):
    def __init(self):
        name = "Brass Pipe"
        description = "A jagged brass pipe from a broken piping system."
        dropped_description = "There is a pipe on the ground."
        damage = 50




class Knife(Item):
    def __init(self):
        name = "Knife"
        description = "It's not an actual knife, instead its a jagged piece of metal you found in someones body."
        dropped_description = "There is a knife on the ground."
        damage = 50



class DemogorganTeeth(Item):
    def __init(self):
        name = "Dem Teeth"
        descirption = 'Teeth from a Doggerman. Etching in the handle says "use Wordplays"'
        dropped_description = "There is are demogorgan teeth on the ground."
        damage = 10


class Gun(Item):
    def __init(self):
        name = "Snake Gun"
        description = "Gun that shoots black worms that crawl into the enemies mouth. Proceeds to eat the inside of the enemy. Yum"
        dropped_description = "There is a gun on the ground."
        damage = 60


class OpSword(Item):
    def __init(self):
        name = "Ironically Op Sword"
        description = "Read the name"
        dropped_description = "There is a glowing sword on the ground."
        damage = 1000000000000000


class HandCannon(Item):
    def __init(self):
        name = "Hand Cannon"
        description = "A cannon that was shrunk to fit a human hand"
        dropped_description = "There is a huge gun on the ground."
        damage = 90


class Consumable(Item):
	consume_description = "You should define flavor text for consuming this item in its subclass."

    healing_value = 0

	def consume(self):
		return [self.consume_description, self.dropped_description, self.healing_value]


class EnergyDrink(Consumable):
	name = "red potion"
	healing_value = 75

	description = " An Energy Drink from your local SpaceMart. It doesn't look expired"
	dropped_description = "An Energy Drink is on the ground."
	consume_description = "You drink the Energy Drink."

class Key(Item):
    description = "flavor text"

	def consume(self):
		return [self.description]
