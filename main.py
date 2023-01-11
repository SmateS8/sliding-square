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
VEL = 3

FPS = 120
clock = pygame.time.Clock()

# Handling movement of the Player
def handle_movements(pressed):
    if pressed[pygame.K_w]:
        Player.y -= VEL
    if pressed[pygame.K_s]:
        Player.y += VEL
    if pressed[pygame.K_a]:
        Player.x -= VEL
    if pressed[pygame.K_d]:
        Player.x += VEL
    
    
    
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
        handle_movements(pressed_keys)
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