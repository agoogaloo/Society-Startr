from world.entities.entity import Entity

class Player (Entity):
    char = " P"
    pass

    def update(self, inp, level):
        print(self.x,self.y)
        self.move(inp,level)

