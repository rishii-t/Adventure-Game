import items

class Enemy:
	name = "Do not create raw enemies!"
	description = "There is no description here because you should not create raw Enemy objects!"
	attack_description = "There is no attack_description here because you should not create raw Enemy objects!"

	hp = 0
	damage = 0

	loot = []

	agro = False	# Used to cause enemies to attack spontaneously.

	def __init__(self, direction = None, loot = []):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			self.direction = None

		if(len(self.loot) > 0):
			for item in loot:
				self.loot.append(item)
		else:
			self.loot = loot

	def __str__(self):
		return self.name

	def check_text(self):
		text = ""
		if(self.direction):
			text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description
		return text

	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "The %s took %d damage." % (self.name, amount)

	def is_alive(self):
		return self.hp > 0

	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Demogorgon(Enemy):
	name = "Demogorgon"
	description = "A scary alien-looking creature"
	hp = 10
	damage = 2


class VirusBot(Enemy):
	name = "VirusBot"
	description = "A robot engaged by the virus."
	hp = 300
	damage = 10
	loot = [items.Key1("The Virus is Holding the first key")]
	agro = True

class ComputerVirus(Enemy):
	name = "Bleh"
	description = "The  Computer Virus that has locked you in"
	hp = 3000
	damage = 0




class Slime(Enemy):
	name = "Slime"
	description = "A slimey virus created in the Research Lab."
	hp = 180
	damage = 15
	loot = [items.Key2("There is a key within the remanents of the primitive slime")]
