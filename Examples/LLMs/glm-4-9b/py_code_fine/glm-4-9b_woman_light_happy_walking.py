
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the woman's walking motion
.walk_speed = 0.05
.walk_amplitude = 50
.walk_frequency = 2
.num_lights = 15

# Parameters for the point-lights
.light_radius = 3

# Generate initial positions for the point-lights
def generate_light_positions(time):
    positions = []
    for i in range(_num_lights):
        # Assign each light to a specific joint or body part
        # Mapping: 0=left shoulder, 1=right shoulder, 2=left elbow, 3=right elbow,
        # 4=left wrist, 5=right wrist, 6=left hip, 7=right hip, 8=left knee,
        # 9=right knee, 10=left ankle, 11=right ankle, 12=left ear, 13=right ear,
        # 14=nose
        if i < 2:  # Shoulders
            angle = math.sin(time + i * 0.5) * _walk_amplitude * 0.2
            x = WIDTH // 2 + int(math.cos(angle) * 100)
            y = HEIGHT // 4 + int(math.sin(angle) * 20)
        elif i < 4:  # Elbows
            angle = math.sin(time + i * 0.5 + math.pi/4) * _walk_amplitude * 0.3
            x = WIDTH // 2 + int(math.cos(angle) * 80)
            y = HEIGHT // 4 + int(math.sin(angle) * 30)
        elif i < 6:  # Wrists
            angle = math.sin(time + i * 0.5 + math.pi/2) * _walk_amplitude * 0.4
            x = WIDTH // 2 + int(math.cos(angle) * 60)
            y = HEIGHT // 4 + int(math.sin(angle) * 40)
        elif i < 8:  # Hips
            angle = math.sin(time + i * 0.5 + 3*math.pi/4) * _walk_amplitude * 0.5
            x = WIDTH // 2 + int(math.cos(angle) * 40)
            y = HEIGHT // 3 + int(math.sin(angle) * 50)
        elif i < 10:  # Knees
            angle = math.sin(time + i * 0.5 + 5*math.pi/4) * _walk_amplitude * 0.6
            x = WIDTH // 2 + int(math.cos(angle) * 20)
            y = HEIGHT // 3 + int(math.sin(angle) * 60)
        else:  # Ankles, ears, nose
            angle = math.sin(time + i * 0.5 + 7*math.pi/4) * _walk_amplitude * 0.7
            x = WIDTH // 2 + int(math.cos(angle) * 10)
            y = HEIGHT // 3 + int(math.sin(angle) * 70)
        
        positions.append((x, y))
    
    return positions

# Function to draw the happy face
def draw_happy_face(x, y):
    # Draw eyes
    pygame.draw.circle(screen, WHITE, (x - 15, y - 10), 5)
    pygame.draw.circle(screen, WHITE, (x + 15, y - 10), 5)
    
    # Draw smile
    pygame.draw.arc(screen, WHITE, (x - 15, y - 10, 30, 20), math.pi, 2 * math.pi, 2)

# Main loop
clock = pygame.time.Clock()
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Calculate new light positions
    light_positions = generate_light_positions(time)
    
    # Draw the lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, _light_radius)
    
    # Draw a simple representation of a happy woman at the center
    center_x, center_y = WIDTH // 2, HEIGHT // 3
    draw_happy_face(center_x, center_y)
    
    # Update the display
    pygame.display.flip()
    
    # Increment time
    time += _walk_speed
    
    # Control the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
