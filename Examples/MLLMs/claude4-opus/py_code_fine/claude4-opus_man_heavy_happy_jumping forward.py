
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 8

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Heavy Man Jumping Forward")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, name, x, y):
        self.name = name
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y

# Define the 15 point-light positions for a human figure (front view)
# Based on typical biological motion capture points
points = [
    PointLight("head", 400, 150),
    PointLight("neck", 400, 200),
    PointLight("left_shoulder", 360, 220),
    PointLight("right_shoulder", 440, 220),
    PointLight("left_elbow", 340, 260),
    PointLight("right_elbow", 460, 260),
    PointLight("left_wrist", 330, 300),
    PointLight("right_wrist", 470, 300),
    PointLight("torso", 400, 280),
    PointLight("left_hip", 380, 340),
    PointLight("right_hip", 420, 340),
    PointLight("left_knee", 375, 420),
    PointLight("right_knee", 425, 420),
    PointLight("left_ankle", 370, 500),
    PointLight("right_ankle", 430, 500)
]

def animate_jumping_forward(time, point):
    # Jump cycle parameters
    jump_duration = 2.0  # seconds for complete jump cycle
    progress = (time % jump_duration) / jump_duration
    
    # Heavy man characteristics - slower, more deliberate movement
    weight_factor = 1.2
    horizontal_speed = 60 * weight_factor
    vertical_amplitude = 80 / weight_factor
    
    # Phase calculations
    if progress < 0.3:  # Preparation phase
        phase = progress / 0.3
        crouch_factor = math.sin(phase * math.pi) * 0.3
    elif progress < 0.7:  # Jump phase
        phase = (progress - 0.3) / 0.4
        crouch_factor = -math.sin(phase * math.pi) * 0.8
    else:  # Landing phase
        phase = (progress - 0.7) / 0.3
        crouch_factor = math.sin(phase * math.pi) * 0.4
    
    # Base position adjustments
    forward_offset = progress * horizontal_speed
    
    # Point-specific animations
    if point.name == "head":
        x = point.base_x + forward_offset
        y = point.base_y + crouch_factor * 15 + math.sin(progress * 2 * math.pi) * 5
        
    elif point.name == "neck":
        x = point.base_x + forward_offset
        y = point.base_y + crouch_factor * 20
        
    elif "shoulder" in point.name:
        side = -1 if "left" in point.name else 1
        x = point.base_x + forward_offset + side * math.sin(progress * 4 * math.pi) * 8
        y = point.base_y + crouch_factor * 25 + math.sin(progress * 2 * math.pi) * 8
        
    elif "elbow" in point.name:
        side = -1 if "left" in point.name else 1
        arm_swing = math.sin(progress * 4 * math.pi + math.pi) * 20
        x = point.base_x + forward_offset + side * arm_swing
        y = point.base_y + crouch_factor * 20 + math.sin(progress * 2 * math.pi) * 12
        
    elif "wrist" in point.name:
        side = -1 if "left" in point.name else 1
        arm_swing = math.sin(progress * 4 * math.pi + math.pi) * 30
        x = point.base_x + forward_offset + side * arm_swing
        y = point.base_y + crouch_factor * 15 + math.sin(progress * 2 * math.pi) * 15
        
    elif point.name == "torso":
        x = point.base_x + forward_offset
        y = point.base_y + crouch_factor * 30
        
    elif "hip" in point.name:
        side = -1 if "left" in point.name else 1
        x = point.base_x + forward_offset + side * math.sin(progress * 2 * math.pi) * 3
        y = point.base_y + crouch_factor * 35
        
    elif "knee" in point.name:
        side = -1 if "left" in point.name else 1
        knee_lift = 0
        if 0.2 < progress < 0.8:  # During jump
            knee_lift = math.sin((progress - 0.2) / 0.6 * math.pi) * 40
        x = point.base_x + forward_offset + side * math.sin(progress * 2 * math.pi) * 5
        y = point.base_y + crouch_factor * 40 - knee_lift
        
    elif "ankle" in point.name:
        side = -1 if "left" in point.name else 1
        foot_lift = 0
        if 0.25 < progress < 0.75:  # During jump
            foot_lift = math.sin((progress - 0.25) / 0.5 * math.pi) * 60
        x = point.base_x + forward_offset + side * math.sin(progress * 2 * math.pi) * 8
        y = point.base_y + crouch_factor * 45 - foot_lift
    
    else:
        x = point.base_x + forward_offset
        y = point.base_y + crouch_factor * 25
    
    # Apply overall vertical movement (jump trajectory)
    if 0.2 < progress < 0.8:
        jump_height = math.sin((progress - 0.2) / 0.6 * math.pi) * vertical_amplitude
        y -= jump_height
    
    return x, y

# Main animation loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Calculate time
    current_time = (pygame.time.get_ticks() - start_time) / 1000.0
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update and draw points
    for point in points:
        x, y = animate_jumping_forward(current_time, point)
        
        # Keep points on screen (wrap around)
        if x > SCREEN_WIDTH + 50:
            point.base_x = -100
            start_time = pygame.time.get_ticks()  # Reset animation
        
        # Draw point
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
