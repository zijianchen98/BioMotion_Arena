
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Setup screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion Animation")

# Frame rate control
clock = pygame.time.Clock()

# Joint positions: x, y offsets for displaying point-lights
# These reflect the approximate placement of joints in biological motion
# For simplicity, we'll attach the positions to simulate walking.
body_structure = {
    "head": (0, -200),
    "shoulder_left": (-50, -180),
    "shoulder_right": (50, -180),
    "elbow_left": (-80, -140),
    "elbow_right": (80, -140),
    "hand_left": (-100, -100),
    "hand_right": (100, -100),
    "hip_left": (-50, -80),
    "hip_right": (50, -80),
    "knee_left": (-50, -40),
    "knee_right": (50, -40),
    "foot_left": (-50, 0),
    "foot_right": (50, 0),
    "torso_center": (0, -100),
    "pelvis_center": (0, -60)
}

# Timer for controlling motion
animation_frame = 0
walking_speed = 0.05


def update_positions(frame):
    """Update joint positions to simulate walking."""
    updated_positions = {}
    for joint, (dx, dy) in body_structure.items():
        if "foot" in joint:
            # Feet move sinusoidally to simulate walking
            offset_y = math.sin(frame + (50 if "left" in joint else -50)) * 20
        elif "knee" in joint:
            # Knees follow a slightly dampened sinusoidal motion
            offset_y = math.sin(frame + (50 if "left" in joint else -50)) * 15
        elif "elbow" in joint or "hand" in joint:
            # Arms swing sinusoidally but opposite to the legs
            offset_y = math.sin(frame + (50 if "right" in joint else -50)) * 10
        else:
            # Central parts (torso, pelvis) have minor movement
            offset_y = math.sin(frame) * 2

        updated_positions[joint] = (dx, dy + offset_y)

    return updated_positions


def draw_body(screen, positions):
    """Draw the body using white point-lights."""
    for joint, (x, y) in positions.items():
        px = screen_width // 2 + x
        py = screen_height // 2 + y
        pygame.draw.circle(screen, white, (px, py), 5)


# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the animation frame
    animation_frame += walking_speed

    # Clear screen and set background to black
    screen.fill(black)

    # Update joint positions for current frame
    joint_positions = update_positions(animation_frame)

    # Draw the body
    draw_body(screen, joint_positions)

    # Update the display
    pygame.display.flip()

    # Maintain frame rate (60 FPS)
    clock.tick(60)
