import pygame
# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("No traction?")


# Initialize STATIC variables
P_WIDTH = 50
P_HEIGHT = 80
MAX_VEL = 3 # Maximum velocity
SLIDE = 0.05  # Is the deceleration while sliding the square
ACCEL = 0.2 # Is the acceleration of the square
ROTATION_SPEED = 2 # Speed of the rotation in degrees

FPS = 15
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
        self.rot = 0
        self.speed = [0,0]


    def rotate(self, pressed):
        if pressed[pygame.K_a]:
            pass

    def do_movement(self,pressed):
        pass


    def update(self):
        if self.rot > 359:
            self.rot -= 360
        self.image = pygame.transform.rotozoom(self.original_car, self.rot, 1)
        self.prev_rect = self.rect
        self.rect = self.image.get_rect()
        self.rect.center = self.prev_rect.center
        self.rot += 1


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
        pygame.draw.rect(WIN,(255,255,255),car.rect)
        car_group.update()
        car_group.draw(WIN)
        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()