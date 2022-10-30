from world.entities import player, follower


class Level():
    keys = {
        "w": " ■",
        "e": "  ",
        "p": " P",
        "f": " F",
    }
    size = 10
    world = [[]]
    entities = []
    player = None

    def __init__(self, path):
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
                else:
                    self.world[x][y]=(self.keys[ch])
                x+=1
            y+=1
            x=0

    def update(self, inp):
        moved = self.player.update(inp,self)
        for i in self.entities:
            i.update(inp,self)

        return moved





