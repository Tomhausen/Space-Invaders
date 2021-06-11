class AlienController: 
    # other option would be to instantiate a sprite that sits off screen and handles this
    
    def __init__(self):
        self.direction = 1
        self.speed = 0


    def get_direction(self):
        return self.direction


    def get_speed(self):
        return self.speed


    def set_direction(self, direction):
        self.direction = direction


    def set_speed(self, speed):
        self.speed = speed
