import pygame
#Sometimes I use BetterComments extension in VS code, that explains why some of my comments start with random symbols

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("No traction?")

# ! All the settings is made for 120 FPS, different FPS will influence the physics od the game (speed, rotation, etc.)
# Initialize STATIC variables
P_WIDTH = 50
P_HEIGHT = 80
MAX_VEL = 3 # Maximum velocity
SLIDE = 0.05  # Is the deceleration while sliding the square
ACCEL = 0.2 # Is the acceleration of the square
ROTATION_SPEED = 2 # Speed of the rotation in degrees

FPS = 120
clock = pygame.time.Clock()


class drift_car(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,max_vel,accel,drag,rotation_speed,):
        super().__init__()
        self.original_car = pygame.image.load("car.png")
        self.original_car = pygame.transform.scale(self.original_car, (width, height))
        self.image = self.original_car
        self.rect = self.image.get_rect()
        self.prev_rect = self.rect
        self.rect.x = x
        self.rect.y = y

        self.max_vel = max_vel
        self.accel = accel
        self.drag = drag
        self.rot_speed = rotation_speed
        self.rot = 0 # 0 degrees is car facing down.
        self.speed = [0,0]
        self.direction = [0,-1] # -1 to 1, depends on direction. Absolute x + y = 1. Default 0 degrees --> x = 0 ; y = -1


    def handle_rot_keys(self, pressed):
        if pressed[pygame.K_a]: # Handling rotation
            self.rot += self.rot_speed
        if pressed[pygame.K_d]:
            self.rot -= self.rot_speed
        if self.rot > 359:
                self.rot -= 360
        elif self.rot < 0:
                self.rot +=360 # End of rotation 
        

        #Angle to direction algorith: y direction first
        if self.rot//90 == 0:
            self.direction[1] = 90 - self.rot%90 # Using the variable for proxy calculations
            self.direction[1] = round(self.direction[1]/90,2)
        elif self.rot//90 == 3:
            self.direction[1] = round((self.rot%90)/90,2)
        if self.rot//90 == 1:
            self.direction[1] = round((self.rot%90)/90,2)
            self.direction[1] = -self.direction[1]
        elif self.rot//90 == 2:
            self.direction[1] = 90 - self.rot%90 # Using the variable for proxy calculations
            self.direction[1] = round(self.direction[1]/90,2) 
            self.direction[1] = -self.direction[1]
        # *Now be basicly now the x, just need to figure out if it is minus or plus
        self.direction[0] = round(1 - abs(self.direction[1]),2)
        if 180 <= self.rot <= 359:
            self.direction[0] *= -1        




    def update(self):
        self.image = pygame.transform.rotozoom(self.original_car, self.rot, 1)
        self.prev_rect = self.rect
        self.rect = self.image.get_rect()
        self.rect.center = self.prev_rect.center


car = drift_car(100,100,P_WIDTH,P_HEIGHT,MAX_VEL,ACCEL,SLIDE,ROTATION_SPEED)
            
car_group = pygame.sprite.Group()
car_group.add(car)    
    
    
# Main game loop
def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle user input
        pressed_keys = pygame.key.get_pressed()
        car.handle_rot_keys(pressed_keys)
        print(car.direction[0], "   ", car.direction[1])

        # Draw the screen
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN,(255,255,255),car.rect)
        car_group.update()
        car_group.draw(WIN)
        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()