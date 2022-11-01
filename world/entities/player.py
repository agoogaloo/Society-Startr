from world.entities.entity import Entity
from playsound import playsound


def levelComplete():
    pass
    #playsound("sounds/levelComplete.wav", False)


class Player(Entity):

    def __init__(self, x, y, char):
        super().__init__(x, y, char)
        self.followerQueue = []
        self.addedFollower = False
        self.prevDir = "u"

    def update(self, inp, level, undoing):

        moved = self.moveDir(inp, level)
        # only doing things if they can actually move
        if moved:

            self.addedFollower = False
            if len(self.followerQueue) > 0:
                self.addFollower(self.followerQueue[0])
                self.followerQueue[0].hidden = True
                self.followerQueue.pop(0)
            super().follow(level)
            # play sound
            if not undoing:
                #playsound("sounds/move.wav",False)
                pass
        return moved

    def addFollower(self, follower):

        # adding them to the queue if there are more than 1 joining per move
        if self.addedFollower:
            self.followerQueue.append(follower)

            print("queing")
            return False
        # follower.x, follower.y = self.getEndLoc()
        # actually adding the dude
        if not self.nextFollower:
            self.nextFollower = follower

        else:
            self.nextFollower.addFollower(follower)

        follower.queued = False
        self.addedFollower = True

        return True

    def getLength(self, level):
        if self.nextFollower:
            return self.nextFollower.getLength(level) + 1
        else:
            return 0
