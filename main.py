import pygame
# Using 'Better Comments' extension in VS Code
# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Square!")


# Initialize game objects and variables
P_WIDTH = 20
P_HEIGHT = 20
P_COLOR = (255,0,0)
Player = pygame.Rect(WIDTH/2 - P_WIDTH/2, HEIGHT/2 - P_HEIGHT/2 ,P_WIDTH, P_HEIGHT) # Sets Rectangle in the middle of the screen
MAX_VEL = 3 # Maximum velocity
SLIDE = 0.025  # Is the deceleration while sliding the square
ACCEL = 0.1 # Is the acceleration of the square

speed = [0,0] # X speed, Y speed

FPS = 120
clock = pygame.time.Clock()

# Handling everything about speeeeeeeeed!
def update_player_velocity(pressed):
    # Handling acceleration
    if pressed[pygame.K_w]:
        if speed[1] > -MAX_VEL:
            if speed[1] - ACCEL >= -MAX_VEL:
                speed[1] -= ACCEL
            else:
                speed[1] = -MAX_VEL
    if pressed[pygame.K_s]:
        if speed[1] < MAX_VEL:
            if speed[1] + ACCEL <= MAX_VEL:
                speed[1] += ACCEL
            else:
                speed[1] = MAX_VEL
    if pressed[pygame.K_a]:
        if speed[0] > -MAX_VEL:
            speed[0] -= ACCEL
    if pressed[pygame.K_d]:
        if speed[0] < MAX_VEL:
            speed[0] += ACCEL
    # Handling deceleration
     
    if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
        if speed[1] != 0:
            if speed[1] > 0:
                if speed[1] - SLIDE >= 0:
                    speed[1] -= SLIDE
                else:
                    speed[1] = 0
            elif speed[1] < 0:
                if speed[1] + SLIDE <= 0:
                    speed[1] += SLIDE
                else:
                    speed[1] = 0   
    if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
            if speed[0] > 0:
                if speed[0] - SLIDE >= 0:
                    speed[0] -= SLIDE
                else:
                    speed[0] = 0
            elif speed[0] < 0:
                if speed[0] + SLIDE <= 0:
                    speed[0] += SLIDE
                else:
                    speed[0] = 0  

    print(speed)    
    


            
    
    
    
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
        update_player_velocity(pressed_keys)
        # Update game objects and variables
        # ...

        # Draw the screen
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, P_COLOR, Player)
        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()