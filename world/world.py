from world.worldPlayer import Player
from world.level import Level

class World():
    path = "levels/world.wld"
    keys = {
        "A": " A",
        "D": " D",
        "W": " W",
        "w": " ■",
        "e": "  ",
        "p": " ♀",
        "t": "te",
        "0": " T",
        "1": " 1",
        "2": " 2",
        "3": " 3",
        "4": " 4",
        "5": " A",
        "6": " B",
        "7": " C",
        "8": " D",
        "a": " a",
        "b": " b",
        "c": " c",
        "d": " d",

        "F":" !",
        "E":" W"

    }
    currentLevel = None
    followers = 0
    totalFollowers = 0

    def __init__(self):
        f = open(self.path, "r")
        lines = f.readlines()
        x = 0
        y = 0
        self.world = [["  " for i in lines] for i in range(len(lines[1]) - 1)]
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
            for ch in lines[i]:
                if ch == "p":
                    self.player = Player(x, y, self.keys["p"])
                    self.world[x][y] = (self.keys["p"])
                elif ch in self.keys:
                    self.world[x][y] = (self.keys[ch])
                else:
                    self.world[x][y] =" "+ch
                x += 1
            y += 1
            x = 0

    def update(self, inp):
        # updating the level if one is loaded
        if self.currentLevel is not None:
            moved = self.currentLevel.update(inp)
            #removing the level if it has been completed
            if self.currentLevel.complete and self.currentLevel.exit and inp:
                for i in self.world:
                    if self.currentLevel.icon in i:
                        i[i.index(self.currentLevel.icon)]=self.keys["e"]
                self.totalFollowers+=self.currentLevel.totalFollowers
                self.currentLevel = None
            #exiting the level if the want to exit
            elif self.currentLevel.exit:
                self.currentLevel = None
            return moved

        #moving the player in the overworld
        if(inp=="e"):
            exit()
        level = self.player.update(inp, self)
        #loading the level if the player step on one
        if level !=-1:
            for key,value in self.keys.items():
                if value==level:
                    self.currentLevel = Level("levels/"+key+".lvl",level)




        return True

    def getWorld(self):
        if self.currentLevel is None:
            return self.world
        return self.currentLevel.world
