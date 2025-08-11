
"""
This program creates a point‐light stimulus animation that depicts a heavy, sad woman running.
It uses exactly 15 white “joints” drawn as circles on a solid black background.
The 15 joints represent:

  0. Head
  1. Left Shoulder
  2. Right Shoulder
  3. Torso (Chest)
  4. Pelvis (Center)
  5. Left Hip
  6. Right Hip
  7. Left Knee
  8. Right Knee
  9. Left Ankle
 10. Right Ankle
 11. Left Elbow
 12. Right Elbow
 13. Left Wrist
 14. Right Wrist

Their positions are computed from a “base” position that moves horizontally at a constant speed (to simulate running)
and from small periodic (sinusoidal) offsets that simulate the natural swing of arms and legs – typical of running.
A slight “droop” (adjusted offsets) gives a sad, heavy‐laden posture.
Natural “bob” is added to most joints.
The animation runs at 60 frames per second.
"""

import sys, math, pygame

# Initialize Pygame
pygame.init()

# Window size and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Heavy Sad Woman Running")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Animation parameters
speed = 100  # horizontal speed in pixels per second
base_y = HEIGHT // 2  # vertical center for the figure

# These functions return joint positions (x,y) relative to the current base position.
# The figure’s posture is “slumped” to suggest sadness and heaviness.
# The running cycle is controlled by theta = 2*pi*t.
def compute_joint_positions(t):
    # Running cycle phase (1 cycle per second)
    theta = 2 * math.pi * t

    # bob: a slight up-and-down oscillation, smaller amplitude for a heavy gait
    bob = 3 * math.sin(2 * theta)

    # Overall horizontal movement (wrap around so the figure stays visible)
    base_x = (WIDTH//2 + speed * t) % (WIDTH + 200) - 100  # extra margin for smooth wrapping

    # Base offsets for body parts (relative to base_x, base_y)
    # Adopt a slumped posture for a sad, weighted look.
    head_offset     = (0, -55 + bob)
    lshoulder_offset= (-15, -35 + bob)
    rshoulder_offset= (15, -35 + bob)
    torso_offset    = (0, -15 + bob)
    pelvis_offset   = (0, 0 + bob)
    lhip_offset     = (-10, 0 + bob)
    rhip_offset     = (10, 0 + bob)
    
    # Leg swing: left and right legs move out of phase (phase difference pi)
    # Knee swing parameters:
    knee_horiz_amp = 10
    knee_vert_amp  = 5
    # Ankle swing parameters:
    ankle_horiz_amp = 15
    ankle_vert_amp  = 5

    # Arms swing: again using sine for natural oscillation;
    # arms swing opposite to the leg on the same side.
    arm_horiz_amp = 15

    # Compute positions by adding base_x, base_y to each offset.
    joints = [None] * 15

    # 0. Head
    joints[0] = (base_x + head_offset[0], base_y + head_offset[1])
    
    # 1. Left Shoulder
    joints[1] = (base_x + lshoulder_offset[0], base_y + lshoulder_offset[1])
    
    # 2. Right Shoulder
    joints[2] = (base_x + rshoulder_offset[0], base_y + rshoulder_offset[1])
    
    # 3. Torso (Chest)
    joints[3] = (base_x + torso_offset[0], base_y + torso_offset[1])
    
    # 4. Pelvis (Center)
    joints[4] = (base_x + pelvis_offset[0], base_y + pelvis_offset[1])
    
    # 5. Left Hip (a little to the left of pelvis)
    joints[5] = (base_x + lhip_offset[0], base_y + lhip_offset[1])
    
    # 6. Right Hip (a little to the right of pelvis)
    joints[6] = (base_x + rhip_offset[0], base_y + rhip_offset[1])
    
    # 7. Left Knee: base position from left hip plus running swing offsets
    left_knee_x = base_x - 10 + knee_horiz_amp * math.sin(theta)
    left_knee_y = base_y + 20 + bob + knee_vert_amp * math.cos(theta)
    joints[7] = (left_knee_x, left_knee_y)
    
    # 8. Right Knee: base from right hip, phase shifted by pi (opposite swing)
    right_knee_x = base_x + 10 + knee_horiz_amp * math.sin(theta + math.pi)
    right_knee_y = base_y + 20 + bob + knee_vert_amp * math.cos(theta + math.pi)
    joints[8] = (right_knee_x, right_knee_y)
    
    # 9. Left Ankle: base position from left hip lower down, plus swing offsets
    left_ankle_x = base_x - 10 + ankle_horiz_amp * math.sin(theta)
    left_ankle_y = base_y + 40 + bob + ankle_vert_amp * math.cos(theta)
    joints[9] = (left_ankle_x, left_ankle_y)
    
    # 10. Right Ankle: similar to right, with phase shift
    right_ankle_x = base_x + 10 + ankle_horiz_amp * math.sin(theta + math.pi)
    right_ankle_y = base_y + 40 + bob + ankle_vert_amp * math.cos(theta + math.pi)
    joints[10] = (right_ankle_x, right_ankle_y)
    
    # 11. Left Elbow: based on left shoulder (fixed offset for simplicity)
    left_elbow = (base_x - 25, base_y -15 + bob)
    joints[11] = left_elbow
    
    # 12. Right Elbow: based on right shoulder
    right_elbow = (base_x + 25, base_y -15 + bob)
    joints[12] = right_elbow
    
    # 13. Left Wrist: further out from left elbow with an arm-swing exponent (opposite to right leg motion)
    left_wrist_x = base_x - 35 + arm_horiz_amp * math.sin(theta + math.pi)
    left_wrist_y = base_y + 5 + bob
    joints[13] = (left_wrist_x, left_wrist_y)
    
    # 14. Right Wrist: further out from right elbow with arm swing (in phase with right leg)
    right_wrist_x = base_x + 35 + arm_horiz_amp * math.sin(theta)
    right_wrist_y = base_y + 5 + bob
    joints[14] = (right_wrist_x, right_wrist_y)

    return joints

# Main loop
def main():
    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        # Event handling – allow the user to quit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute elapsed time in seconds.
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Fill background with black.
        screen.fill(BLACK)

        # Compute joint positions for current time.
        joints = compute_joint_positions(t)
        
        # Draw each joint as a white filled circle (point-light).
        for pos in joints:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 3)

        # Update the display.
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()