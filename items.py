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

class Weapon(Item):
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.

	def equip_text(self):
		return self.equip_description

	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]		# Return damage and a random attack description from your list.


class Pipe(Weapon):
	def __init__(self):
		name = "brass pipe"
		description = "A jagged brass pipe from a broken piping system."
		dropped_description = "There is a pipe on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
		damage = 50




class Knife(Weapon):
	def __init__(self):
		name = "knife"
		description = "It's not an actual knife, instead its a jagged piece of metal you found in someones body."
		dropped_description = "There is a knife on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
		damage = 50



class DemogorganTeeth(Weapon):
		name = "dem tooth"
		descirption = 'Teeth from a Domogorgon. Etching in the handle says "use Wordplays"'
		dropped_description = "There are demogorgan teeth on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
		damage = 10


class Gun(Weapon):
		name = "gun"
		description = "Gun that shoots black worms that crawl into the enemies mouth. Proceeds to eat the inside of the enemy. Yum"
		dropped_description = "There is a gun on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
		damage = 60


class OpSword(Weapon):
		name = "Ironically Op Sword"
		description = "Read the name"
		dropped_description = "There is a glowing sword on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
		damage = 1000000000000000


class HandCannon(Weapon):
		name = "Hand Cannon"
		description = "A cannon that was shrunk to fit a human hand"
		dropped_description = "There is a huge gun on the ground."
		equip_description = "You arm yourself with the rock."
		attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
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

class Key1(Item):
	name = "Key 1"
	description = "1st aqcuirable key used"

	def consume(self):
		return [self.description]
class Key2(Item):
	name = "Key 2"
	description = "2nd aqcuirable key"

	def consume(self):
		return [self.description]
class Key3(Item):
	name = "Key 3"
	description = "3st aqcuirable key used"

	def consume(self):
		return [self.description]
class Gold(Item):
	name = "Gold"
	description = "This shouldn't exist."
