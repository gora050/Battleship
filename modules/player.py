from modules.field import Field


class Player():
    def __init__(self, name="", passw=""):
        self.field = Field()
        self.name = name
        while self.name == "":
            self.name = input("Player, please type your name:")
        self.__passw = passw
        while self.__passw == "":
            self.__passw = input(self.name + ", now type your password:")

    def auth(self, passw):
        return True if passw == self.__passw else False

    def read_position(self, passw):
        if passw == self.__passw:
            cell_status = False
            while not cell_status:
                cell = input(self.name + ", choose cell to attack (e.g. A1):")
                if len(cell) in [2, 3] and cell[0] in "ABCDEFGHIJ" and \
                   int(cell[1:]) in range(1, 11):
                    return (int(cell[1]), "ABCDEFGHIJ".index(cell[0]) + 1)
