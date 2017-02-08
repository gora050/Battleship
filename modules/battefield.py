# That module contains all function dedicated to field-generation and checking

import random


def read_field(filename):
    """(str) -> [(int,int),bool,{(int,int):[str,(int,int)]}]
    Reads battlefield from file [filename] and returns it in such format:
    [
        (int width, int height), -- Battlefield size
        bool is_valid, -- True - if this Battlefield is valid standart
battlefield: size is 10x10 and there placed 4 ship (1,1), 3 ships (2,1),
2 ships (3,1), 1 ship (4,1). Also there minimum 1 empty cell between every pair
        {
            (int x, int y) : [str symbol, (int max_size, int min_size)]
-- That dictionary contains every non-empty cell  (with ship). Kyes is
coordinates of that cell. Values is a list. Zero-indexed element of this list
contains char '*' if this part of ship is alive, and "X" if it is damaged.
Firs-indexed element of this list is tuple of 2 int's, that means ship size.
The largest number should at index 0 in this tuple. (Example: (4,1)).
        }
    ]
    """
    with open(filename) as field_file:
        field_str = field_file.readlines()
    field = [(), False, {}]
    ships = {}
    max_y = 10
    for x in range(len(field_str)):
        for y in range(len(field_str[x])):
            max_y = max(max_y, y)
            if field_str[x][y] in "*X":
                field[2][(x, y)] = [field_str[x][y], (0, 0)]
    field[0] = (len(field_str), max_y)

    for cell in field[2]:
        field[2][cell][1] = ship_size(field, cell)
    field[1] = is_valid(field)
    return field


def has_ship(field, coords):
    """ ([(int,int),bool,{(int,int):[str,(int,int)]}], (int, int)) -> bool
    Gets field, that should be saved by the standart described in read_field()
    Returns True, if cell with coords (coords[0],coords[1]) contains ship part
    """
    try:
        return True if field[coords][0] in "*X" else False
    except:
        return False


def ship_size(field, coords):
    """ ([(int,int),bool,{(int,int):[str,(int,int)]}], (int, int)) -> (int,int)
    Gets field, that should be saved by the standart described in read_field()
    Returns ship size of the smallest rectange, in wich we can put ship that
    contains cell by coordinates (coords[0], coords[1])
    If there no ship, will return (0,0)
    """
    checked = set()
    size = [[10**100, 10**100], [0, 0]]
    to_check = set([coords, coords])
    while to_check:
        p_to_check = set()
        for pair in to_check:
            try:
                if field[2][pair][0] in "*X":
                    if field[2][pair][1] == (0, 0):
                        p_to_check.add((pair[0] + 1, pair[1]))
                        p_to_check.add((pair[0], pair[1] + 1))
                        p_to_check.add((pair[0] - 1, pair[1]))
                        p_to_check.add((pair[0], pair[1] - 1))
                        size[0] = [min(size[0][0], pair[0]),
                                   min(size[0][1], pair[1])]
                        size[1] = [max(size[1][0], pair[0]),
                                   max(size[1][1], pair[1])]
                        checked.add(pair)
                    else:
                        return(field[2][pair][1])
            except:
                pass
        to_check = p_to_check.difference(checked)
        x_size = max(size[1][1] - size[0][1] + 1,
                     size[1][0] - size[0][0] + 1)
        y_size = min(size[1][1] - size[0][1] + 1,
                     size[1][0] - size[0][0] + 1)
    return (x_size, y_size)


def is_valid(field):
    """ [(int,int),bool,{(int,int):[str,(int,int)]}] -> bool
    Gets field, that should be saved by the standart described in read_field()
    Returns True if this field is valid standart field in order to standart
    Battleship rules. Size is 10x10 and there placed 4 ship with size (1,1),
    3 ships with size (2,1), 2 ships with size (3,1), 1 ship with size  (4,1).
    Also there minimum 1 empty cell between every pair of ships
    """
    if field[0] == (10, 10):
        ships = [0, [0] * 5]
        try:
            for cell in field[2]:
                ships[field[2][cell][1][1]][field[2][cell][1][0]] += 1
        except:
            return False
        if ships[1][1] == 4 and ships[1][2] == 6 and\
           ships[1][3] == 6 and ships[1][4] == 4:
            return True
    else:
        return False


def field_to_str(field):
    """[(int,int),bool,{(int,int):[str,(int,int)]}] -> str
    Gets field, that should be saved by the standart described in read_field()
    Returns str, that represents our field in string for printing
    """
    field_str = []
    for i in range(field[0][1]):
        field_str.append([" "] * field[0][0])
    for cell in field[2]:
        field_str[cell[0]][cell[1]] = field[2][cell][0]
    return "\n".join(map(lambda x: "".join(x), field_str))


def generate_field():
    """ () -> [(int,int),bool,{(int,int):[str,(int,int)]}]
    Generates valid field by standart battlefield rules in order
    to is_valid(field) and read_field(filename) standarts.
    Format:
    [
        (int width, int height), -- Battlefield size
        bool is_valid, -- True - if this Battlefield is valid standart
battlefield: size is 10x10 and there placed 4 ship (1,1), 3 ships (2,1),
2 ships (3,1), 1 ship (4,1). Also there minimum 1 empty cell between every pair
        {
            (int x, int y) : [str symbol, (int max_size, int min_size)]
-- That dictionary contains every non-empty cell  (with ship). Kyes is
coordinates of that cell. Values is a list. Zero-indexed element of this list
contains char '*' if this part of ship is alive, and "X" if it is damaged.
Firs-indexed element of this list is tuple of 2 int's, that means ship size.
The largest number should at index 0 in this tuple. (Example: (4,1)).
        }
    ]
    """
    field = [(10, 10), True, {}]
    free_cells = set([(x, y) for x in range(field[0][0])
                      for y in range(field[0][1])])
    ships = [0, 4, 3, 2, 1]
    for i in range(1, 5):
        for k in range(i):
            placed = False
            rotation = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            while placed is False:
                q = random.randint(0, len(rotation) - 1)
                rotate = rotation[q]
                cells = []
                init_point = random.choice(tuple(free_cells))
                status = True
                for g in range(ships[i]):
                    point = (init_point[0] + g * rotate[0],
                             init_point[1] + g * rotate[1])
                    if point in free_cells:
                        cells.append(point)
                        cells.append(point)
                    else:
                        status = False
                        break
                if status:
                    for cell in cells:
                        for ci in range(-1, 2):
                            for ck in range(-1, 2):
                                try:
                                    free_cells.remove((cell[0] + ci,
                                                       cell[1] + ck))
                                except:
                                    pass
                        field[2][cell] = ["*", (ships[i], 1)]
                    placed = True
    return field
