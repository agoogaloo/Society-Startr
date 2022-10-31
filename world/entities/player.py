from world.entities.entity import Entity

class Player (Entity):

    followerQueue = []
    addedFollower = False

    prevDir = "u"



    def update(self, inp, level):

        moved = self.moveDir(inp,level)
        #only doing things if they can actually move
        if moved:
            self.addedFollower = False
            if len(self.followerQueue)>0:
                self.addFollower(self.followerQueue[0])
                self.followerQueue[0].hidden=True
                self.followerQueue.pop(0)
            super().follow(level)
        return moved



    def addFollower(self, follower):

        #adding them to the queue if there are more than 1 joining per move
        if self.addedFollower:
            self.followerQueue.append(follower)

            print("queing")
            return False

        print("adding char")

        #follower.x, follower.y = self.getEndLoc()
        #actually adding the dude
        if not self.nextFollower:
            self.nextFollower = follower

        else:
            self.nextFollower.addFollower(follower)

        follower.queued=False
        self.addedFollower = True
        return True

    def getLength(self):
        if self.nextFollower:
            return self.nextFollower.getLength()+1
        else:
            return 0





