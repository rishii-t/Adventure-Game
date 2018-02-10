class MapTile:
	def __init__(self, x=0, y=0):
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

class ContRoomTile(MapTile):
	def intro_text(self):
		return """This is the control room. You see """


class VictoryTile(MapTile):
	def intro_text(self):
		return """You see a bright light in the distance...
		It grows as you get closer! It's sunlight!
		Victory is yours!
		"""

class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[None,                VictoryTile(),      None],
		[None,                BoringTile(),       None],
		[BoringTile(),        SpawnTile(),        BoringTile()],
		[None,                BoringTile(),       None]
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
