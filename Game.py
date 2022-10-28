import os

worldSize = 10
px=3
py=3

def update(inp):
    global px
    global py

    if inp== "u":
        py-=1
    elif inp== "d":
        py+=1
    elif inp == "l":
        px -= 1
    elif inp == "r":
        px += 1

def drawWorld():
    #this only clears on windows, I should probably change this later
    os.system('cls')
    print(px,py)
    world = [[" □" for w in range(worldSize)] for h in range(worldSize)]
    world[px][py]=" c"



    for y in range(worldSize):
        for x in range(worldSize):
            print(world[x][y], end="")
        print("")








