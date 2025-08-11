
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Number of point-lights and their initial positions
num_points = 15
points = []
point_radius = 2

# Define the initial positions of the points
for i in range(num_points):
    x = WIDTH / 2
    y = HEIGHT / 2 + i * 10
    points.append((x, y))

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus")
clock = pygame.time.Clock()

def wave_hand(points):
    point_pos = [pygame.Vector2(-x + WIDTH/2, -y + HEIGHT/2) for x, y in points]
    
    velocities = [
        point_pos[i].rotate(math.radians(20)).scale(1.0) for i in range(num_points)
    ]
    
    accelerations = [
        (-velocities[i].normalize().scale(0.1)) for i in range(num_points)
    ]

    for i in range(num_points):
        point_pos[i] += velocities[i]
        velocities[i] += accelerations[i]

    return [(point_x + WIDTH/2, point_y + HEIGHT/2) for point_x, point_y in point_pos]

def main():
    running = True
    direction = 1  # 1 means forward, -1 means backward
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        
        points = wave_hand(points)
        for x, y in points:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), point_radius)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
