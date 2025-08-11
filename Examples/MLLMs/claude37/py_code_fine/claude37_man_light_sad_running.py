
import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions (15 points)
points = [
    (400, 100), (370, 130), (430, 130), # Head
    (350, 160), (450, 160), # Shoulders
    (320, 200), (400, 200), (480, 200), # Arms
    (360, 280), (440, 280), # Hips
    (350, 400), (400, 400), (450, 400), # Legs
    (370, 480), (430, 480), # Feet
]

# Running motion parameters
frame_count = 60
run_cycle = 2 * math.pi  # One complete cycle
fps = 30

def animate_running():
    clock = pygame.time.Clock()
    
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)

        # Calculate the positions of the point lights for the running animation
        for i, (x, y) in enumerate(points):
            # Apply a simple sine wave for vertical movement to simulate running
            if i <= 2:  # Head points
                offset = 20 * math.sin(run_cycle * (frame / frame_count))
            elif i <= 5:  # Shoulder points
                offset = 10 * math.sin(run_cycle * (frame / (frame_count - 10)))
            elif i <= 8:  # Arm points
                offset = 5 * math.sin(run_cycle * (frame / (frame_count - 20)))
            elif i <= 11:  # Hip points
                offset = 15 * math.sin(run_cycle * (frame / (frame_count - 30)))
            else:  # Leg and foot points
                offset = 25 * math.sin(run_cycle * (frame / (frame_count - 40)))
            
            pygame.draw.circle(screen, WHITE, (x, y + int(offset)), 5)

        pygame.display.flip()
        frame += 1
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    animate_running()
