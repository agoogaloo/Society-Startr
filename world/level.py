from world.entities import player, follower, sceptic


class Level():
    keys = {
        "w": "██",
        "e": "  ",
        "p": " ♀",
        "pf":" ü",
        "f": " Ö",
        "s": " ö",
    }



    def __init__(self, path, icon):
        self.complete = False
        self.exit = False
        self.undoing = False
        self.path = path
        self.icon = icon

        self.inputs = []
        self.world = [[]]
        self.entities = []
        self.totalFollowers = 0

        #loading the file ath the given path
        f = open(path, "r")
        lines = f.readlines()
        x=0
        y=0
        self.world = [["  " for i in lines] for i in range(len(lines[1])-1)]
        for i in range(len(lines)):
            lines[i]=lines[i].replace("\n","")
            for ch in lines[i]:
                if ch in self.keys:
                    if ch == "p":
                        self.player = player.Player(x,y,self.keys["p"])
                        self.world[x][y]=(self.keys["p"])
                    elif ch == "f":
                        self.entities.append(follower.Follower(x,y,self.keys["f"]))
                        self.world[x][y]=(self.keys["f"])
                        self.totalFollowers+=1
                    elif ch == "s":
                        self.entities.append(sceptic.Sceptic(x,y,self.keys["s"]))
                        self.world[x][y]=(self.keys["s"])
                        self.totalFollowers+=1
                    else:
                        self.world[x][y]=(self.keys[ch])
                else:
                    self.world[x][y] = (" "+ch)
                x+=1
            y+=1
            x=0

    def update(self, inp):
        #exiting the level if they push escape
        if inp == "e":
            self.exit = True
            return True
        #reseting
        print(inp)
        if inp == "x":
            return self.reset()
        #undoing if they push undo
        if inp=="z":
            return self.undo()

        moved = self.player.update(inp,self, self.undoing)

        #updating everthing else if the player can move
        if moved:
            self.inputs.append(inp)
            for i in self.player.followerQueue:
                i.update(inp, self)

            for i in self.entities:
                if i not in self.player.followerQueue:
                    i.update(inp,self)
            if self.complete:
                self.exit = True
            if self.player.getLength(self) == self.totalFollowers:
                self.complete = True
                player.levelComplete()
        return moved

    def reset(self):
        if len(self.inputs) == 0:
            return False
        # resetting the level
        self.__init__(self.path, self.icon)
        return True

    def undo(self):
        inpCopy = [i for i in self.inputs]
        moved = self.reset()
        self.undoing=True
        if not moved:
            return False
        #reinputing every input, except for the last one
        for i in range(len(inpCopy)-1):
            self.update(inpCopy[i])
        self.undoing = False

        return True


