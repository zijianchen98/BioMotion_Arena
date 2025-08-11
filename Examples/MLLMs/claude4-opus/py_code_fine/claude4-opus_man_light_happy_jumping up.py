
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
POINT_RADIUS = 5

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion - Jumping")
clock = pygame.time.Clock()

class BodyJoint:
    def __init__(self, x, y, name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.name = name

# Define 15 body joints for biological motion
def create_body_joints():
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 50
    
    joints = [
        BodyJoint(center_x, center_y - 120, "head"),          # 1
        BodyJoint(center_x, center_y - 90, "neck"),           # 2
        BodyJoint(center_x - 30, center_y - 70, "left_shoulder"), # 3
        BodyJoint(center_x + 30, center_y - 70, "right_shoulder"), # 4
        BodyJoint(center_x - 35, center_y - 30, "left_elbow"),     # 5
        BodyJoint(center_x + 35, center_y - 30, "right_elbow"),    # 6
        BodyJoint(center_x - 40, center_y + 10, "left_hand"),      # 7
        BodyJoint(center_x + 40, center_y + 10, "right_hand"),     # 8
        BodyJoint(center_x, center_y - 40, "spine"),              # 9
        BodyJoint(center_x, center_y + 20, "pelvis"),             # 10
        BodyJoint(center_x - 20, center_y + 20, "left_hip"),       # 11
        BodyJoint(center_x + 20, center_y + 20, "right_hip"),      # 12
        BodyJoint(center_x - 25, center_y + 70, "left_knee"),      # 13
        BodyJoint(center_x + 25, center_y + 70, "right_knee"),     # 14
        BodyJoint(center_x - 30, center_y + 120, "left_foot"),     # 15
        BodyJoint(center_x + 30, center_y + 120, "right_foot")     # 16 (using 15)
    ]
    
    return joints[:15]  # Return exactly 15 joints

def update_jumping_motion(joints, frame):
    # Jumping motion parameters
    jump_duration = 120  # frames for complete jump cycle
    current_phase = (frame % jump_duration) / jump_duration
    
    # Create different phases of jumping
    if current_phase < 0.2:  # Crouch phase
        crouch_factor = current_phase / 0.2
        vertical_offset = -20 * crouch_factor
        knee_bend = 15 * crouch_factor
        arm_raise = -10 * crouch_factor
    elif current_phase < 0.5:  # Jump up phase
        jump_factor = (current_phase - 0.2) / 0.3
        vertical_offset = -20 + 80 * jump_factor  # From crouch to peak
        knee_bend = 15 - 25 * jump_factor  # Straighten legs
        arm_raise = -10 + 30 * jump_factor  # Raise arms
    elif current_phase < 0.8:  # Peak and fall phase
        fall_factor = (current_phase - 0.5) / 0.3
        vertical_offset = 60 - 60 * fall_factor  # Fall down
        knee_bend = -10 + 15 * fall_factor  # Prepare for landing
        arm_raise = 20 - 20 * fall_factor  # Lower arms
    else:  # Landing phase
        land_factor = (current_phase - 0.8) / 0.2
        vertical_offset = -5 * land_factor  # Slight compression
        knee_bend = 5 - 5 * land_factor  # Return to normal
        arm_raise = -5 * land_factor
    
    # Apply motion to each joint
    for i, joint in enumerate(joints):
        joint.x = joint.base_x
        joint.y = joint.base_y + vertical_offset
        
        # Add specific joint movements
        if joint.name in ["left_knee", "right_knee"]:
            joint.y += knee_bend
        elif joint.name in ["left_foot", "right_foot"]:
            joint.y += knee_bend * 1.5
        elif joint.name in ["left_hand", "right_hand"]:
            joint.y += arm_raise
        elif joint.name in ["left_elbow", "right_elbow"]:
            joint.y += arm_raise * 0.7
        
        # Add slight horizontal sway for naturalness
        sway = math.sin(frame * 0.1) * 2
        if joint.name.startswith("left"):
            joint.x += sway
        elif joint.name.startswith("right"):
            joint.x -= sway

def main():
    joints = create_body_joints()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update motion
        update_jumping_motion(joints, frame)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw point-lights
        for joint in joints:
            pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
