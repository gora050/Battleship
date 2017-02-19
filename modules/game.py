from modules.field import Field
from modules.player import Player


class Game():
    def __init__(self):
        self.logo = "\n                      \n                      \n       \
;+''''+;       \n      +;:,,,,:;+      \n     +:,......,:+     \n    +\
;,........,;+    \n    ',..........,'    \n   .;,..........,;.   \n   \
;;,..........,;;   \n   ';:'',....,''::'   \n   ';#@@+....+@@#;'   \n \
  ;;@##@.,,.@##@;;   \n   #;+##',.,,+##+;#   \n   +;,,,,,..,,,,,;+   \
  \n   +;::::,'',::::;+   \n   +';;:::@@:::;;'+   \n    :++;;::::;;++:\
      \n       +';;;;;+       \n       ++';;'++       \n"
        print(chr(27) + "[2J")
        print(self.logo)
        self.players = [Player()]
        print(chr(27) + "[2J")
        print(self.logo)
        self.players.append(Player())
        print(chr(27) + "[2J")
        self.turn = False

    def play(self):
        while (self.players[0].field.alive_ships() > 0 and
               self.players[1].field.alive_ships() > 0):
            passw = ""
            print(chr(27) + "[2J")
            print(self.logo)

            while not self.players[self.turn].auth(passw):
                passw = input(self.players[self.turn].name +
                              ", now is your turn. Type your password to \
continue:")
            print("Your field:\n",
                  self.players[self.turn].field.get_field(True))
            print("Enemy's field:\n",
                  self.players[not self.turn].field.get_field(False))
            res = self.players[not self.turn].\
                field.shoot_at(self.players[self.turn].read_position(passw))
            if res == 0:
                if (self.players[0].field.alive_ships() > 0 and
                   self.players[1].field.alive_ships() > 0):
                    print("Killed!")
                else:
                    print("You WIN!!!\n" * 3)
                    print("Your field:\n",
                          self.players[self.turn].field.get_field(True))
                    print("Enemy's field:\n",
                          self.players[not self.turn].field.get_field(True))
                    print("You WIN!!!\n" * 3)
            elif res > 0:
                print("Hurted!")
            elif res == -2:
                print("You have already shooted there before. Try again")
            else:
                print("Miss shot!")
                self.turn = not self.turn
            input("Press ENTER to continue")
