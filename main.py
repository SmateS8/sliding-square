import pygame
import math
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
        self.precise_x = x
        self.precise_y = y


        self.max_vel = max_vel
        self.max_squared = max_vel**2
        self.accel = accel
        self.drag = drag
        self.rot_speed = rotation_speed
        self.rot = 45 # 0 degrees is car facing down.
        self.speed = [0,0]
        self.direction = [0,-1] # -1 to 1, depends on direction. Absolute x + y = 1. Default 0 degrees --> x = 0 ; y = -1


    def handle_rotation(self, pressed):
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



    def handle_forward(self, pressed): #! Something gone wrong. When directions are equaly speeds should be equal too, but they are not
        if pressed[pygame.K_w]:
            #X direction first
            self.speed[0] = self.max_squared * self.direction[0] #Using it as a proxy variable
            if self.speed[0] < 0:
                self.speed[0] = math.sqrt(self.speed[0] * (-1))
                self.speed[0] *= (-1)
            else:
               self.speed[0] = math.sqrt(self.speed[0])
            #Y direction second           
            self.speed[1] = self.max_vel - abs(self.speed[0])
            if self.direction[1] < 0:
                self.speed[1] *= (-1)
            #Y direction second
            #self.speed[1] = self.max_squared * self.direction[1] #Using it as a proxy variable
            #if self.speed[1] < 0:
            #    self.speed[1] = math.sqrt(self.speed[1] * (-1))
            #    self.speed[1] *= (-1)
            #else:
            #    self.speed[1] = math.sqrt(self.speed[1])
        else:
            self.speed = [0,0]


    def update(self):
        #Rotating the image
        self.image = pygame.transform.rotozoom(self.original_car, self.rot, 1)
        self.prev_rect = self.rect
        self.rect = self.image.get_rect()
        self.rect.center = self.prev_rect.center
        #Moving the image
        self.precise_x += self.speed[0]
        self.precise_y += self.speed[1]
        self.rect.centerx = int(self.precise_x)
        self.rect.centery = int(self.precise_y)


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
        car.handle_rotation(pressed_keys)
        car.handle_forward(pressed_keys)


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