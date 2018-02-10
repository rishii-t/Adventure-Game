class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create a raw Weapon objects")

    def __str__(self):
        return self.name
class Pipe(Weapon):
    def __init(self)
        self.name = "Brass Pipe"
        self.description = "A jagged brass pipe from a broken piping system."
        self.damage = 50

class Knife(Weapon)
