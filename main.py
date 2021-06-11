from pgzrun import go
from alien_controller import AlienController


TITLE = "SPACE INVADERS"
WIDTH = 750
HEIGHT = 600


# actors
ship = Actor("ship", (WIDTH//2, HEIGHT - 21))
pips = []
aliens = []
alien_costumes = ["alien1", "alien2", "alien3", "alien4"]
controller = AlienController()


def update(): # built in
    ship_movement()
    update_pips()
    update_aliens()


def draw(): # built in
    screen.fill((0, 0, 0))
    ship.draw()
    for pip in pips:
        pip.draw()
    for alien in aliens:
        alien.draw()


def ship_movement():
    if keyboard[keys.LEFT]:
        if ship.x > 30:
            ship.x -= 5
    elif keyboard[keys.RIGHT]:
        if ship.x < 720:
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


def new_level():
    speed = controller.get_speed()
    controller.set_speed(speed + 1)

    y_spawn = 25
    columns = 0
    
    while columns < 4:
        row_length = 0
        x_spawn = 150
        
        while row_length < 10:
            alien = Actor(alien_costumes[columns], (x_spawn, y_spawn))
            aliens.append(alien)
            row_length += 1
            x_spawn += 50
        
        columns += 1
        y_spawn += 50


def aliens_movement():
    speed = controller.get_speed()
    direction = controller.get_direction()

    for alien in aliens:
        movement = speed * direction
        alien.x += movement
        
        if alien.x <= 20:
            controller.set_direction(1)
            move_aliens_down()
        
        if alien.x >= 730:
            controller.set_direction(-1)
            move_aliens_down()


def move_aliens_down():  
    for alien in aliens:
        alien.y += 10
    aliens_movement()


def collisions():
    
    if len(aliens)>0:
        alien_index = 0
        for alien in aliens:    
            pip_index = 0
            
            for pip in pips:
                if alien.colliderect(pip):
                    aliens.pop(alien_index)
                    pips.pop(pip_index)
                pip_index += 1        
            
            alien_index +=1
    else:
        new_level()   


def update_aliens():
    aliens_movement()
    collisions()


new_level()
go()