from pgzrun import go
from random import randrange, randint
from pygame import Rect


TITLE = "SPACE INVADERS"
WIDTH = 600
HEIGHT = 450


ship = Actor("ship", (WIDTH//2, HEIGHT - 21))
pips = []


def update(): # built in
    key_press()
    print(len(pips))
    update_pips()


def draw(): # built in
    screen.blit("background", (0, 0))
    ship.draw()
    for pip in pips:
        pip.draw()


def key_press():
    if keyboard[keys.LEFT]:
        ship.x -= 5
    elif keyboard[keys.RIGHT]:
        ship.x += 5


def on_key_down(key): # built in
    if key == key.SPACE:
        pips.append(Actor("pip", (ship.x, ship.y)))

    
def update_pips():
    index = 0
    for pip in pips:
        pip.y -= 10
        if pip.y < 0:
            pips.pop(index)    
        index += 1


go()