
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Point-Light Walker")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
clock = pygame.time.Clock()

def calculate_positions(t):
    """Calculate positions of 15 body points at time t"""
    points = []
    
    # Core body points
    head_y = height/4 + 8 * math.sin(2*math.pi*t)
    neck_x, neck_y = width/2, head_y + 20
    torso_x, torso_y = neck_x, neck_y + 60 + 5*math.sin(2*math.pi*t + math.pi/2)
    
    # Hips (phase opposition for natural sway)
    left_hip = (width/2 - 25, torso_y + 15 + 10*math.sin(2*math.pi*t))
    right_hip = (width/2 + 25, torso_y + 15 + 10*math.sin(2*math.pi*t + math.pi))
    
    # Shoulders (counter-sway to hips)
    shoulder_phase = math.pi  # Opposite phase to hips
    left_shoulder = (width/2 - 40, neck_y - 5 + 8*math.sin(2*math.pi*t + shoulder_phase))
    right_shoulder = (width/2 + 40, neck_y - 5 + 8*math.sin(2*math.pi*t + shoulder_phase + math.pi))
    
    # Limbs (arm/leg angles with biomechanical relationships)
    arm_angle = 0.5*math.sin(4*math.pi*t)  # Faster arm swing
    leg_angle = 0.8*math.sin(2*math.pi*t)  # Slower leg movement
    
    # Arms (opposite arm/leg movement)
    left_elbow = (
        left_shoulder[0] + 35*math.cos(arm_angle + math.pi),
        left_shoulder[1] + 35*math.sin(arm_angle + math.pi)
    )
    right_elbow = (
        right_shoulder[0] + 35*math.cos(arm_angle),
        right_shoulder[1] + 35*math.sin(arm_angle)
    )
    
    # Hands (follow elbows with slight phase shift)
    left_hand = (
        left_elbow[0] + 25*math.cos(arm_angle + math.pi/1.5),
        left_elbow[1] + 25*math.sin(arm_angle + math.pi/1.5)
    )
    right_hand = (
        right_elbow[0] + 25*math.cos(arm_angle - math.pi/1.5),
        right_elbow[1] + 25*math.sin(arm_angle - math.pi/1.5)
    )
    
    # Legs (coordinated movement with knee flexion)
    left_knee = (
        left_hip[0] + 40*math.cos(leg_angle),
        left_hip[1] + 40*math.sin(leg_angle)
    )
    right_knee = (
        right_hip[0] + 40*math.cos(leg_angle + math.pi),
        right_hip[1] + 40*math.sin(leg_angle + math.pi)
    )
    
    # Feet (follow knees with phase offset)
    left_foot = (
        left_knee[0] + 40*math.cos(leg_angle + math.pi/2),
        left_knee[1] + 40*math.sin(leg_angle + math.pi/2)
    )
    right_foot = (
        right_knee[0] + 40*math.cos(leg_angle + 3*math.pi/2),
        right_knee[1] + 40*math.sin(leg_angle + 3*math.pi/2)
    )
    
    # Compile all points
    points = [
        (width/2, head_y),         # Head
        (neck_x, neck_y),           # Neck
        left_shoulder,              # Left shoulder
        right_shoulder,             # Right shoulder
        left_elbow,                 # Left elbow
        right_elbow,                # Right elbow
        left_hand,                  # Left hand
        right_hand,                 # Right hand
        left_hip,                   # Left hip
        right_hip,                  # Right hip
        left_knee,                  # Left knee
        right_knee,                 # Right knee
        left_foot,                  # Left foot
        right_foot,                 # Right foot
        (torso_x, torso_y)          # Torso
    ]
    
    return points

# Main animation loop
time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    # Get current positions
    points = calculate_positions(time)
    
    # Draw points
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)
    
    pygame.display.flip()
    time += 1/FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
