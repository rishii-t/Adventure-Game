import items
import walls
import enemy

from random import randint

class MapTile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	walls = []
	enemy = []
	items = []


	def __init__(self, x=0, y=0, walls = [], items = [], enemy = []):
		self.x = x
		self.y = y
		for walls in walls:
			self.add_walls(walls)
		for item in items:
			self.add_item(item)
		for enemy in enemy:
			self.add_enemy(enemy)

	def intro_text(self):
		text = self.description
		for walls in self.walls:
			if(walls.verbose):
				text += " " + walls.description()
		#for enemy in self.contents['enemy']:
		#	text += " " + enemy.description()
		for item in self.items:
			text += " " + item.room_text()
		return text

	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1):
						if(isinstance(self.items[index], items.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif(verb == 'drop'):
				for index in range(len(inventory)):
					if(inventory[index].name.lower() == noun1):
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		for list in [self.walls, self.items, self.enemy]:
			for item in list:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if(status):
					return [status, description, inventory]

		for list in [self.walls, self.items, self.enemy]:			# Added to give the player feedback if they have part of the name of an object correct.
			for item in list:
				if(item.name):
					if(noun1 in item.name):
						return [True, "Be more specific.", inventory]

		return [False, "", inventory]

	def add_walls(self, walls):
		if(len(self.walls) == 0):
			self.walls = [walls]		# Initialize the list if it is empty.
		else:
			self.walls.append(walls)	# Add to the list if it is not empty.

	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.

	def add_enemy(self, enemy):
		if(len(self.enemy) == 0):
			self.enemy = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemy.append(enemy)

			first.ecounter = True

	def check_text(self):
		if(self.first_encounter):
			text = self.first_time()
			return text
		else:
			return self.description

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		return self.description

class SpawnTile(MapTile):
	description = """You enter a messy room. There are clothes strewn everywhere. """



class WorkTile(MapTile):
	description = """You are in a massive room: the work station. There are many cubicles, mini- lab stations
        and papers all over the floor. The light is flickering. """

class LivingQuarters(MapTile):
	description = """You enter in your companions room. There is no sign of him."""

class ContRoomTile(MapTile):
	items = [items.Gun("The is a gun on the control panel. Have fun")]
	description = """This is the control room. You see hundreds of pipes running in different directions.
		There is a low hiss and a broken copper pipe in the corner. In the back corner of the room,
		there are dials spinning in crazy directions. On your left you see a red lever and above it that says
		'EMERGENCY SHUTOFF'."""

class Recreation(MapTile):
	description = """You are in a small room filled with work-out equipment. On the floor there is a
		a leather jacket with a label 'Scott Clarke' . The jacket has
		blood stains.   """

	def random_spawn(self):
		if(randint(0,1) == 0):		# 1 in 2 odds.
			self.enemy = [enemy.VirusBot()]
		else:
			self.enemy = []

class Ellis(MapTile):
	description = """There is a computer screen in the distance. As you approach it lights up at says
		'Hello! My name is E.L.L.I.S. I am the computer systems module that runs
		in this facility.' """
	def random_spawn(self):
		if(randint(0,1) == 0):		# 1 in 2 odds.
			self.enemy = [enemy.VirusBot()]
		else:
			self.enemy = []

class Basement(MapTile):
	description = """You are in a dark Basement. The Basment has pipes and wires running on it's walls.
		There are a few boxes on the floor and an open minifridge in the corner. The minifridge has an Energy Drink. """
	items = [items.OpSword("There is a sword leaning on the wall. You shouldn't take it")]
		#items.HandCannon("There is a hand cannon on the shelf")
		#Consumable.EnergyDrink("There is an energy drink in the mini fridge")]

class EastHall(MapTile):
	description = """You are in the East Hall. The hall has pipes and wires running on it's walls.  """

class SouthHall(MapTile):
	description = """You are in the South Hall. The hall has pipes and wires running on it's walls.
		Yet, there is something very strange about the south hall. It is almost as if
		everything is offset. The door to the south is to the Exit Transport Pod but you need 3 keys to unlock it and escape.  """

class NorthHall(MapTile):
	description = """You are in the North Hall. The hall has pipes and wires running on it's walls.  """


class Laboratory(MapTile):
	enemy = [enemy.Slime()]
	description = """You are in a Laboratory. There is giant telescope in the corner.
		There are also rows of counters with different lab equipment you cannot idenitfy.
		Most of the cabinets underneath the counters are broken. However, there is one counter that is covered in green slime and it's cabinets are locked.
		"""
class WasteRoom(MapTile):
	description = """ There are pipes and tubing everywhere. In the center there is
		giant tank, most probably where the waste is recycled. For some reason, the system
		display is stuck on a random screen. The stench is also horrible and their
		is waste on the floor.  """

	def random_spawn(self):
		if(randint(0,1) == 0):		# 1 in 2 odds.
			self.enemy = [enemy.VirusBot()]
		else:
			self.enemy = []

class ETP(MapTile):
	description = """You are in the ETP, the Exit Transport Pod. You have sucessfully completed the game in the stage that it is now. Thank You For Playing. """

class RocketPad(MapTile):
	enemy = [enemy.Demogorgon()]
	description = """You are in the Rocket Pad Chamber. There is a gigantic platform in the center.
		The ceiling consists of a series of metal plates that seem to be interconnected with
		each other.   """

class RocketPadReal(MapTile):
	description = """You are in the Rocket Pad Chamber. There is a gigantic platform in the center.
		The ceiling consists of a series of metal plates that seem to be interconnected with
		each other.  There is a robot in the corner that seems to be disabled."""

class MainDeck(MapTile):
	description = """You are in the mainframe of this Space Base. There a rows of computers, desks, and cubicles lined across.
		The computer systems all show the same error message. There are papers scattered everywhere. In the center of the
		room is a gigantic hologram model of the space base. The model seems to display where everthing is.  """

	def random_spawn(self):
		if(randint(0,2) == 0):		# 1 in 2 odds.
			self.enemy = [enemy.VirusBot()]
		else:
			self.enemy = []

class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[None, 			  None,		  None,		   None,			                        None, 			LivingQuarters(), 	SpawnTile(walls = [walls.WoodenDoor('s')]), 	LivingQuarters(), 	None, 			  None],
		[None, 			  Basement(), None,	       None, 			                        Recreation(), 	None, 				NorthHall(), 	None, 				None, 			  None],
		[None,			  None,		  None,		   None, 			                        MainDeck(walls = [walls.WoodenDoor('n')]), 	MainDeck(), 	    MainDeck(), 	MainDeck(walls = [walls.WoodenDoor('e')]), 	    ContRoomTile(walls = [walls.WoodenDoor('w')]),   None],
		[RocketPadReal(walls = [walls.WoodenDoor('e')]), EastHall(), RocketPad(walls = [walls.WoodenDoor('e')]), EastHall(), 	                            MainDeck(), 	MainDeck(), 		MainDeck(), 	MainDeck(), 		None, 		   	  None],
		[None,			  None,		  None,		   Laboratory(walls = [walls.Wall('e')]), 	MainDeck(), 	MainDeck(), 		MainDeck(), 	MainDeck(), 		Ellis(), 		  None],
		[None,			  None,		  None,		   Laboratory(walls = [walls.Wall('e')]), 	SouthHall(walls = [walls.WoodenDoor('n')]), 	None, 				SouthHall(walls = [walls.LockedDoor('s')]), 	None, 				None, 			  None],
		[None,			  None,		  None,		   None, 			                        WasteRoom(walls = [walls.WoodenDoor('n')]), 	None, 				ETP(), 			None, 				None, 			  None],
		]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i

					self.add_implied_walls(j,i)	# If there are implied walls (e.g. edge of map, adjacent None room, etc.) add a Wall.


	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None

	def check_north(self, x, y):
		for enemy in self.map[y][x].enemy:
			if(enemy.direction == 'north'):
				return [False, enemy.check_text()]
		for barrier in self.map[y][x].walls:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]

		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None

		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]

	def check_south(self, x, y):
		for enemy in self.map[y][x].enemy:
			if(enemy.direction == 'south'):
				return [False, enemy.check_text()]
		for barrier in self.map[y][x].walls:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]

		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None

		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for enemy in self.map[y][x].enemy:
			if(enemy.direction == 'west'):
				return [False, enemy.check_text()]
		for barrier in self.map[y][x].walls:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]

		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None

		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]

	def check_east(self, x, y):
		for enemy in self.map[y][x].enemy:
			if(enemy.direction == 'east'):
				return [False, enemy.check_text()]
		for barrier in self.map[y][x].walls:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]

		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None

		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]

	def add_implied_walls(self, x, y):

		[status, text] = self.check_north(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemy:
				if enemy.direction == 'north':
					barrier_present = True
			for barrier in self.map[y][x].walls:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_walls(walls.Wall('n'))

		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemy:
				if enemy.direction == 'south':
					barrier_present = True
			for barrier in self.map[y][x].walls:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_walls(walls.Wall('s'))

		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemy:
				if enemy.direction == 'east':
					barrier_present = True
			for barrier in self.map[y][x].walls:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_walls(walls.Wall('e'))

		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemy:
				if enemy.direction == 'west':
					barrier_present = True
			for barrier in self.map[y][x].walls:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_walls(walls.Wall('w'))

	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if(room):
					room.update(player)
