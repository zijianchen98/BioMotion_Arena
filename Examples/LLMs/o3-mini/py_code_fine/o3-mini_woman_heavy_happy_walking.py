
"""
This program uses Pygame to render an animation of a point‐light stimulus that
depicts the biological movement of a “happy, heavy‐set woman” walking.
The animation uses exactly 15 white dots (point‐lights) on a solid black background.
The positions of the dots are computed in each frame to simulate a biomechanically plausible walking motion.
"""

import sys, math, pygame

# Initialize Pygame.
pygame.init()

# Window dimensions.
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock to manage frame rate.
clock = pygame.time.Clock()

# Animation parameters.
# "Walking" period in seconds; adjust for a heavy, slower gait.
PERIOD = 1.5  
# Walking speed in pixels per second.
SPEED = 100  
# Initial horizontal offset.
START_OFFSET = -100  

# Function to compute the positions of the 15 joints at time t.
def get_joint_positions(t):
    # t is in seconds.
    # Compute walking cycle phase.
    phase = (2 * math.pi / PERIOD) * t

    # x position of the center of the body (will move to the right).
    # Wrap around when off the right edge.
    x_center = START_OFFSET + SPEED * t
    # To create a continuous loop, wrap x_center.
    x_center = x_center % (WIDTH + 200) - 100

    # Vertical base position for the torso.
    # We choose a fixed y so that the figure remains in view.
    center_y = HEIGHT // 2

    # For a heavy-walking gait the movements are measurable but subdued.
    # Arm swing amplitude (smaller swing for heavy weight)
    arm_swing = 8 * math.sin(phase)
    # Leg bending amplitude: use a sine function to create an alternating effect.
    # Left leg using phase, right leg opposite (phase+pi).
    leg_swing_left = 5 * math.sin(phase)
    leg_swing_right = 5 * math.sin(phase + math.pi)

    # Define the joint positions.
    # The coordinates below are defined relative to x_center and center_y.
    # 0: Head - placed high above the torso.
    head = (x_center, center_y - 60)
    # 1: Left Shoulder.
    left_shoulder = (x_center - 10, center_y - 40)
    # 2: Right Shoulder.
    right_shoulder = (x_center + 10, center_y - 40)
    # 3: Mid-Spine (between shoulders and hips).
    mid_spine = (x_center, center_y - 20)
    # 4: Left Elbow. (Relative to left shoulder; add an arm swing.)
    left_elbow = (x_center - 10 - 15, center_y - 40 + 10 + arm_swing)
    # 5: Right Elbow.
    right_elbow = (x_center + 10 + 15, center_y - 40 + 10 - arm_swing)
    # 6: Left Hand.
    left_hand = (left_elbow[0] - 10, left_elbow[1] + 10)
    # 7: Right Hand.
    right_hand = (right_elbow[0] + 10, right_elbow[1] + 10)
    # 8: Left Hip.
    left_hip = (x_center - 10, center_y)
    # 9: Right Hip.
    right_hip = (x_center + 10, center_y)
    # 10: Left Knee (lift leg slightly when stepping).
    left_knee = (x_center - 10, center_y + 30 - leg_swing_left)
    # 11: Right Knee.
    right_knee = (x_center + 10, center_y + 30 - leg_swing_right)
    # 12: Left Foot.
    left_foot = (x_center - 10, center_y + 60 - leg_swing_left)
    # 13: Right Foot.
    right_foot = (x_center + 10, center_y + 60 - leg_swing_right)
    # 14: Pelvis (a point slightly below the hips).
    pelvis = (x_center, center_y + 10)

    # Create a list of positions in order.
    joints = [
        head,           # 0
        left_shoulder,  # 1
        right_shoulder, # 2
        mid_spine,      # 3
        left_elbow,     # 4
        right_elbow,    # 5
        left_hand,      # 6
        right_hand,     # 7
        left_hip,       # 8
        right_hip,      # 9
        left_knee,      # 10
        right_knee,     # 11
        left_foot,      # 12
        right_foot,     # 13
        pelvis          # 14
    ]
    return joints

# Main loop.
running = True
while running:
    # Process events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the current time.
    t = pygame.time.get_ticks() / 1000.0

    # Fill the background.
    screen.fill(BLACK)

    # Get the joint positions for the current time.
    joints = get_joint_positions(t)

    # Draw each joint as a white circle (point-light).
    # Use a small radius (e.g., 4 pixels).
    for pos in joints:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 4)

    # Update the display.
    pygame.display.flip()

    # Cap frame rate to 60 fps.
    clock.tick(60)

pygame.quit()
sys.exit()