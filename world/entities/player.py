from world.entities.entity import Entity

class Player (Entity):

    followers = 0
    followerQueue = 0
    prevDir = "u"



    def update(self, inp, level):

        moved = self.moveDir(inp,level)
        if moved:
            super().follow(level)
        return moved



    def addFollower(self, follower):
        print(self.nextFollower, follower)
        if not self.nextFollower:
            self.nextFollower = follower
        else:
            self.nextFollower.addFollower(follower)

        self.followers+=1


