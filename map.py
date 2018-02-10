class MapTile:
	def __init__(self, x=7, y=9):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")


class SpawnTile(MapTile):
	def intro_text(self):
		return """You wake up in your cabin. Not everthing comes back to you.
        All you remember is a mechanic, alarms, and a crash.
        There is a bright in the room. As you look around you realize you are in
        a space station.
		"""


class WorkTile(MapTile):
	def intro_text(self):
		return """You are in a massive room: the work station. There are many cubicles, mini- lab stations
        and papers all over the floor. The light is flickering. """

class LivingQuarters(MapTile):
	def intro_text(self):
		return """You """

class ContRoomTile(MapTile):
	def intro_text(self):
		return """This is the control room. You see hundreds of pipes running in different directions.
		There is a low hiss and a broken copper pipe in the corner. In the back corner of the room,
		there are dials spinning in crazy directions. On your left you see a red lever and above it that says
		'EMERGENCY SHUTOFF'."""

class Recreation(MapTile):
	def intro_text(self):
		return """You are in a small room filled with work-out equipment. On the floor there is a
		a leather jacket with a label 'Scott Clarke' . The jacket has
		blood stains.   """
class Basement(MapTile):
	def intro_text(self):
		return """Basement   """

class EastHall(MapTile):
	def intro_text(self):
		return """EastHall   """

class SouthHall(MapTile):
	def intro_text(self):
		return """SouthHall  """

class NorthHall(MapTile):
	def intro_text(self):
		return """NorthHall   """


class VictoryTile(MapTile):
	def intro_text(self):
		return """You see a bright light in the distance...
		It grows as you get closer! It's sunlight!
		Victory is yours!
		"""
class WasteRoom(MapTile):
	def intro_text(self):
		return """ WasteRoom   """

class ETP(MapTile):
	def intro_text(self):
		return """ ETP   """

class RocketPad(MapTile):
	def intro_text(self):
		return """RP   """

class RocketPadReal(MapTile):
	def intro_text(self):
		return """RP Real  """

class WorkRoom(MapTile):
	def intro_text(self):
		return """Work WorkRoom   """

class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Basement(), 		None,		None,		None,			None, 			None, 			SpawnTile(), 	None, 		None, None],
		[None, 				None,		None,		None, 			None, 			None, 			NorthHall(), 	None, 		None, None],
		[None,				None,		None,		None, 			WorkRoom(), 	WorkRoom(), 	WorkRoom(), 	WorkRoom(), None, None],
		[RocketPadReal(),	EastHall(), RocketPad(),EastHall(), 	WorkRoom(), 	WorkRoom(), 	WorkRoom(), 	WorkRoom(), None, None],
		[None,				None,		None,		None, 			WorkRoom(), 	WorkRoom(), 	WorkRoom(), 	WorkRoom(), None, None],
		[None,				None,		None,		None, 			SouthHall(), 	None, 			SouthHall(), 	None, 		None, None],
		[None,				None,		None,		None, 			WasteRoom(), 	None, 			ETP(), 			None, 		None, None],
		[None, 				None,		None,		None, 			None, 			None, 			ETP(),			None, 		None, None],
		[None, 				None,		None,		None, 			None, 			None, 			ETP(),			None, 		None, None],
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i

	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None

	def check_north(self, x, y):
		if y-1 < 0:
			room = None
		try:
			room = self.map[y-1][x]
		except IndexError:
			room = None

		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be anything to the north."]

	def check_south(self, x, y):
		if y+1 < 0:
			room = None
		try:
			room = self.map[y+1][x]
		except IndexError:
			room = None

		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be anything to the south."]

	def check_west(self, x, y):
		if x-1 < 0:
			room = None
		try:
			room = self.map[y][x-1]
		except IndexError:
			room = None

		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be anything to the west."]

	def check_east(self, x, y):
		if x+1 < 0:
			room = None
		try:
			room = self.map[y][x+1]
		except IndexError:
			room = None

		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be anything to the east."]
