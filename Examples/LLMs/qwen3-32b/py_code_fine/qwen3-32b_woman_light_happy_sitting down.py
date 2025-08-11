
import pygame
import sys
import math
import numpy as np

# Define joint positions (relative to center of the body)
# These positions are simplified for demonstration purposes
# and should be adapted from a real motion capture dataset for accuracy.

# 15 joints: Head, neck, spine, chest, right shoulder, right elbow, right hand,
#            left shoulder, left elbow, left hand, right hip, right knee, right foot,
#            left hip, left knee, left foot

# Define keyframes for the sitting down action (simplified)
# Each keyframe is a list of (x, y) positions for each joint

# We'll simulate a simple sitting down motion by moving hips down and knees bending

# Frame 0: standing
keyframes = [
    # Head, Neck, Spine, Chest, RShoulder, RElbow, RHand,
    # LShoulder, LElbow, LHand, RHip, RKnee, RFoot,
    # LHip, LKnee, LFoot
    [ ( 0, -100), ( 0, -80), ( 0, -60), ( 0, -40), ( -20, -20), ( -20, 0), ( -20, 20),
      ( 20, -20), ( 20, 0), ( 20, 20), ( -20, 40), ( -20, 60), ( -20, 80),
      ( 20, 40), ( 20, 60), ( 20, 80) ],
    # Frame 1
    [ ( 0, -100), ( 0, -80), ( 0, -60), ( 0, -40), ( -20, -20), ( -20, 0), ( -20, 20),
      ( 20, -20), ( 20, 0), ( 20, 20), ( -20, 50), ( -20, 65), ( -20, 80),
      ( 20, 50), ( 20, 65), ( 20, 80) ],
    # Frame 2
    [ ( 0, -100), ( 0, -80), ( 0, -60), ( 0, -40), ( -20, -20), ( -20, 0), ( -20, 20),
      ( 20, -20), ( 20, 0), ( 20, 20), ( -20, 60), ( -20, 70), ( -20, 80),
      ( 20, 60), ( 20, 70), ( 20, 80) ],
    # Frame 3
    [ ( 0, -100), ( 0, -80), ( 0, -60), ( 0, -40), ( -20, -20), ( -20, 0), ( -20, 20),
      ( 20, -20), ( 20, 0), ( 20, 20), ( -20, 70), ( -20, 75), ( -20, 80),
      ( 20, 70), ( 20, 75), ( 20, 80) ],
    # Frame 4 (sitting)
    [ ( 0, -100), ( 0, -80), ( 0, -60), ( 0, -40), ( -20, -20), ( -20, 0), ( -20, 20),
      ( 20, -20), ( 20, 0), ( 20, 20), ( -20, 80), ( -20, 80), ( -20, 80),
      ( 20, 80), ( 20, 80), ( 20, 80) ],
]

# Convert keyframes to numpy array for easy interpolation
keyframes = np.array(keyframes)

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Animation settings
num_frames = len(keyframes)
frame_duration = 1000 // FPS  # in milliseconds
current_frame = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Draw point lights
    for i in range(15):
        x, y = keyframes[current_frame][i]
        pygame.draw.circle(screen, WHITE, (WIDTH // 2 + int(x * 10), HEIGHT // 2 + int(y * 10)), 5)

    # Update display
    pygame.display.flip()

    # Move to next frame
    current_frame = (current_frame + 1) % num_frames

    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
