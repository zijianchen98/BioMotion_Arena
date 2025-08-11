
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forward Rolling Motion")
clock = pygame.time.Clock()

# Define the 15 body joints for point-light display
# Based on standard biomechanical model
joint_names = [
    "head", "neck", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
    "left_wrist", "right_wrist", "spine", "left_hip", "right_hip",
    "left_knee", "right_knee", "left_ankle", "right_ankle"
]

def forward_roll_motion(frame, total_frames):
    """Generate positions for forward rolling motion"""
    
    # Rolling parameters
    roll_progress = frame / total_frames
    angle = roll_progress * 2 * math.pi  # One complete roll
    
    # Center of mass movement (parabolic trajectory during roll)
    center_x = WIDTH // 2 + (roll_progress - 0.5) * 200
    center_y = HEIGHT // 2 - abs(math.sin(angle * 0.5)) * 50
    
    # Body orientation during roll
    body_angle = angle
    
    # Define relative joint positions (in body-centered coordinates)
    # These represent a person in tucked position during forward roll
    base_positions = {
        "head": (0, -25),
        "neck": (0, -15),
        "left_shoulder": (-15, -10),
        "right_shoulder": (15, -10),
        "left_elbow": (-25, 0),
        "right_elbow": (25, 0),
        "left_wrist": (-30, 10),
        "right_wrist": (30, 10),
        "spine": (0, 0),
        "left_hip": (-10, 15),
        "right_hip": (10, 15),
        "left_knee": (-15, 35),
        "right_knee": (15, 35),
        "left_ankle": (-10, 45),
        "right_ankle": (10, 45)
    }
    
    # Apply rotation and translation
    positions = {}
    for joint, (rel_x, rel_y) in base_positions.items():
        # Rotate relative to body angle
        rotated_x = rel_x * math.cos(body_angle) - rel_y * math.sin(body_angle)
        rotated_y = rel_x * math.sin(body_angle) + rel_y * math.cos(body_angle)
        
        # Translate to world coordinates
        world_x = center_x + rotated_x
        world_y = center_y + rotated_y
        
        positions[joint] = (world_x, world_y)
    
    return positions

def main():
    running = True
    frame = 0
    total_frames = 120  # 4 seconds at 30 FPS
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    frame = 0  # Reset animation
        
        # Clear screen
        screen.fill(BLACK)
        
        # Get current frame positions
        positions = forward_roll_motion(frame, total_frames)
        
        # Draw point lights
        for joint_name in joint_names:
            x, y = positions[joint_name]
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        
        # Advance frame
        frame = (frame + 1) % total_frames
        
        # Control frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
