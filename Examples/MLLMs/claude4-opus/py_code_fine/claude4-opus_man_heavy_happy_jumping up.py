
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping Human")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.name = name

# Define 15 body joint points based on human anatomy
# Coordinates are relative to center of mass
joints = [
    PointLight(0, -60, "head"),           # 0
    PointLight(0, -30, "neck"),           # 1
    PointLight(0, 0, "torso_center"),     # 2
    PointLight(-20, -10, "left_shoulder"), # 3
    PointLight(20, -10, "right_shoulder"), # 4
    PointLight(-35, 10, "left_elbow"),     # 5
    PointLight(35, 10, "right_elbow"),     # 6
    PointLight(-50, 30, "left_hand"),      # 7
    PointLight(50, 30, "right_hand"),      # 8
    PointLight(-15, 30, "left_hip"),       # 9
    PointLight(15, 30, "right_hip"),       # 10
    PointLight(-18, 80, "left_knee"),      # 11
    PointLight(18, 80, "right_knee"),      # 12
    PointLight(-20, 130, "left_foot"),     # 13
    PointLight(20, 130, "right_foot")      # 14
]

# Animation parameters
frame = 0
cycle_length = 120  # frames for complete jump cycle
center_x = WIDTH // 2
center_y = HEIGHT // 2

def update_jump_animation(frame, joints):
    # Normalize frame to 0-1 cycle
    t = (frame % cycle_length) / cycle_length
    
    # Jump phases: crouch (0-0.2), takeoff (0.2-0.4), air (0.4-0.8), landing (0.8-1.0)
    
    # Vertical displacement for center of mass
    if t < 0.2:  # Crouch phase
        crouch_factor = 1 - (t / 0.2) * 0.3
        vertical_offset = 50 * (1 - crouch_factor)
    elif t < 0.4:  # Takeoff phase
        takeoff_t = (t - 0.2) / 0.2
        vertical_offset = 50 - 120 * takeoff_t
    elif t < 0.8:  # Air phase
        air_t = (t - 0.4) / 0.4
        vertical_offset = -70 + 30 * math.sin(air_t * math.pi)
    else:  # Landing phase
        land_t = (t - 0.8) / 0.2
        vertical_offset = -40 + 90 * land_t
    
    # Update each joint
    for i, joint in enumerate(joints):
        # Reset to base position
        x, y = joint.base_x, joint.base_y
        
        # Apply phase-specific modifications
        if t < 0.2:  # Crouch
            crouch_factor = t / 0.2
            if joint.name in ["left_knee", "right_knee"]:
                y -= 20 * crouch_factor
                x *= 1 + 0.2 * crouch_factor
            elif joint.name in ["left_foot", "right_foot"]:
                y -= 30 * crouch_factor
            elif joint.name in ["left_hip", "right_hip"]:
                y += 10 * crouch_factor
            elif joint.name in ["left_hand", "right_hand"]:
                y -= 15 * crouch_factor
                
        elif t < 0.4:  # Takeoff
            takeoff_t = (t - 0.2) / 0.2
            if joint.name in ["left_knee", "right_knee"]:
                y += 40 * takeoff_t
            elif joint.name in ["left_foot", "right_foot"]:
                y += 20 * takeoff_t
            elif joint.name in ["left_hand", "right_hand"]:
                y -= 25 * takeoff_t
                x *= 1 + 0.3 * takeoff_t
                
        elif t < 0.8:  # Air phase
            air_t = (t - 0.4) / 0.4
            if joint.name in ["left_knee", "right_knee"]:
                y += 30 * math.sin(air_t * math.pi)
            elif joint.name in ["left_foot", "right_foot"]:
                y += 15 * math.sin(air_t * math.pi)
            elif joint.name in ["left_hand", "right_hand"]:
                y -= 20
                x *= 1.2
                
        else:  # Landing
            land_t = (t - 0.8) / 0.2
            if joint.name in ["left_knee", "right_knee"]:
                y -= 15 * land_t
                x *= 1 + 0.15 * land_t
            elif joint.name in ["left_foot", "right_foot"]:
                y -= 20 * land_t
            elif joint.name in ["left_hand", "right_hand"]:
                y += 20 * land_t
                x *= 1.2 - 0.2 * land_t
        
        # Add slight bob and sway for realism
        bob = 3 * math.sin(t * 2 * math.pi)
        sway = 2 * math.sin(t * 4 * math.pi)
        
        # Apply transformations
        joint.x = center_x + x + sway
        joint.y = center_y + y + vertical_offset + bob

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update animation
    update_jump_animation(frame, joints)
    
    # Draw point lights
    for joint in joints:
        pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), 4)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    frame += 1

pygame.quit()
sys.exit()
