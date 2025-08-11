
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
POINT_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Configuration for point light positions (15 points)
# These coordinates can be adjusted for more realistic representation
point_positions = [
    (WIDTH // 2 - 60, HEIGHT // 2 + 40), 
    (WIDTH // 2 - 40, HEIGHT // 2 + 20),
    (WIDTH // 2 - 20, HEIGHT // 2 + 30),
    (WIDTH // 2, HEIGHT // 2 + 0), 
    (WIDTH // 2 + 20, HEIGHT // 2 + 30),
    (WIDTH // 2 + 40, HEIGHT // 2 + 20),
    (WIDTH // 2 + 60, HEIGHT // 2 + 40),
    (WIDTH // 2 - 60, HEIGHT // 2 + 80),
    (WIDTH // 2 - 40, HEIGHT // 2 + 70),
    (WIDTH // 2 - 20, HEIGHT // 2 + 90),
    (WIDTH // 2, HEIGHT // 2 + 60), 
    (WIDTH // 2 + 20, HEIGHT // 2 + 90),
    (WIDTH // 2 + 40, HEIGHT // 2 + 70),
    (WIDTH // 2 + 60, HEIGHT // 2 + 80),
    (WIDTH // 2 - 40, HEIGHT // 2 + 100),
    (WIDTH // 2 + 40, HEIGHT // 2 + 100)
]

def animate_jump(screen):
    clock = pygame.time.Clock()
    jump_height = 100
    jump_velocity = -5
    y_position = HEIGHT // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Update point lights' vertical position to simulate jump
        y_offset = int(math.sin(pygame.time.get_ticks() / 200) * jump_height)
        
        for position in point_positions:
            x, original_y = position
            pygame.draw.circle(screen, LIGHT_COLOR, (x, original_y + y_offset), 5)

        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Animation of Jumping Sad Woman")
    
    animate_jump(screen)

if __name__ == "__main__":
    main()
