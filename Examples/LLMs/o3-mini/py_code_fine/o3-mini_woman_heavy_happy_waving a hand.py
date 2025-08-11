
"""
Point-light stimulus animation for a happy, heavy‐set woman waving a hand.
This Pygame program shows 15 white point‐lights on a solid black background.
The points represent body joints and parts of the figure.
The right arm (points “right elbow” and “right hand”) rotates about the right shoulder
to simulate a realistic, biomechanically plausible waving action.
A gentle vertical bob simulates the weight-related sway.
"""

import sys, math, pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Heavy Woman Waving")
clock = pygame.time.Clock()

# Colors and settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Define a function to return a point with bobbing (vertical displacement)
def add_bob(y, bob):
    return y + bob

def main():
    # Center of figure’s torso (base coordinate)
    cx = WIDTH // 2
    cy = HEIGHT // 2 + 50  # shift downward
    
    # Segment definitions (static parts relative to torso center)
    # We define initial positions for 15 points (joint markers):
    # Index mapping:
    # 0: Head (center top)
    # 1: Left shoulder
    # 2: Right shoulder
    # 3: Left elbow
    # 4: Right elbow (will be computed dynamically)
    # 5: Left hand
    # 6: Right hand (computed dynamically)
    # 7: Left hip
    # 8: Right hip
    # 9: Left knee
    # 10: Right knee
    # 11: Left foot
    # 12: Right foot
    # 13: Torso center
    # 14: Lower back

    # Fixed offsets for most joints relative to torso center (cy)
    # These positions are chosen to resemble a human figure in a natural standing pose.
    base_joints = {
        0: (cx, cy - 60),               # Head (above torso)
        1: (cx - 20, cy - 40),           # Left shoulder
        2: (cx + 20, cy - 40),           # Right shoulder (pivot for waving arm)
        3: (cx - 35, cy - 10),           # Left elbow
        # 4: Right elbow: computed dynamically below.
        5: (cx - 40, cy + 20),           # Left hand
        # 6: Right hand: computed dynamically below.
        7: (cx - 15, cy + 40),           # Left hip
        8: (cx + 15, cy + 40),           # Right hip
        9: (cx - 15, cy + 80),           # Left knee
        10: (cx + 15, cy + 80),          # Right knee
        11: (cx - 15, cy + 110),         # Left foot
        12: (cx + 15, cy + 110),         # Right foot
        13: (cx, cy),                   # Torso center
        14: (cx, cy + 20)               # Lower back
    }

    # Timing for animations
    t = 0
    freq = 2.0  # frequency for the waving motion (radians per second)
    bob_freq = 1.0  # frequency for vertical bobbing
    bob_amplitude = 4  # pixels

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds elapsed since last frame (frame rate 60fps)
        t += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen to black
        screen.fill(BLACK)

        # Compute a bobbing offset (simulate the slight sway from heavy weight)
        bob = bob_amplitude * math.sin(bob_freq * t)

        # Create a dictionary for the current positions of the 15 points.
        # Start with the static points from base_joints adjusted with bob.
        joints = {}
        for key, (x, y) in base_joints.items():
            joints[key] = (x, y + bob)

        # Update the right arm positions (points 4 and 6) for waving
        # Right shoulder (point 2) is the pivot.
        right_shoulder = joints[2]
        # For a natural waving motion, let the entire right arm rotate about the shoulder.
        # The arm is simulated as a two-segment structure with constant lengths.
        upper_arm_len = 30
        lower_arm_len = 30
        # Wave angle oscillates over time.
        # Using an offset so that the arm is roughly horizontal when sin==0, then lifts upward.
        # Angle in radians. Here, an oscillation between about -1 (lifting arm upward) and 0 (arm horizontal).
        wave_angle = 0.0 - 0.5 + 0.5 * math.sin(freq * t)
        # Compute right elbow (point 4) based on rotation from the right shoulder.
        re_x = right_shoulder[0] + upper_arm_len * math.cos(wave_angle)
        re_y = right_shoulder[1] + upper_arm_len * math.sin(wave_angle)
        joints[4] = (re_x, re_y)
        # Compute right hand (point 6) rotating about the right shoulder, with the full arm length.
        rh_x = right_shoulder[0] + (upper_arm_len + lower_arm_len) * math.cos(wave_angle)
        rh_y = right_shoulder[1] + (upper_arm_len + lower_arm_len) * math.sin(wave_angle)
        joints[6] = (rh_x, rh_y)

        # Now, draw exactly 15 white points (circles) for each joint.
        # The keys 0 through 14 represent our 15 points.
        for i in range(15):
            if i in joints:
                pygame.draw.circle(screen, WHITE, (int(joints[i][0]), int(joints[i][1])), POINT_RADIUS)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()