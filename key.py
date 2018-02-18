class Key:
    def __init__(self):
        raise NotImplementedError("Do not create a raw Key objects")

    def __str__(self):
        return self.name

class K1(Key):
    self.name = "First acquirable key. Shows the number 1."

class K2(Key):
    self.name = "Second acquirable key. Shows the number 1."

class K3(Key):
    self.name = "Third acquirable key. Shows the number 9."

class K4(Key):
    self.name = "Fourth acquirable key. Shows the number 5."

class K5(Key):
    self.name = "Fifth acquirable key. Shows the number 4."

class K6(Key):
    self.name = "Sixth acquirable key. Shows the number 2."
