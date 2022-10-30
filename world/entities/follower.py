from world.entities.entity import Entity

class Follower(Entity):
    prevDir = "u"
    following = False


    def update(self, inp, level):
        left = level.world[self.x-1][self.y]==level.keys["p"]
        right = level.world[self.x+1][self.y] == level.keys["p"]
        up = level.world[self.x][self.y-1] == level.keys["p"]
        down = level.world[self.x][self.y+1] == level.keys["p"]

        print(self.x,self.y,self.following,left,right,up,down)
        if (not self.following) and (left or right or up or down):
            level.player.addFollower(self)
            self.following = True
            print("found some guy")

    def move(self, x,y, level):
        super().move(x,y,level)
        super().follow(level)

    def addFollower(self, follower):
        if not self.nextFollower and follower is not self:
            self.nextFollower = follower
        else:
            self.nextFollower.addFollower(follower)


