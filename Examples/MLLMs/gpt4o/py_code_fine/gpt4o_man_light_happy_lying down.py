
import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion - Lying Down")

# Frame rate
clock = pygame.time.Clock()

# Define body parts
points = {
    "head": [WIDTH // 2, HEIGHT // 2 - 100],
    "shoulders_left": [WIDTH // 2 - 50, HEIGHT // 2 - 70],
    "shoulders_right": [WIDTH // 2 + 50, HEIGHT // 2 - 70],
    "elbow_left": [WIDTH // 2 - 70, HEIGHT // 2 - 50],
    "elbow_right": [WIDTH // 2 + 70, HEIGHT // 2 - 50],
    "hip_left": [WIDTH // 2 - 50, HEIGHT // 2 - 30],
    "hip_right": [WIDTH // 2 + 50, HEIGHT // 2 - 30],
    "hand_left": [WIDTH // 2 - 90, HEIGHT // 2 - 20],
    "hand_right": [WIDTH // 2 + 90, HEIGHT // 2 - 20],
    "knee_left": [WIDTH // 2 - 70, HEIGHT // 2 + 10],
    "knee_right": [WIDTH // 2 + 70, HEIGHT // 2 + 10],
    "foot_left": [WIDTH // 2 - 90, HEIGHT // 2 + 50],
    "foot_right": [WIDTH // 2 + 90, HEIGHT // 2 + 50],
    "torso": [WIDTH // 2, HEIGHT // 2 - 50]
}

# Animation variables
angle = 0
angular_speed = 0.05

# Function to simulate motion
def update_point_motion():
    global angle
    
    for key in ["elbow_left", "elbow_right", "hand_left", "hand_right", "knee_left", "knee_right", "foot_left", "foot_right"]:
        initial_x, initial_y = points[key]
        direction = -1 if "left" in key else 1
        
        points[key][0] = initial_x + direction * math.sin(angle) * 20
        points[key][1] = initial_y + math.cos(angle) * 10

    angle += angular_speed

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update motion
        update_point_motion()

        # Draw
        screen.fill(BLACK)
        
        for position in points.values():
            pygame.draw.circle(screen, WHITE, position, 5)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
