
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light figure configuration
JOINT_RADIUS = 5
FPS = 60
TOTAL_JOINTS = 15

# Joint indices
HEAD = 0
NECK = 1
L_SHOULDER = 2
L_ELBOW = 3
L_HAND = 4
R_SHOULDER = 5
R_ELBOW = 6
R_HAND = 7
HIP_CENTER = 8
L_HIP = 9
L_KNEE = 10
L_FOOT = 11
R_HIP = 12
R_KNEE = 13
R_FOOT = 14

# Standing pose (x, y coordinates)
standing_pose = [
    (400, 150),  # Head
    (400, 200),  # Neck
    (380, 200),  # Left Shoulder
    (360, 240),  # Left Elbow
    (340, 290),  # Left Hand
    (420, 200),  # Right Shoulder
    (440, 240),  # Right Elbow
    (460, 290),  # Right Hand
    (400, 350),  # Hip Center
    (380, 350),  # Left Hip
    (380, 420),  # Left Knee
    (380, 500),  # Left Foot
    (420, 350),  # Right Hip
    (420, 420),  # Right Knee
    (420, 500)   # Right Foot
]

# Animation parameters
MAX_BOW_ANGLE = math.radians(60)  # 60 degrees in radians
LOWER_BODY_DROP = 50  # Pixels to drop lower body
CYCLE_FRAMES = 120  # Total frames for a full bow cycle
ARM_SWING_RANGE = 20  # Arm swing range during bow

# Clock for controlling frame rate
clock = pygame.time.Clock()

def rotate_point(point, center, angle):
    """Rotate a point around a center by a given angle."""
    px, py = point
    cx, cy = center
    dx = px - cx
    dy = py - cy
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    new_x = cx + dx * cos_angle + dy * sin_angle
    new_y = cy + dy * cos_angle - dx * sin_angle
    return (new_x, new_y)

def animate_bow(frame):
    """Calculate joint positions for the current animation frame."""
    phase = frame % CYCLE_FRAMES
    cycle_progress = phase / CYCLE_FRAMES
    
    # Calculate current bow angle (0 to max and back)
    if cycle_progress < 0.5:
        bow_progress = 2 * cycle_progress
    else:
        bow_progress = 2 * (1 - cycle_progress)
    
    bow_angle = MAX_BOW_ANGLE * bow_progress
    
    # Calculate arm swing angle
    arm_swing = math.sin(2 * math.pi * cycle_progress) * ARM_SWING_RANGE
    
    # Initialize pose as standing position
    current_pose = list(standing_pose)
    hip_center = standing_pose[HIP_CENTER]
    
    # Apply dynamic changes to joint positions
    # Head and neck (more movement during bow)
    for joint in [HEAD, NECK]:
        current_pose[joint] = rotate_point(
            standing_pose[joint], 
            hip_center,
            bow_angle * 1.2
        )
    
    # Shoulders
    current_pose[L_SHOULDER] = (
        standing_pose[L_SHOULDER][0] - arm_swing * 0.3,
        standing_pose[L_SHOULDER][1] + arm_swing * 0.1
    )
    current_pose[R_SHOULDER] = (
        standing_pose[R_SHOULDER][0] + arm_swing * 0.3,
        standing_pose[R_SHOULDER][1] + arm_swing * 0.1
    )
    
    # Arms (pendulum motion during bow)
    current_pose[L_ELBOW] = rotate_point(
        (standing_pose[L_ELBOW][0] - arm_swing, standing_pose[L_ELBOW][1]),
        current_pose[L_SHOULDER],
        bow_angle * 0.5
    )
    current_pose[R_ELBOW] = rotate_point(
        (standing_pose[R_ELBOW][0] + arm_swing, standing_pose[R_ELBOW][1]),
        current_pose[R_SHOULDER],
        bow_angle * 0.5
    )
    current_pose[L_HAND] = rotate_point(
        (standing_pose[L_HAND][0] - arm_swing * 1.5, standing_pose[L_HAND][1]),
        current_pose[L_ELBOW],
        bow_angle * 0.3
    )
    current_pose[R_HAND] = rotate_point(
        (standing_pose[R_HAND][0] + arm_swing * 1.5, standing_pose[R_HAND][1]),
        current_pose[R_ELBOW],
        bow_angle * 0.3
    )
    
    # Lower body adjustments (slight drop and knee bend during bow)
    for joint in [HIP_CENTER, L_HIP, R_HIP, L_KNEE, R_KNEE, L_FOOT, R_FOOT]:
        x, y = standing_pose[joint]
        # Add drop proportional to bow progress
        current_pose[joint] = (x, y + bow_progress * LOWER_BODY_DROP)
    
    # Hip center follows neck trajectory
    hip_dx = current_pose[NECK][0] - standing_pose[NECK][0]
    hip_dy = current_pose[NECK][1] - standing_pose[NECK][1]
    current_pose[HIP_CENTER] = (
        standing_pose[HIP_CENTER][0] + hip_dx * 0.7,
        standing_pose[HIP_CENTER][1] + hip_dy * 0.5 + bow_progress * LOWER_BODY_DROP
    )
    
    return current_pose

# Main animation loop
def main():
    frame_counter = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        
        # Calculate current pose
        current_pose = animate_bow(frame_counter)
        
        # Draw all point-light joints
        for joint in current_pose:
            pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), JOINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame_counter += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
