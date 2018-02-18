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
        There is a bright in the room. As you look out the window you realize you are in
        a space station!
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

class Ellis(MapTile):
	def intro_text(self):
		return """There is a computer screen in the distance. As you approach it lights up at says
		'Hello! My name is E.L.L.I.S. I am the computer systems module that runs
		in this facility.' """

class Basement(MapTile):
	def intro_text(self):
		return """ You enter a dark room. In here are scattered tools and remains across the floor
		that you cannot identify. In the east corner there is a box labeled WIRES. On
		the west corner there is a minfridge.  """

class EastHall(MapTile):
	def intro_text(self):
		return """You are in the East Hall. The hall has pipes and wires running on it's walls.  """

class SouthHall(MapTile):
	def intro_text(self):
		return """You are in the South Hall. The hall has pipes and wires running on it's walls.
		Yet, there is something very strange about the south hall. It is almost as if
		everything is offset.  """

class NorthHall(MapTile):
	def intro_text(self):
		return """You are in the North Hall. The hall has pipes and wires running on it's walls.  """


class Laboratory(MapTile):
	def intro_text(self):
		return """You are in a Laboratory. There is giant telescope in the corner.
		There are also rows of counters with different lab equipment you cannot idenitfy.
		Most of the cabinets underneath the counters are broken. However, there is one counter that
		is strangly clean and it's cabinets are locked.
		"""
class WasteRoom(MapTile):
	def intro_text(self):
		return """ There are pipes and tubing everywhere. In the center there is
		giant tank, most probably where the waste is recycled. For some reason, the system
		display is stuck on a random screen. The stench is also horrible and their
		is waste on the floor.  """

class ETP(MapTile):
	def intro_text(self):
		return """You are in the ETP, the Exit Transport Pod. Unfortunately, the pod is locked.
		It seems as if the door had been manually locked.  """

class RocketPad(MapTile):
	def intro_text(self):
		return """You are in the Rocket Pad Chamber. There is a gigantic platform in the center.
		The ceiling consists of a series of metal plates that seem to be interconnected with
		each other.   """

class RocketPadReal(MapTile):
	def intro_text(self):
		return """You are in the Rocket Pad Chamber. There is a gigantic platform in the center.
		The ceiling consists of a series of metal plates that seem to be interconnected with
		each other.  There is a robot in the corner that seems to be disabled. Try to turn it on. """

class WorkRoom(MapTile):
	def intro_text(self):
		return """You are in the mainframe of this Space Base. There a rows of computers, desks, and cubicles lined across.
		The computer systems all show the same error message. There are papers scattered everywhere. In the center of the
		room is a gigantic hologram model of the space base. The model seems to display where everthing is.  """

class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Basement(), 		None,		None,		None,			None, 			LivingQuarters(), 	SpawnTile(), 	LivingQuarters(), 	None, 			None],
		[None, 				None,		None,		None, 			Recreation(), 	None, 				NorthHall(), 	None, 				None, 			None],
		[None,				None,		None,		None, 			WorkRoom(), 	WorkRoom(), 		WorkRoom(), 	WorkRoom(), 		ContRoomTile(), None],
		[RocketPadReal(),	EastHall(), RocketPad(),EastHall(), 	WorkRoom(), 	WorkRoom(), 		WorkRoom(), 	WorkRoom(), 		None, 			None],
		[None,				None,		None,		Laboratory(), 	WorkRoom(), 	WorkRoom(), 		WorkRoom(), 	WorkRoom(), 		Ellis(), 			None],
		[None,				None,		None,		Laboratory(), 	SouthHall(), 	None, 				SouthHall(), 	None, 				None, 			None],
		[None,				None,		None,		None, 			WasteRoom(), 	None, 				ETP(), 			None, 				None, 			None],
		[None, 				None,		None,		None, 			None, 			None, 				ETP(),			None, 				None, 			None],
		[None, 				None,		None,		None, 			None, 			None, 				ETP(),			None, 				None, 			None],
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
