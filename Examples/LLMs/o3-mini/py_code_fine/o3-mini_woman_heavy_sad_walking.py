
"""
This program uses Pygame to display an animation of a point‐light “skeleton” depicting a sad,
heavily weighted woman walking. The figure is rendered using exactly 15 white dots on a black
background. The positions of the dots (representing head, neck, shoulders, elbows, hands,
torso, hips, knees, and feet) are modulated with smooth sinusoidal functions to simulate a
biomechanically plausible walking cycle with a slight downward (sad) posture.
"""

import sys, math, pygame
from pygame.locals import QUIT

# Define the relative positions (in pixels) for the 15 joints.
# The coordinate system here is relative to a “body center” point (the mid-hip).
# A positive y is downward.
# These positions give a slightly slumped posture.
RELATIVE_JOINTS = {
    'head': (0, -50),
    'neck': (0, -40),
    'left_shoulder': (-10, -40),
    'right_shoulder': (10, -40),
    'left_elbow': (-20, -30),
    'right_elbow': (20, -30),
    'left_hand': (-25, -20),
    'right_hand': (25, -20),
    'torso': (0, -20),
    'left_hip': (-10, 0),
    'right_hip': (10, 0),
    'left_knee': (-10, 20),
    'right_knee': (10, 20),
    'left_foot': (-10, 40),
    'right_foot': (10, 40),
}

# Walking cycle parameters
CYCLE_PERIOD = 2.0  # seconds per walking cycle
ARM_SWING_AMPLITUDE = 5  # pixels for arm horizontal swing
LEG_SWING_AMPLITUDE = 5  # pixels for leg horizontal swing
HEAD_BOB_AMPLITUDE = 2   # pixels vertical bobbing for head
FOOT_EXTRA = 2         # extra swing for feet

# Global motion parameters
WALK_SPEED = 100  # pixels per second for horizontal translation

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def update_joint_positions(t, base_pos):
    """
    Given the elapsed time t (in seconds) and a global base_pos (x,y) for the body’s hip center,
    return a dictionary mapping joint names to their absolute (x,y) coordinates on screen.
    
    The walking cycle is simulated using sinusoidal modulations:
    - Arms swing opposite to the legs.
    - The legs alternate swinging.
    - The head experiences a slight bob.
    """
    # Compute phase in the walking cycle: goes from 0 to 2*pi every CYCLE_PERIOD seconds.
    phase = 2 * math.pi * ((t % CYCLE_PERIOD) / CYCLE_PERIOD)
    
    # For arms: to simulate contralateral swing, define phase offsets.
    # Left arm swings with right leg: use (phase + pi)
    # Right arm swings with left leg: use phase.
    left_arm_offset = ARM_SWING_AMPLITUDE * math.sin(phase + math.pi)
    right_arm_offset = ARM_SWING_AMPLITUDE * math.sin(phase)
    # For legs: left leg swings with phase; right leg swings with phase+pi.
    left_leg_offset = LEG_SWING_AMPLITUDE * math.sin(phase)
    right_leg_offset = LEG_SWING_AMPLITUDE * math.sin(phase + math.pi)
    # Head bobbing (vertical oscillation)
    head_bob = HEAD_BOB_AMPLITUDE * math.sin(phase)
    
    positions = {}
    # Global translation: The body moves horizontally at a steady pace.
    base_x, base_y = base_pos

    # Process each joint. Start with the base relative coordinates then add
    # time-dependent offsets based on the joint identity.
    for joint, (rx, ry) in RELATIVE_JOINTS.items():
        # Start with the default relative position.
        x = rx
        y = ry

        # Apply modifications based on joint name.
        if joint == 'head':
            # Add a small bob effect.
            y += head_bob
        elif joint in ('neck', 'left_shoulder', 'right_shoulder', 'torso'):
            # The upper torso moves a bit less.
            y += 0.5 * head_bob
        elif joint in ('left_elbow', 'left_hand'):
            # Left arm joints swing with an offset.
            x += left_arm_offset
            if joint == 'left_hand':
                x += 0.4 * left_arm_offset  # a little extra at the extremity
        elif joint in ('right_elbow', 'right_hand'):
            x += right_arm_offset
            if joint == 'right_hand':
                x += 0.4 * right_arm_offset
        elif joint in ('left_knee', 'left_foot'):
            x += left_leg_offset
            if joint == 'left_foot':
                x += 0.4 * left_leg_offset
        elif joint in ('right_knee', 'right_foot'):
            x += right_leg_offset
            if joint == 'right_foot':
                x += 0.4 * right_leg_offset
        # For hips, no extra swing is added.
        # For any other joint, no additional modulations.

        # Now add the global base position.
        abs_x = int(base_x + x)
        abs_y = int(base_y + y)
        positions[joint] = (abs_x, abs_y)
    return positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion - Sad Heavy Woman Walking")
    clock = pygame.time.Clock()
    
    # Define the starting horizontal base position for the hip center.
    # We start a bit off screen to the left.
    start_x = -50
    # Fix the vertical base position (hips) roughly to mid-screen.
    base_y = SCREEN_HEIGHT // 2 + 50  # a bit lower to leave space for head bobbing
    
    time_start = pygame.time.get_ticks() / 1000.0  # in seconds
    
    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Compute elapsed time.
        t = pygame.time.get_ticks() / 1000.0 - time_start

        # Update the global horizontal translation.
        base_x = start_x + WALK_SPEED * t
        # Wrap around if the figure goes off the right edge.
        if base_x > SCREEN_WIDTH + 50:
            # Reset the start time so the animation keeps going seamlessly.
            time_start = pygame.time.get_ticks() / 1000.0
            base_x = start_x

        # Compute joint positions.
        base_position = (base_x, base_y)
        joint_positions = update_joint_positions(t, base_position)

        # Drawing.
        screen.fill((0, 0, 0))  # Black background
        
        # Draw each joint as a white circle.
        # Using a small radius (e.g., 5 pixels) to simulate point-lights.
        for pos in joint_positions.values():
            pygame.draw.circle(screen, (255, 255, 255), pos, 5)

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()