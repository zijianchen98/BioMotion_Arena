
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping Forward")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define 15 joint points for human body
joints = [
    PointLight(WIDTH//2, HEIGHT//2 - 120, "head"),
    PointLight(WIDTH//2, HEIGHT//2 - 100, "neck"),
    PointLight(WIDTH//2 - 30, HEIGHT//2 - 80, "left_shoulder"),
    PointLight(WIDTH//2 + 30, HEIGHT//2 - 80, "right_shoulder"),
    PointLight(WIDTH//2 - 45, HEIGHT//2 - 40, "left_elbow"),
    PointLight(WIDTH//2 + 45, HEIGHT//2 - 40, "right_elbow"),
    PointLight(WIDTH//2 - 60, HEIGHT//2 - 10, "left_hand"),
    PointLight(WIDTH//2 + 60, HEIGHT//2 - 10, "right_hand"),
    PointLight(WIDTH//2, HEIGHT//2 - 60, "torso"),
    PointLight(WIDTH//2, HEIGHT//2 - 20, "pelvis"),
    PointLight(WIDTH//2 - 20, HEIGHT//2 + 40, "left_hip"),
    PointLight(WIDTH//2 + 20, HEIGHT//2 + 40, "right_hip"),
    PointLight(WIDTH//2 - 25, HEIGHT//2 + 100, "left_knee"),
    PointLight(WIDTH//2 + 25, HEIGHT//2 + 100, "right_knee"),
    PointLight(WIDTH//2 - 30, HEIGHT//2 + 160, "left_foot"),
    PointLight(WIDTH//2 + 30, HEIGHT//2 + 160, "right_foot")
]

# Animation variables
frame = 0
jump_cycle = 120  # frames for complete jump cycle

def update_jumping_motion(frame):
    global joints
    
    # Normalize frame to 0-1 cycle
    t = (frame % jump_cycle) / jump_cycle
    
    # Jump phases: prepare (0-0.3), takeoff (0.3-0.4), flight (0.4-0.7), landing (0.7-1.0)
    
    # Vertical displacement for whole body (parabolic jump)
    if t < 0.3:  # Preparation
        crouch_factor = math.sin(t / 0.3 * math.pi) * 0.3
        y_offset = crouch_factor * 40
        forward_offset = 0
    elif t < 0.4:  # Takeoff
        takeoff_t = (t - 0.3) / 0.1
        y_offset = -takeoff_t * 20
        forward_offset = takeoff_t * 10
    elif t < 0.7:  # Flight
        flight_t = (t - 0.4) / 0.3
        jump_height = math.sin(flight_t * math.pi) * 80
        y_offset = -jump_height
        forward_offset = 10 + flight_t * 40
    else:  # Landing
        land_t = (t - 0.7) / 0.3
        y_offset = -10 + land_t * 10
        forward_offset = 50 + land_t * 20
    
    # Update each joint with specific biomechanical motion
    for i, joint in enumerate(joints):
        base_x = joint.base_x
        base_y = joint.base_y
        
        # Apply global forward movement and vertical jump
        joint.x = base_x + forward_offset
        joint.y = base_y + y_offset
        
        # Joint-specific motion patterns
        if joint.joint_name == "head":
            # Head follows body with slight lag
            joint.y += math.sin(t * math.pi * 2) * 3
            
        elif "shoulder" in joint.joint_name:
            # Shoulders swing opposite to leg motion
            swing = math.sin(t * math.pi * 4) * 15
            if "left" in joint.joint_name:
                joint.x += swing
            else:
                joint.x -= swing
                
        elif "elbow" in joint.joint_name:
            # Arms bend more during preparation and landing
            arm_bend = math.sin(t * math.pi * 2) * 20
            if "left" in joint.joint_name:
                joint.x += arm_bend
                joint.y += abs(arm_bend) * 0.5
            else:
                joint.x -= arm_bend
                joint.y += abs(arm_bend) * 0.5
                
        elif "hand" in joint.joint_name:
            # Hands follow arms with more swing
            hand_swing = math.sin(t * math.pi * 4) * 25
            if "left" in joint.joint_name:
                joint.x += hand_swing
            else:
                joint.x -= hand_swing
                
        elif "hip" in joint.joint_name:
            # Hips rotate slightly during jump
            hip_rotation = math.sin(t * math.pi * 2) * 5
            if "left" in joint.joint_name:
                joint.x -= hip_rotation
            else:
                joint.x += hip_rotation
                
        elif "knee" in joint.joint_name:
            # Knees bend significantly during preparation and landing
            if t < 0.3 or t > 0.7:
                knee_bend = math.sin((t if t < 0.3 else (t - 0.7)) / 0.3 * math.pi) * 30
                joint.y -= knee_bend
            else:  # During flight, knees pull up
                knee_lift = math.sin((t - 0.3) / 0.4 * math.pi) * 40
                joint.y -= knee_lift
                
        elif "foot" in joint.joint_name:
            # Feet follow knee motion with ankle flexion
            if t < 0.3 or t > 0.7:
                foot_bend = math.sin((t if t < 0.3 else (t - 0.7)) / 0.3 * math.pi) * 35
                joint.y -= foot_bend
            else:
                foot_lift = math.sin((t - 0.3) / 0.4 * math.pi) * 50
                joint.y -= foot_lift
                # Foot angle during flight
                foot_angle = math.sin((t - 0.3) / 0.4 * math.pi) * 10
                if "left" in joint.joint_name:
                    joint.x -= foot_angle
                else:
                    joint.x += foot_angle

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update animation
    update_jumping_motion(frame)
    frame += 1
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw point lights
    for joint in joints:
        pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), POINT_RADIUS)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
