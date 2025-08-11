
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Woman Jumping")
clock = pygame.time.Clock()

class JointPoint:
    def __init__(self, x, y, name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.name = name

# Define 15 key body points for biological motion
joints = [
    JointPoint(400, 150, "head"),           # 0 - head
    JointPoint(400, 180, "neck"),           # 1 - neck
    JointPoint(380, 210, "left_shoulder"),  # 2 - left shoulder
    JointPoint(420, 210, "right_shoulder"), # 3 - right shoulder
    JointPoint(370, 250, "left_elbow"),     # 4 - left elbow
    JointPoint(430, 250, "right_elbow"),    # 5 - right elbow
    JointPoint(360, 290, "left_hand"),      # 6 - left hand
    JointPoint(440, 290, "right_hand"),     # 7 - right hand
    JointPoint(400, 280, "torso"),          # 8 - torso center
    JointPoint(380, 340, "left_hip"),       # 9 - left hip
    JointPoint(420, 340, "right_hip"),      # 10 - right hip
    JointPoint(370, 420, "left_knee"),      # 11 - left knee
    JointPoint(430, 420, "right_knee"),     # 12 - right knee
    JointPoint(360, 500, "left_foot"),      # 13 - left foot
    JointPoint(440, 500, "right_foot")      # 14 - right foot
]

def update_jump_motion(frame, joints):
    # Jump cycle parameters
    cycle_length = 120  # frames per jump cycle
    phase = (frame % cycle_length) / cycle_length * 2 * math.pi
    
    # Heavy weight jumping motion - slower, more effort
    jump_height = 80 * max(0, math.sin(phase)) if phase < math.pi else 0
    
    # Additional vertical displacement for different body parts
    torso_lift = jump_height * 0.8
    head_lift = jump_height * 0.9
    arm_lift = jump_height * 0.7
    leg_compression = 30 * max(0, math.cos(phase)) if phase < math.pi else 0
    
    # Heavy motion characteristics
    effort_factor = 1.2
    sway_amplitude = 15 * effort_factor
    arm_swing = 25 * effort_factor
    
    # Body sway and effort
    sway = math.sin(phase) * sway_amplitude
    arm_effort = math.sin(phase * 2) * arm_swing
    
    # Update head
    joints[0].x = joints[0].base_x + sway * 0.5
    joints[0].y = joints[0].base_y - head_lift
    
    # Update neck
    joints[1].x = joints[1].base_x + sway * 0.6
    joints[1].y = joints[1].base_y - torso_lift
    
    # Update shoulders
    joints[2].x = joints[2].base_x + sway * 0.7 - arm_effort * 0.3
    joints[2].y = joints[2].base_y - arm_lift
    joints[3].x = joints[3].base_x + sway * 0.7 + arm_effort * 0.3
    joints[3].y = joints[3].base_y - arm_lift
    
    # Update elbows (swinging motion)
    joints[4].x = joints[4].base_x + sway * 0.8 - arm_effort
    joints[4].y = joints[4].base_y - arm_lift * 0.8
    joints[5].x = joints[5].base_x + sway * 0.8 + arm_effort
    joints[5].y = joints[5].base_y - arm_lift * 0.8
    
    # Update hands
    joints[6].x = joints[6].base_x + sway * 0.9 - arm_effort * 1.2
    joints[6].y = joints[6].base_y - arm_lift * 0.6
    joints[7].x = joints[7].base_x + sway * 0.9 + arm_effort * 1.2
    joints[7].y = joints[7].base_y - arm_lift * 0.6
    
    # Update torso
    joints[8].x = joints[8].base_x + sway * 0.8
    joints[8].y = joints[8].base_y - torso_lift
    
    # Update hips
    joints[9].x = joints[9].base_x + sway * 0.9
    joints[9].y = joints[9].base_y - jump_height * 0.6
    joints[10].x = joints[10].base_x + sway * 0.9
    joints[10].y = joints[10].base_y - jump_height * 0.6
    
    # Update knees (compression and extension)
    knee_bend = leg_compression if phase < math.pi else -20
    joints[11].x = joints[11].base_x + sway
    joints[11].y = joints[11].base_y + knee_bend - jump_height * 0.4
    joints[12].x = joints[12].base_x + sway
    joints[12].y = joints[12].base_y + knee_bend - jump_height * 0.4
    
    # Update feet
    foot_lift = jump_height * 0.2 if phase > math.pi * 0.3 and phase < math.pi * 0.7 else 0
    joints[13].x = joints[13].base_x + sway * 1.1
    joints[13].y = joints[13].base_y + leg_compression * 0.5 - foot_lift
    joints[14].x = joints[14].base_x + sway * 1.1
    joints[14].y = joints[14].base_y + leg_compression * 0.5 - foot_lift

def draw_points(screen, joints):
    for joint in joints:
        pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), 5)

# Main animation loop
frame = 0
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
    
    # Update joint positions
    update_jump_motion(frame, joints)
    
    # Draw points
    draw_points(screen, joints)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    frame += 1

pygame.quit()
sys.exit()
