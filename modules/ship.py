class Ship():
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.alive = [1] * length

    def __repr__(self):
        return str(sum(self.alive))

    def __add__(self, other):
        return sum(self.alive) + other

    def __radd__(self, other):
        return sum(self.alive) + other

    def shoot_at(self, coord):
        self.alive[abs(self.bow[0] - coord[0] if self.horizontal
                   else self.bow[1] - coord[1])] = 0
        return sum(self.alive)
