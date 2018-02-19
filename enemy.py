class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name
		return self.description

	def is_alive(self):
		return self.hp > 0


class Doggerman(Enemy):
	def __init__(self):
		self.name = "Doggerman"
		self.description = "Has a peculiar face that splits into five petals with teeth. Built with a humanoid body."
		self.hp = 100
		self.damage = 10


class Ogre(Enemy):
	def __init__(self):
		self.name = "Ogre"
		self.hp = 30
		self.damage = 10


class BatColony(Enemy):
	def __init__(self):
		self.name = "Colony of bats"
		self.hp = 100
		self.damage = 4


class RockMonster(Enemy):
	def __init__(self):
		self.name = "Rock Monster"
		self.hp = 80
		self.damage = 15
