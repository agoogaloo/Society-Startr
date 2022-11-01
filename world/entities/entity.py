

class Entity():


    def __init__(self,x,y, char):
        self.nextFollower = False
        self.x=x
        self.y=y
        self.prevx = x
        self.prevy = y
        self.char = char

    def update(self, inp, level):
        pass

    def move(self, newx,newy, level):
        if level.world[newx][newy]!=level.keys["e"]:
            return False
        level.world[self.x][self.y] = level.keys["e"]
        level.world[newx][newy] = self.char
        self.prevx = self.x
        self.prevy = self.y
        self.x = newx
        self.y = newy
        return True

    def moveDir(self, direction, level):
        if direction== "u":
            return self.move(self.x,self.y-1,level)
        elif direction== "d":
            return self.move(self.x,self.y+1,level)
        elif direction == "l":
            return self.move(self.x-1,self.y,level)
        elif direction == "r":
            return self.move(self.x+1,self.y,level)

    def follow(self,level):
        if self.nextFollower:
            self.nextFollower.move(self.prevx,self.prevy,level)






