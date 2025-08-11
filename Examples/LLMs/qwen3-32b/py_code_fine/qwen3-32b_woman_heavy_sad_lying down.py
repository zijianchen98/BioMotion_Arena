
import pygame
import sys
import math
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Lying Down - Point Light Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate and animation parameters
FPS = 30
ANIMATION_FRAMES = 60  # Total frames for the animation
FRAME_DURATION = 1 / FPS

# Joint positions (relative to a central body position)
# These positions are simplified and approximate for a sad, heavy woman lying down
# Coordinates are in relative terms and will be scaled and offset during animation

# Joint names and relative positions (in a neutral standing pose)
JOINTS = {
    "head": (0, -1),
    "neck": (0, 0),
    "left_shoulder": (-0.5, 0.5),
    "right_shoulder": (0.5, 0.5),
    "left_elbow": (-0.8, 1),
    "right_elbow": (0.8, 1),
    "left_hand": (-1, 1.5),
    "right_hand": (1, 1.5),
    "left_hip": (-0.3, 1),
    "right_hip": (0.3, 1),
    "left_knee": (-0.6, 1.5),
    "right_knee": (0.6, 1.5),
    "left_ankle": (-0.8, 2),
    "right_ankle": (0.8, 2),
    "left_foot": (-1, 2.2),
    "right_foot": (1, 2.2),
}

# Normalize joint positions to fit on screen
SCALE = 100
BASE_X, BASE_Y = WIDTH // 2, HEIGHT // 2

# Generate keyframe positions for the animation
# Here we simulate a slow, sad transition from sitting to lying down
def generate_animation_frames(joints, num_frames):
    frames = []
    for t in range(num_frames):
        frame = {}
        # Body tilt angle (from upright to lying down)
        tilt_angle = math.pi / 2 * (t / num_frames)  # from 0 to 90 degrees
        # Body compression (from standing to lying down)
        compression = 1 - (t / num_frames)
        # Head drooping
        head_drop = 0.2 * (t / num_frames)

        for joint, (x, y) in joints.items():
            # Rotate joint around the base
            rx = x * math.cos(tilt_angle) - y * math.sin(tilt_angle)
            ry = x * math.sin(tilt_angle) + y * math.cos(tilt_angle)
            # Apply compression (flatten the body)
            ry *= compression
            # Apply head drop
            if joint == "head":
                ry += head_drop
            # Convert to screen coordinates
            sx = BASE_X + rx * SCALE
            sy = BASE_Y + ry * SCALE
            frame[joint] = (sx, sy)
        frames.append(frame)
    return frames

# Generate frames
animation_frames = generate_animation_frames(JOINTS, ANIMATION_FRAMES)

# Main animation loop
frame_index = 0
start_time = time.time()
running = True
while running:
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Determine the current frame based on elapsed time
    frame_index = int((elapsed_time * FPS) % ANIMATION_FRAMES)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Draw the current frame's joints
    current_frame = animation_frames[frame_index]
    for joint, pos in current_frame.items():
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
