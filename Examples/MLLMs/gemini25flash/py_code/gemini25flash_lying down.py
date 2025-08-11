
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Man Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Center of the figure on the screen.
# The figure will be placed such that its hip center is at CENTER_X, CENTER_Y.
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# Scale factor from relative coordinates (conceptual units) to pixels.
# The relative coordinates are designed so that total body length (feet to head)
# is approximately 1.5 units (0.7 - (-0.8) = 1.5).
# If we want the figure to be roughly 400 pixels long, SCALE = 400 / 1.5 = ~266.
SCALE = 260

# Define the 15 body points and their initial relative coordinates for a lying pose.
# The figure is imagined lying on its back, head to the right, feet to the left.
# (0,0) is set to be the approximate center of the hips.
# X-axis represents the length of the body (positive X towards head, negative X towards feet).
# Y-axis represents the width of the body (positive Y towards the viewer's left, negative Y towards the viewer's right).
# This configuration will result in a horizontal figure on the screen.

# The 15 points follow a common standard for point-light displays:
# Head, Neck, R_Shoulder, L_Shoulder, R_Elbow, L_Elbow, R_Wrist, L_Wrist,
# Torso (mid-spine/sternum), R_Hip, L_Hip, R_Knee, L_Knee, R_Ankle, L_Ankle
relative_coords_base = [
    # 0: Head (approx at top of spine)
    (0.7, 0.0),
    # 1: Neck (base of skull)
    (0.6, 0.0),
    # 2: R_Shoulder, 3: L_Shoulder (Shoulder width)
    (0.45, -0.2), # Right Shoulder (viewer's right)
    (0.45, 0.2),  # Left Shoulder (viewer's left)
    # 4: R_Elbow, 5: L_Elbow (Arms straight or slightly bent, close to body)
    (0.2, -0.25), # Right Elbow (slightly lower X, slightly wider Y than shoulder)
    (0.2, 0.25),  # Left Elbow
    # 6: R_Wrist, 7: L_Wrist (Hands near hips/thighs)
    (0.0, -0.15), # Right Wrist (at hip level X, closer to center Y)
    (0.0, 0.15),  # Left Wrist
    # 8: Torso (center of chest/upper abdomen, for breathing)
    (0.3, 0.0),
    # 9: R_Hip, 10: L_Hip (pelvic width, at origin of X)
    (0.0, -0.15), # Right Hip
    (0.0, 0.15),  # Left Hip
    # 11: R_Knee, 12: L_Knee (Legs straight, slightly narrower)
    (-0.4, -0.1), # Right Knee
    (-0.4, 0.1),  # Left Knee
    # 13: R_Ankle, 14: L_Ankle (Feet together)
    (-0.8, -0.05), # Right Ankle
    (-0.8, 0.05)   # Left Ankle
]

# Map for clarity (using named indices for better readability in animation logic)
POINT_NAMES = {
    "HEAD": 0, "NECK": 1,
    "R_SHOULDER": 2, "L_SHOULDER": 3,
    "R_ELBOW": 4, "L_ELBOW": 5,
    "R_WRIST": 6, "L_WRIST": 7,
    "TORSO": 8,
    "R_HIP": 9, "L_HIP": 10,
    "R_KNEE": 11, "L_KNEE": 12,
    "R_ANKLE": 13, "L_ANKLE": 14
}

# Animation parameters for subtle, realistic biological motion (e.g., breathing, minor adjustments)
frame_count = 0
FPS = 60 # Frames per second

# Breathing motion (simulating chest rising/falling as if lying on a surface)
# This affects the vertical position (screen Y) of relevant points.
BREATH_AMPLITUDE_Y = 0.02 * SCALE # Amplitude in pixels
BREATH_FREQUENCY = 0.04 # Cycles per frame (e.g., 60 FPS * 0.04 = 2.4 cycles/second = ~1.2 breaths/second)

# Limb twitches (small, seemingly random movements of arms and legs)
LIMB_TWITCH_AMPLITUDE_X = 0.005 * SCALE # Amplitude in pixels for X-axis movement
LIMB_TWITCH_AMPLITUDE_Y = 0.005 * SCALE # Amplitude in pixels for Y-axis movement
LIMB_TWITCH_FREQUENCY = 0.1 # Faster, more erratic cycles per frame

# Define which points are affected by which animation types
BREATH_POINTS = [
    POINT_NAMES["TORSO"], POINT_NAMES["HEAD"], POINT_NAMES["NECK"],
    POINT_NAMES["R_SHOULDER"], POINT_NAMES["L_SHOULDER"]
]

ARM_POINTS = [
    POINT_NAMES["R_ELBOW"], POINT_NAMES["L_ELBOW"],
    POINT_NAMES["R_WRIST"], POINT_NAMES["L_WRIST"]
]

LEG_POINTS = [
    POINT_NAMES["R_KNEE"], POINT_NAMES["L_KNEE"],
    POINT_NAMES["R_ANKLE"], POINT_NAMES["L_ANKLE"]
]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Calculate and draw points
    for i, (rel_x, rel_y) in enumerate(relative_coords_base):
        # Convert relative coordinates to absolute screen coordinates
        # X-coordinate on screen: CENTER_X + (relative X * SCALE)
        # Y-coordinate on screen: CENTER_Y + (relative Y * SCALE)
        # Note: screen Y increases downwards, so a positive rel_y means further down on screen.
        # This means points with positive rel_y (left side of body from viewer's perspective) will appear below the centerline.
        screen_x = CENTER_X + int(rel_x * SCALE)
        screen_y = CENTER_Y + int(rel_y * SCALE)

        # Apply breathing animation for torso, head, neck, and shoulders
        if i in BREATH_POINTS:
            # Use sine wave for smooth, periodic breathing motion.
            # Adding `i * phase_shift` creates a slight delay/phase difference between points
            # which makes the movement appear more natural than perfectly synchronized motion.
            breath_offset_y = BREATH_AMPLITUDE_Y * math.sin(frame_count * BREATH_FREQUENCY + i * 0.5)
            screen_y += breath_offset_y

        # Apply limb twitch animation for arms and legs
        if i in ARM_POINTS or i in LEG_POINTS:
            # Use sine and cosine for slightly more complex, oscillating movements.
            # Different frequencies and phase shifts for X and Y components, and for each joint,
            # help create a subtle, non-repeating "twitch" effect.
            twitch_offset_x = LIMB_TWITCH_AMPLITUDE_X * math.sin(frame_count * LIMB_TWITCH_FREQUENCY + i * 0.7)
            twitch_offset_y = LIMB_TWITCH_AMPLITUDE_Y * math.cos(frame_count * LIMB_TWITCH_FREQUENCY * 1.2 + i * 0.9)
            screen_x += twitch_offset_x
            screen_y += twitch_offset_y

        # Draw the point (white circle)
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

    # Update the display to show the new frame
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame_count += 1
    clock.tick(FPS)

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
