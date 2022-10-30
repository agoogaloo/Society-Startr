from game import Game
from pynput import keyboard


def on_press(key):
    global game
    print(key)
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
    except AttributeError:
        if key == keyboard.Key.up:
            inp ="u"
        elif key == keyboard.Key.down:
            inp ="d"
        elif key == keyboard.Key.left:
            inp ="l"
        elif key == keyboard.Key.right:
            inp ="r"


    if inp!="" and game.update(inp):
        game.drawWorld()


game = Game()



with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
