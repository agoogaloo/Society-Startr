import os
from world.world import World
from world.entities.player import  Player

class Game():
    world = World()

    def __init__(self, name):
        self.name = name
        #"   "+"═"*(len(name)+2)
        self.info = ["  ║ "+name.upper()+" ║","   "+"═"*(len(name)+2),"   -members:",]


    def update(self, inp):

        return self.world.update(inp)

    def drawWorld(self):
        world = self.world.getWorld()
        #this only clears on windows, I should probably change this later
        os.system('cls')
        print("\n")
        for y in range(len(world[1])):
            print("   ",end="")
            for x in range(len(world)):
                print(world[x][y], end="")
            if(y<len(self.info)):
                print(self.info[y],end="")
                if y == 2:
                    mems, maxMem = self.getMembers()
                    print(str(mems)+"/"+str(maxMem),end="")
            print("")

        print("  ║ wasd/arrows→move    ║")
        print("  ║ z→undo move         ║")
        print("  ║ esc→exit level/game ║")
        print("   ═════════════════════")


    def getMembers(self):
        members = 0
        maxMembers = 0
        if self.world.currentLevel is None:
            members=self.world.totalFollowers
            maxMembers = 10
        else:
            members = self.world.currentLevel.player.getLength()
            maxMembers = self.world.currentLevel.totalFollowers
        return members,maxMembers











