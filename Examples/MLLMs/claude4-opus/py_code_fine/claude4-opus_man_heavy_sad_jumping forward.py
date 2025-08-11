
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Heavy Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class JointPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_x = x
        self.base_y = y

# Define 15 key joints for human figure
joints = [
    JointPoint(400, 100),   # 0: Head
    JointPoint(400, 150),   # 1: Neck
    JointPoint(400, 200),   # 2: Chest/upper torso
    JointPoint(400, 280),   # 3: Waist
    JointPoint(400, 320),   # 4: Hip center
    JointPoint(370, 200),   # 5: Left shoulder
    JointPoint(430, 200),   # 6: Right shoulder
    JointPoint(350, 250),   # 7: Left elbow
    JointPoint(450, 250),   # 8: Right elbow
    JointPoint(340, 300),   # 9: Left hand
    JointPoint(460, 300),   # 10: Right hand
    JointPoint(380, 380),   # 11: Left knee
    JointPoint(420, 380),   # 12: Right knee
    JointPoint(370, 450),   # 13: Left foot
    JointPoint(430, 450),   # 14: Right foot
]

def update_jumping_motion(frame, joints):
    # Heavy jumping motion with slower, more labored movement
    time = frame * 0.08  # Slower animation for heavy movement
    
    # Jump phases: crouch -> takeoff -> air -> landing
    jump_cycle = time % (2 * math.pi)
    
    # Vertical displacement for jumping (reduced for heavy person)
    if jump_cycle < math.pi * 0.3:  # Crouch phase (longer)
        crouch_factor = 0.3 * (1 - math.cos(jump_cycle / 0.3))
        jump_height = 0
    elif jump_cycle < math.pi * 0.8:  # Takeoff and air phase
        jump_progress = (jump_cycle - math.pi * 0.3) / (0.5 * math.pi)
        jump_height = 40 * math.sin(jump_progress * math.pi)  # Reduced jump height
        crouch_factor = 0.3 * (1 - jump_progress)
    else:  # Landing phase
        land_progress = (jump_cycle - math.pi * 0.8) / (1.2 * math.pi)
        jump_height = 0
        crouch_factor = 0.2 * land_progress
    
    # Forward movement (slower for heavy person)
    forward_offset = time * 15  # Slower forward movement
    
    # Apply transformations to each joint
    for i, joint in enumerate(joints):
        # Reset to base position
        x, y = joint.base_x, joint.base_y
        
        # Apply forward movement
        x += forward_offset
        
        # Apply vertical jump movement
        y -= jump_height
        
        # Apply crouching (compress vertically)
        if i >= 3:  # Lower body joints
            y += crouch_factor * (i - 2) * 5
        
        # Add specific joint movements for realism
        if i == 0:  # Head - slight bobbing
            y += math.sin(time * 4) * 3
        elif i in [5, 6]:  # Shoulders - arm swinging (reduced for heavy movement)
            arm_swing = math.sin(time * 3 + (math.pi if i == 6 else 0)) * 8
            x += arm_swing * 0.3  # Reduced arm movement
        elif i in [7, 8]:  # Elbows
            elbow_bend = math.sin(time * 3 + (math.pi if i == 8 else 0)) * 15
            if i == 7:  # Left elbow
                x += elbow_bend * 0.4 - 10
                y += abs(elbow_bend) * 0.3
            else:  # Right elbow
                x += elbow_bend * 0.4 + 10
                y += abs(elbow_bend) * 0.3
        elif i in [9, 10]:  # Hands
            hand_swing = math.sin(time * 3 + (math.pi if i == 10 else 0)) * 20
            if i == 9:  # Left hand
                x += hand_swing * 0.5 - 15
                y += abs(hand_swing) * 0.4
            else:  # Right hand
                x += hand_swing * 0.5 + 15
                y += abs(hand_swing) * 0.4
        elif i in [11, 12]:  # Knees - bending motion
            knee_bend = math.sin(time * 4) * 8 + crouch_factor * 15
            y += knee_bend
            if jump_cycle > math.pi * 0.3 and jump_cycle < math.pi * 0.8:
                # Knees up during jump
                y -= 15
        elif i in [13, 14]:  # Feet
            foot_lift = 0
            if jump_cycle > math.pi * 0.3 and jump_cycle < math.pi * 0.8:
                # Feet up during jump
                foot_lift = 25 + math.sin(time * 6) * 5
            y -= foot_lift
            
            # Foot placement for running motion
            stride = math.sin(time * 4 + (math.pi if i == 14 else 0)) * 10
            x += stride
        
        # Update joint position with screen wrapping
        joint.x = x % WIDTH
        joint.y = y

def main():
    running = True
    frame = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update motion
        update_jumping_motion(frame, joints)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw joints as white circles
        for joint in joints:
            pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), 4)
        
        # Update display
        pygame.display.flip()
        clock.tick(30)  # Slower frame rate for heavy movement
        frame += 1
    
    pygame.quit()

if __name__ == "__main__":
    main()
