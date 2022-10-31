from world.entities import player, follower


class Level():
    
    keys = {
        "w": "██",
        "e": "  ",
        "p": " ♀",
        "f": " Ö",
    }
    world = [[]]
    entities = []
    totalFollowers = 0
    player = None
    complete = False
    exit = False


    def __init__(self, path, icon):
        self.icon = icon

        #loading the file ath the given path
        f = open(path, "r")
        lines = f.readlines()
        x=0
        y=0
        self.world = [["  " for i in lines] for i in range(len(lines[1])-1)]
        for i in range(len(lines)):
            lines[i]=lines[i].replace("\n","")
            for ch in lines[i]:
                if ch == "p":
                    self.player = player.Player(x,y,self.keys["p"])
                    self.world[x][y]=(self.keys["p"])
                elif ch == "f":
                    self.entities.append(follower.Follower(x,y,self.keys["f"]))
                    self.world[x][y]=(self.keys["f"])
                    self.totalFollowers+=1
                else:
                    self.world[x][y]=(self.keys[ch])
                x+=1
            y+=1
            x=0

    def update(self, inp):
        #exiting the level if they push escape
        if(inp == "e"):
            self.exit = True
            return True

        moved = self.player.update(inp,self)

        #updating everthing else if the player can move
        if moved:
            if self.player.getLength() == self.totalFollowers:
                self.complete = True

            for i in self.player.followerQueue:
                i.update(inp, self)

            for i in self.entities:
                if i not in self.player.followerQueue:
                    i.update(inp,self)




        return moved





