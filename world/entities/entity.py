

class Entity():
    char = " F"
    x = 0
    y = 0

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def update(self, inp, level):
        pass

    def move(self, direction, level):
        newx = self.x
        newy = self.y
        if direction== "u":
            newy-=1
        elif direction== "d":
            newy+=1
        elif direction == "l":
            newx -= 1
        elif direction == "r":
            newx += 1

        if level.world[newx][newy]==level.keys["e"]:
            level.world[self.x][self.y] = level.keys["e"]
            level.world[newx][newy] = self.char
            self.x = newx
            self.y = newy



