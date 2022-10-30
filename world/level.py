from world.entities import player


class Level():
    keys = {
        "w": " ■",
        "e": " □",
        "p": " ▣",
    }
    size = 10
    world = [[]]
    entities = []

    def __init__(self, path):
        f = open(path, "r")
        lines = f.readlines()
        x=0
        y=0
        for i in range(len(lines)):
            self.world.append([])
            lines[i]=lines[i].replace("\n","")
            for ch in lines[i]:
                if ch == "p":
                    self.entities.append(player.Player(x,y))
                    self.world[i].append(self.keys["e"])
                else:
                    self.world[i].append(self.keys[ch])
                x+=1
            y+=1
            x=0

    def update(self, inp):
        print(self.entities)
        for i in self.entities:

            i.update(inp,self)





