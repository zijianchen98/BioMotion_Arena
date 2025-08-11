
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
NUM_LIGHTS = 15

# Man's initial position and size
man_x, man_y = WIDTH // 2, HEIGHT // 2
man_radius = 30

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Function to calculate point-light positions for sitting animation
def calculate_light_positions(frame):
    lights = []
    
    # Head
    lights.append((man_x, man_y - man_radius - 20))
    
    # Shoulders
    shoulder_offset = 15
    lights.append((man_x - shoulder_offset, man_y - man_radius))
    lights.append((man_x + shoulder_offset, man_y - man_radius))
    
    # Arms
    arm_length = 40
    arm_angle = math.radians(90)  # Adjust angle for more natural motion
    lights.append((man_x - shoulder_offset - arm_length * math.cos(arm_angle), man_y - man_radius + arm_length * math.sin(arm_angle)))
    lights.append((man_x + shoulder_offset + arm_length * math.cos(arm_angle), man_y - man_radius + arm_length * math.sin(arm_angle)))
    
    # Body
    body_height = 60
    lights.append((man_x, man_y))
    
    # Hips
    hip_offset = 10
    lights.append((man_x - hip_offset, man_y + man_radius))
    lights.append((man_x + hip_offset, man_y + man_radius))
    
    # Legs
    leg_length = 60
    leg_angle = math.radians(45)  # Adjust angle for more natural motion
    lights.append((man_x - hip_offset - leg_length * math.cos(leg_angle), man_y + man_radius + leg_length * math.sin(leg_angle)))
    lights.append((man_x + hip_offset - leg_length * math.cos(leg_angle), man_y + man_radius + leg_length * math.sin(leg_angle)))
    
    # Ankle and foot (simplified)
    ankle_offset = 5
    lights.append((man_x - hip_offset - leg_length * math.cos(leg_angle) - ankle_offset, man_y + man_radius + leg_length * math.sin(leg_angle) + 10))
    lights.append((man_x + hip_offset - leg_length * math.cos(leg_angle) - ankle_offset, man_y + man_radius + leg_length * math.sin(leg_angle) + 10))
    
    return lights

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    light_positions = calculate_light_positions(frame)
    
    for x, y in light_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    
    pygame.display.flip()
    
    frame += 1
    clock.tick(FPS)

pygame.quit()
sys.exit()
