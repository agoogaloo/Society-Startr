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
   Welcome to the secret society starting service! 
   We guarantee you your own personal 
   secret society, or your money back!

   Now, what do you want to name your secret society?

      --Enter Name--""")

name = input()

print("""
   Excellent! tell you now have a secret society, so my job is done.
   If you some followers you'll need to go and get them yourself.


      --Press Enter To Start--""")
input()

game = Game(name)
game.drawWorld()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
