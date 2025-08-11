
import pygame
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body points (static)
body_points = [
    (400, 100),    # Head
    (350, 150),    # Left shoulder
    (450, 150),    # Right shoulder
    (400, 150),    # Upper torso
    (400, 300),    # Lower torso
    (350, 300),    # Left hip
    (450, 300),    # Right hip
    (350, 400),    # Left knee
    (450, 400),    # Right knee
    (350, 500),    # Left foot
    (450, 500),    # Right foot
    (325, 175),    # Left elbow (static)
    (300, 200)     # Left hand (static)
]

# Animation parameters
amplitude = 80
speed = 0.05
bend_scale = 0.15
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Calculate dynamic arm positions
    shoulder_x, shoulder_y = 450, 150
    hand_x = shoulder_x + amplitude * math.sin(time)
    hand_y = shoulder_y + 0.3 * amplitude * math.cos(time)
    
    # Calculate elbow position using perpendicular offset
    mid_x = (shoulder_x + hand_x) / 2
    mid_y = (shoulder_y + hand_y) / 2
    dx, dy = hand_x - shoulder_x, hand_y - shoulder_y
    elbow_x = mid_x + (-dy * bend_scale)
    elbow_y = mid_y + (dx * bend_scale)
    
    # Create full point list
    all_points = body_points + [(elbow_x, elbow_y), (hand_x, hand_y)]
    
    # Draw all points
    for point in all_points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)
    
    pygame.display.flip()
    time += speed
    clock.tick(30)

pygame.quit()
