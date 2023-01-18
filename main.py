import pygame
# Using 'Better Comments' extension in VS Code
# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Square!")


# Initialize game objects and variables
P_WIDTH = 50
P_HEIGHT = 80
MAX_VEL = 3 # Maximum velocity
SLIDE = 0.05  # Is the deceleration while sliding the square
ACCEL = 0.2 # Is the acceleration of the square
ROTATION_SPEED = 2 # Speed of the rotation in degrees
speed = [0,0] # X speed, Y speed

FPS = 120
clock = pygame.time.Clock()


class drift_car(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,max_vel,accel,drag,rotation_speed,):
        super().__init__()
        self.original_car = pygame.image.load("car.png")
        self.original_car = pygame.transform.scale(self.original_car, (width, height))
        self.car = self.original_car
        self.x = x
        self.y = y

        self.max_vel = max_vel
        self.accel = accel
        self.drag = drag
        self.rot_speed = rotation_speed
        self.rot = 0
        self.speed = [0,0]

        
    def rotate(self, pressed):
        if pressed[pygame.K_a]:
            pass

    def do_movement(self,pressed):
        pass


    def update(self):
        WIN.blit(self.car, (self.x, self.y))


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



        # Draw the screen
        WIN.fill((0, 0, 0))
        
        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()