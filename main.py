from pgzrun import go
from random import randrange, randint


TITLE = "SPACE INVADERS"
WIDTH = 800
HEIGHT = 600


# actors
ship = Actor("ship", (WIDTH//2, HEIGHT - 21))
pips = []
aliens = []
alien_costumes = ["alien1", "alien2", "alien3", "alien4"]


def update(): # built in
    ship_movement()
    update_pips()


def draw(): # built in
    screen.fill((0, 0, 0))
    ship.draw()
    for pip in pips:
        pip.draw()
    for alien in aliens:
        alien.draw()


def ship_movement():
    if keyboard[keys.LEFT]:
        if ship.x > 25:
            ship.x -= 5
    elif keyboard[keys.RIGHT]:
        if ship.x < 775:
            ship.x += 5


def on_key_down(key): # built in
    if key == key.SPACE:
        pips.append(Actor("pip", (ship.x, ship.y - 15)))

    
def update_pips():
    index = 0
    for pip in pips:
        pip.y -= 10
        if pip.y < 0:
            pips.pop(index)
        index += 1


def spawn_aliens():
    y_spawn = 75
    columns = 0
    while columns < 4:
        row_length = 0
        x_spawn = 175
        while row_length < 10:
            alien = Actor(alien_costumes[columns], (x_spawn, y_spawn))
            aliens.append(alien)
            row_length += 1
            x_spawn += 50
        columns += 1
        y_spawn += 50


spawn_aliens()
go()