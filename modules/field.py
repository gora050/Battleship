from modules.ship import Ship
import random


class Field():
    def __init__(self, ships=[4, 3, 2, 2, 2, 1, 1, 1, 1], symbols="▣☒☼▢"):
        self.size = [10, 10]
        self.symbols = symbols
        self.ships = []
        self.generate(ships)

    def __str__(self, ship=False):
        number_len = len(str(len(self.field)))
        field_str = " " * (number_len + 3) + " A B C D E F G H I J\n" +\
                    " " * (number_len + 3) + "┏━" +\
                    ("━┻"*self.size[0])[1:] + "━┓\n"
        for i in range(len(self.field)):
            field_str += " " * (number_len - len(str(i + 1)) + 1) +\
                       str(i+1) + " ━┫ " + (" ".join([self.symbols[3]
                                            if (y[0] not in self.symbols[1:3]
                                            and not ship) else y[0]
                                           for y in self.field[i]])) + " ┃\n"
        field_str += " "*(number_len+3) + "┗━" + ("━━"*self.size[0])[1:] + "━┛"
        return field_str

    def get_field(self, with_ships):
        return self.__str__(ship=with_ships)

    def alive_ships(self):
        return sum(self.ships)

    def shoot_at(self, coords):
        if self.field[coords[0]-1][coords[1]-1][0] in self.symbols[1:3]:
            return -1
        try:
            self.field[coords[0]-1][coords[1]-1][0] = self.symbols[1]
            return self.field[coords[0] - 1][coords[1] - 1][1].\
                shoot_at((coords[0] - 1, coords[1] - 1))
        except Exception as e:
            self.field[coords[0] - 1][coords[1] - 1] = (self.symbols[2], 0)
            return -1

    def generate(self, ships):
        self.field = [[(self.symbols[3], 0)] * self.size[0]
                      for y in range(self.size[1])]
        free_cells = set([(x, y) for x in range(self.size[0])
                         for y in range(self.size[1])])
        ships.sort(reverse=True)
        for i in range(len(ships)):
            placed = False
            while placed is False:
                cells = []
                init_point = random.choice(tuple(free_cells))
                status = True
                horizontal = random.random() < 0.5
                rotate = [[0, 1], [1, 0]]
                for g in range(ships[i]):
                    point = (init_point[0] + g * rotate[horizontal][0],
                             init_point[1] + g * rotate[horizontal][1])
                    if point in free_cells:
                        cells.append(point)
                    else:
                        status = False
                        break
                if status:
                    ship = Ship(init_point, horizontal, ships[i])
                    self.ships.append(ship)
                    for cell in cells:
                        for ci in range(-1, 2):
                            for ck in range(-1, 2):
                                try:
                                    free_cells.remove((cell[0] + ci,
                                                       cell[1] + ck))
                                except:
                                    pass
                        self.field[cell[0]][cell[1]] = [self.symbols[0], ship]
                    placed = True
