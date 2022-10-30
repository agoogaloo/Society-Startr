from game import Game
from pynput import keyboard


def on_press(key):
    global game
    print(key)
    try:
        if key.char == 'w':
            game.update("u")
        elif key.char == 's':
            game.update("d")
        elif key.char == "a":
            game.update("l")
        elif key.char == "d":
            game.update("r")
    except AttributeError:
        if key == keyboard.Key.up:
            game.update("u")
        elif key == keyboard.Key.down:
            game.update("d")
        elif key == keyboard.Key.left:
            game.update("l")
        elif key == keyboard.Key.right:
            game.update("r")

    game.drawWorld()


game = Game()



with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
