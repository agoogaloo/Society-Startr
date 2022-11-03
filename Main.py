import os

from game import Game
from pynput import keyboard


def on_press(key):
    global game
    inp = ""
    try:
        if key.char == 'w':
            inp ="u"
        elif key.char == 's':
            inp = "d"
        elif key.char == "a":
            inp ="l"
        elif key.char == "d":
            inp ="r"
        elif key.char == "z":
            inp ="z"
        elif key.char == "r":
            inp = "x"
    except AttributeError:
        if key == keyboard.Key.up:
            inp ="u"
        elif key == keyboard.Key.down:
            inp ="d"
        elif key == keyboard.Key.left:
            inp ="l"
        elif key == keyboard.Key.right:
            inp ="r"
        elif key == keyboard.Key.esc:
            inp ="e"

    if inp!="" and game.update(inp):
        game.drawWorld()


print("""
    Thank you for purchasing your own secret society starter kit! 
    You will find included robes, candles, and a brand new Society Startr™, 
    self cleaning altar (patent pending). 
    Enter a name for your secret society below, or upgrade to a premium membership
    for a Society Startr™, secret society naming guide.

      --Enter Name--""")

name = input()
os.system('cls')
print("""
    Congratulations, you are now the supreme leader of your very own secret society! 
    Upgrade to a premium membership now to receive 10 loyal followers, 
    or press enter to begin collecting followers on your own*
    
    *self recruited members do not carry a Society Startr Secrecy Guarantee. 
    Society Startr Inc. accepts no liability for betrayal, disloyalty, mutiny, 
    or other nefarious acts committed by self collected followers.


      --Press Enter To Start--""")
input()

game = Game(name)
game.drawWorld()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
