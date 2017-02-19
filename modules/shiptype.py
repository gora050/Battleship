# class ShipType():
#    def __init__(self, data):
#        if type(data) == str:
#            self.pattern = []
#            self.borders = [[0, 0],[0, 0]]
#            zero = 0
#            lines = data.split("\n")
#            for i in range(len(lines)):
#                for k in range(len(lines[i]))
#                if lines[i][k] == "x":
#                    self.borders[1][0] = max(self.borders[1][0],i)
#                    self.borders[1][1] = max(self.borders[1][1],k)
#                    self.borders[0][0] = min(self.borders[0][0],i)
#                    self.borders[0][1] = min(self.borders[0][1],k)
#                    if zero == 0:
#                        zero = self.zero = (i,k)
#                        self.borders[0] = [i,k]
#                    self.pattern.append((i-zero[0],k-zero[1]))
#        else:
#            return 0
#    def __str__(self):
#        temp = ["".join([" " for x in range(self.max[0]+1)])
#                for y in range(self.max[1]+1)]
#        for cell in self.pattern:
#            temp[cell[0]+self.zero[0]] +
#        return " "
# a = ShipType("****")
# print(a)
