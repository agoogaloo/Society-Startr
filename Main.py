import Game
from pynput import keyboard

def on_press(key):
    print(key)
    try:
        if key.char == 'w':
            Game.update("u")
        elif key.char == 's':
            Game.update("d")
        elif key.char == "a":
            Game.update("l")
        elif key.char == "d":
            Game.update("r")
    except AttributeError:
        if key == keyboard.Key.up:
            Game.update("u")
        elif key == keyboard.Key.down:
            Game.update("d")
        elif key == keyboard.Key.left:
            Game.update("l")
        elif key == keyboard.Key.right:
            Game.update("r")

    Game.drawWorld()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
