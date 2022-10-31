from world.entities.entity import Entity

class Follower(Entity):
    prevDir = "u"
    following = False
    queued = False
    hidden = False



    def update(self, inp, level):
        if self.hidden or self.queued:
            self.hidden = False
            level.world[self.x][self.y] = level.keys["e"]
        #checking if the player is touching them
        left = level.world[self.x-1][self.y]==level.keys["p"]
        right = level.world[self.x+1][self.y] == level.keys["p"]
        up = level.world[self.x][self.y-1] == level.keys["p"]
        down = level.world[self.x][self.y+1] == level.keys["p"]

        #joining the conga line if they are touching and havent already joined
        if (not self.following) and (left or right or up or down):
            self.queued = not level.player.addFollower(self)
            self.following = True
            self.char = " ü"



    def move(self, x,y, level):
        super().move(x,y,level)
        super().follow(level)

    def addFollower(self, follower):
        #this makes the snake thing work
        if not self.nextFollower and follower is not self:
            self.nextFollower = follower
            follower.prevx = self.x
            follower.prevy = self.y
        else:
            self.nextFollower.addFollower(follower)

    def getLength(self):
        if self.nextFollower and not self.hidden:
            return self.nextFollower.getLength() + 1
        else:
            return 0


