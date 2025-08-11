
import pygame
import sys
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
POINT_COUNT = 15
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Point-Light Animation: Sadman Lying Down')
clock = pygame.time.Clock()

# Define point light positions for a sadman lying down
def get_point_positions(frame):
    # Base positions for a sadman
    point_positions = []
    base_y = SCREEN_HEIGHT // 2
    for i in range(POINT_COUNT):
        # Distributing points linearly for the sadman
        if i < POINT_COUNT // 3:  # Head
            x = SCREEN_WIDTH // 2 + math.sin(frame / 20) * 5
            y = base_y - 50 - i * 10
        elif i < 2 * POINT_COUNT // 3:  # Torso
            x = SCREEN_WIDTH // 2 + math.sin(frame / 20) * 5
            y = base_y + (i - POINT_COUNT // 3) * 10
        else:  # Legs
            x = SCREEN_WIDTH // 2 + math.sin(frame / 20) * 10
            y = base_y + (i - 2 * POINT_COUNT // 3) * 10

        point_positions.append((x, y))
    
    return point_positions

def draw_points(point_positions):
    for pos in point_positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

# Main loop
frame = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BACKGROUND_COLOR)
    
    # Get point positions based on the current frame
    point_positions = get_point_positions(frame)

    # Draw point lights
    draw_points(point_positions)

    # Update display
    pygame.display.flip()
    
    # Increment frame count
    frame += 1
    
    # Control the frame rate
    clock.tick(FPS)
