
"""
This program creates a point‐light animation of a “happy man” 
walking, using exactly 15 white points on a solid black background.
Each point represents a key joint of the human figure. The 15 points are:
  0: Head
  1: Neck
  2: Torso (chest)
  3: Left Shoulder
  4: Right Shoulder
  5: Left Elbow
  6: Right Elbow
  7: Left Hand
  8: Right Hand
  9: Left Hip
 10: Right Hip
 11: Left Knee
 12: Right Knee
 13: Left Foot
 14: Right Foot

The joint positions are computed as functions of time so that the figure appears to walk with a natural-looking gait.
The arms swing in counterphase to the legs.
"""

import sys, math, pygame

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Walking Point-Light Stimulus")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the walking animation
# The horizontal motion of the walker and gait frequencies.
walk_speed = 100   # pixels per second
gait_frequency = 2 * math.pi / 1.5  # one step cycle every 1.5 seconds

# Offsets in the body (in pixels)
HEAD_OFFSET = -50
NECK_OFFSET = -30
SHOULDER_OFFSET_X = 15
HIP_OFFSET_X = 10
HIP_OFFSET_Y = 20

def get_joint_positions(t, base_x, base_y):
    """
    Given time t and the base position (base_x, base_y) of the torso,
    compute and return the positions of the 15 joints as (x, y) tuples.
    The positions are computed with simple sinusoidal modulations to simulate walking.
    """
    # t is in seconds. Trunk position already set from base_x and base_y.
    
    # Compute gait phase. For legs, use cos phases out-of-phase.
    phase = gait_frequency * t

    # Torso (chest)
    torso = (base_x, base_y)

    # Head and Neck (static relative to torso)
    head = (base_x, base_y + HEAD_OFFSET)
    neck = (base_x, base_y + NECK_OFFSET)
    
    # Shoulders positions (left and right)
    left_shoulder = (base_x - SHOULDER_OFFSET_X, base_y + NECK_OFFSET)
    right_shoulder = (base_x + SHOULDER_OFFSET_X, base_y + NECK_OFFSET)
    
    # Arms: use sinusoidal swing, counterbalanced to leg movement.
    # Left arm swings with sin(phase) and right arm swings with opposite phase.
    swing_left = math.sin(phase)
    swing_right = math.sin(phase + math.pi)  # opposite-phase
    
    # Left arm: elbow and hand relative to left shoulder.
    left_elbow = (left_shoulder[0] - 10 * abs(swing_left), left_shoulder[1] + 10 * swing_left)
    left_hand  = (left_shoulder[0] - 20 * abs(swing_left), left_shoulder[1] + 20 * swing_left)
    
    # Right arm: elbow and hand relative to right shoulder.
    right_elbow = (right_shoulder[0] + 10 * abs(swing_left), right_shoulder[1] - 10 * swing_left)
    right_hand  = (right_shoulder[0] + 20 * abs(swing_left), right_shoulder[1] - 20 * swing_left)
    
    # Hips positions (left and right)
    left_hip = (base_x - HIP_OFFSET_X, base_y + HIP_OFFSET_Y)
    right_hip = (base_x + HIP_OFFSET_X, base_y + HIP_OFFSET_Y)
    
    # Legs: Using cosine functions to simulate stepping.
    # Left leg: using phase "phase" and right leg using phase shifted by pi.
    left_knee  = (left_hip[0],
                  left_hip[1] + 10 * math.cos(phase))
    left_foot  = (left_hip[0],
                  left_hip[1] + 20 * math.cos(phase))
    
    right_knee = (right_hip[0],
                  right_hip[1] + 10 * math.cos(phase + math.pi))
    right_foot = (right_hip[0],
                  right_hip[1] + 20 * math.cos(phase + math.pi))
    
    # Return the joints in the specified order (15 points)
    joints = [
        head,            # 0: Head
        neck,            # 1: Neck
        torso,           # 2: Torso (Chest)
        left_shoulder,   # 3: Left Shoulder
        right_shoulder,  # 4: Right Shoulder
        left_elbow,      # 5: Left Elbow
        right_elbow,     # 6: Right Elbow
        left_hand,       # 7: Left Hand
        right_hand,      # 8: Right Hand
        left_hip,        # 9: Left Hip
        right_hip,       # 10: Right Hip
        left_knee,       # 11: Left Knee
        right_knee,      # 12: Right Knee
        left_foot,       # 13: Left Foot
        right_foot       # 14: Right Foot
    ]
    return joints

def main():
    start_time = pygame.time.get_ticks() / 1000.0  # in seconds
    
    running = True
    while running:
        # Manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Calculate elapsed time
        t = pygame.time.get_ticks() / 1000.0 - start_time
        
        # Compute the base horizontal position for the torso.
        # The walker moves from left to right and wraps around.
        base_x = (t * walk_speed) % (SCREEN_WIDTH + 100) - 50  # slight offset offscreen
        base_y = SCREEN_HEIGHT // 2
        
        # Get joint positions
        joints = get_joint_positions(t, base_x, base_y)
        
        # Draw background and points
        screen.fill(BLACK)
        for x, y in joints:
            # Draw a small white circle for each joint.
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()