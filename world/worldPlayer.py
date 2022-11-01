from playsound import playsound


class Player ():
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def move(self, newx,newy, level):
        if level.world[newx][newy]==level.keys["w"]:
            return -1
        elif level.world[newx][newy]!=level.keys["e"]:
            return level.world[newx][newy]
        level.world[self.x][self.y] = level.keys["e"]
        level.world[newx][newy] = self.char
        self.x = newx
        self.y = newy

        return -1


    def update(self, direction, level):
        #playsound("sounds/move.wav",False)
        if direction== "u":
            return self.move(self.x,self.y-1,level)
        elif direction== "d":
            return self.move(self.x,self.y+1,level)
        elif direction == "l":
            return self.move(self.x-1,self.y,level)
        elif direction == "r":
            return self.move(self.x+1,self.y,level)








