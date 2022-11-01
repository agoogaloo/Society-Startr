from world.entities.follower import Follower

class Sceptic(Follower):

    def __init__(self,x,y,char):
        super().__init__(x,y,char)
        self.changed = False

    def update(self, inp, level):
        if not self.changed and level.player.getLength(level)>=1:
            self.changed =True
            self.char = level.keys["f"]
            level.world[self.x][self.y]=self.char
        if(self.changed):
            super().update(inp,level)
