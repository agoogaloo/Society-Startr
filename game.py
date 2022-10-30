import os
from world.level import Level
from world.entities.player import  Player

class Game():
    lev = Level("levels/testLevel.lvl")


    def update(self, inp):
        return self.lev.update(inp)

    def drawWorld(self):
        world = self.lev.world
        #this only clears on windows, I should probably change this later
        os.system('cls')


        for y in range(len(world)):
            for x in range(len(world[y])):
                print(self.lev.world[x][y], end="")
            print("")








