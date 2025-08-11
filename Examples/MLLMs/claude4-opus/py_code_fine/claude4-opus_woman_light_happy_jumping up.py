
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Animation parameters
frame = 0
jump_duration = 60  # frames for complete jump cycle

# Joint positions representing a human figure (15 points)
# Based on standard biological motion capture points
joint_names = [
    "head", "neck", "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow", "left_wrist", "right_wrist",
    "spine", "left_hip", "right_hip",
    "left_knee", "right_knee", "left_ankle", "right_ankle"
]

# Base positions (standing pose) - normalized coordinates
base_positions = {
    "head": (0.0, -0.4),
    "neck": (0.0, -0.3),
    "left_shoulder": (-0.15, -0.25),
    "right_shoulder": (0.15, -0.25),
    "left_elbow": (-0.25, -0.1),
    "right_elbow": (0.25, -0.1),
    "left_wrist": (-0.3, 0.05),
    "right_wrist": (0.3, 0.05),
    "spine": (0.0, -0.1),
    "left_hip": (-0.1, 0.1),
    "right_hip": (0.1, 0.1),
    "left_knee": (-0.12, 0.35),
    "right_knee": (0.12, 0.35),
    "left_ankle": (-0.1, 0.6),
    "right_ankle": (0.1, 0.6)
}

def get_jump_offset(frame_num, duration):
    """Calculate vertical offset for jumping motion"""
    t = (frame_num % duration) / duration * 2 * math.pi
    # Smooth jumping motion using sine wave
    jump_height = -abs(math.sin(t)) * 0.3
    return jump_height

def get_joint_positions(frame_num):
    """Calculate animated joint positions for jumping motion"""
    positions = {}
    
    # Calculate jump phase
    jump_phase = (frame_num % jump_duration) / jump_duration * 2 * math.pi
    jump_offset = get_jump_offset(frame_num, jump_duration)
    
    # Phase of the jump for different body parts
    leg_bend = max(0, math.sin(jump_phase)) * 0.15
    arm_swing = math.sin(jump_phase) * 0.1
    
    for joint in joint_names:
        base_x, base_y = base_positions[joint]
        x, y = base_x, base_y + jump_offset
        
        # Add specific animations for different body parts
        if joint in ["left_knee", "right_knee"]:
            # Bend knees during jump preparation and landing
            y -= leg_bend
            
        elif joint in ["left_ankle", "right_ankle"]:
            # Feet follow knee bending
            y -= leg_bend * 1.2
            
        elif joint in ["left_wrist", "right_wrist"]:
            # Arm swinging motion
            y += arm_swing
            if "left" in joint:
                x += arm_swing * 0.5
            else:
                x -= arm_swing * 0.5
                
        elif joint in ["left_elbow", "right_elbow"]:
            # Elbow movement complementary to wrists
            y += arm_swing * 0.5
            
        # Convert to screen coordinates
        screen_x = int(WIDTH/2 + x * 300)
        screen_y = int(HEIGHT/2 + y * 300)
        
        positions[joint] = (screen_x, screen_y)
    
    return positions

def draw_points(positions):
    """Draw the 15 point-lights on screen"""
    for joint in joint_names:
        x, y = positions[joint]
        pygame.draw.circle(screen, WHITE, (x, y), 8)

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Get current joint positions
    current_positions = get_joint_positions(frame)
    
    # Draw the biological motion stimulus
    draw_points(current_positions)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate and increment frame counter
    clock.tick(FPS)
    frame += 1
    
    # Reset frame counter to avoid overflow
    if frame >= jump_duration * 100:
        frame = 0

pygame.quit()
sys.exit()
