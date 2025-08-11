
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation control
clock = pygame.time.Clock()
t = 0
dt = 0.05  # Speed adjustment

def calculate_positions(t):
    """Calculate positions for 15 points based on time parameter t"""
    # Base position calculations
    hip_center_x = width//4 + t * 50
    hip_center_y = height//2 + 50 * math.sin(t)
    
    # Head and shoulders
    head_x, head_y = hip_center_x, hip_center_y - 50
    shoulder_l = (head_x - 30, head_y + 30)
    shoulder_r = (head_x + 30, head_y + 30)
    
    # Arms
    elbow_l = (shoulder_l[0], shoulder_l[1] + 40 + 20 * math.sin(2*t))
    elbow_r = (shoulder_r[0], shoulder_r[1] + 40 + 20 * math.sin(2*t))
    hand_l = (elbow_l[0], elbow_l[1] + 30 + 15 * math.sin(2*t + 0.5))
    hand_r = (elbow_r[0], elbow_r[1] + 30 + 15 * math.sin(2*t + 0.5))
    
    # Hips
    hip_l = (hip_center_x - 20, hip_center_y)
    hip_r = (hip_center_x + 20, hip_center_y)
    
    # Legs
    knee_l = (hip_l[0], hip_l[1] + 50 + 30 * math.sin(t + math.pi/2))
    knee_r = (hip_r[0], hip_r[1] + 50 + 30 * math.sin(t + math.pi/2))
    ankle_l = (knee_l[0], knee_l[1] + 50 + 20 * math.sin(t + math.pi))
    ankle_r = (knee_r[0], knee_r[1] + 50 + 20 * math.sin(t + math.pi))
    
    # Torso and neck
    chest = ((shoulder_l[0] + shoulder_r[0])//2, (shoulder_l[1] + hip_center_y)//2)
    neck = (head_x, (head_y + chest[1])//2)
    
    return [
        (head_x, head_y), shoulder_l, shoulder_r,
        elbow_l, elbow_r, hand_l, hand_r,
        hip_l, hip_r, knee_l, knee_r,
        ankle_l, ankle_r, chest, neck
    ]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    points = calculate_positions(t)
    
    # Draw all points
    for x, y in points:
        if 0 <= x <= width and 0 <= y <= height:
            pygame.draw.circle(screen, white, (int(x), int(y)), 5)
    
    pygame.display.flip()
    t += dt
    clock.tick(30)

pygame.quit()
sys.exit()
