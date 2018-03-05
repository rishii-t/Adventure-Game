class Barrier:
	name = None
	passable = False
	state = None	# Used to store the state of doors or hidden passages.
	locked = None	# Used to store the state of locked doors, if applicable.

	verbose = False	# Used to determine whether or not include the barrier's description in the room description.

	def __init__(self, direction):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			raise NotImplementedError("Barrier direction is not recognized.")

	def description(self):
		raise NotImplementedError("Create a subclass instead!")

	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]

class Wall(Barrier):
	def description(self):
		return "There doesn't seem to be a path to the %s." % self.direction

class WoodenDoor(Barrier):
	name = 'Wooden Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.

	verbose = True	# Used to determine whether or not include the barrier's description in the room description.

	def description(self):
		if(self.state == 'closed'):
			return "An old wooden door blocks your path to the %s." % self.direction
		else:
			return "An old wooden door lies open before you to the %s." % self.direction

	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'wooden door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					self.state = 'open'
					self.passable = True
					return [True, "You tug on the handle, and the wooden door creaks open.", inventory]
				else:
					return [True, "The door is already open.", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You slam the old wooden door shut.", inventory]
				else:
					return [True, "The door is already closed.", inventory]

		return [False, "", inventory]


class LockedDoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.

	verbose = True	# Used to determine whether or not include the barrier's description in the room description.

	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "An imposing door with a lock blocks a passageway to the %s." % self.direction
			else:
				return "An imposing door blocks a passageway to the %s. " % self.direction
		else:
			return "An imposing door lies open before you to the %s." % self.direction

	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to open the door, but a lock holds it firmly shut. You need to unlock it first with the 3 keys.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You heave the once-locked door open.", inventory]
				else:
					return [True, "The door is already open.", inventory]
		#	if(verb == 'close'):
		#		if(self.state == 'open'):
			#		self.state = 'closed'
		#			self.passable = False
			#		return [True, "You push the massive door closed.", inventory]
			#	else:
			#		return [True, "The door is already closed.", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'keys'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'key 1' and inventory[index].name.lower() ==  'key 2' and inventory[index].name.lower() == 'key 3'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You insert the 3 keys into the lock and twist. The door opens by itself.", inventory]
						return [True, "You don't seem to have all the keys for that door.", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. Note: Enter the phrase 'keys' if you have all the keys. Otherwise, you will not be able to open the door", inventory]
					else:
						return [True, "What item do you plan to unlock that door with?", inventory]
				else:
					return [True, "The door is already unlocked.", inventory]

		return [False, "", inventory]
