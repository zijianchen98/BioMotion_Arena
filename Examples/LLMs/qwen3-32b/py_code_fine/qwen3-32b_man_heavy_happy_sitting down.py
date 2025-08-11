
import pygame
import math
import sys
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Man Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Joint positions (simplified stick figure with 15 joints)
# We'll animate these positions to simulate "sitting down" with a heavy weight
# We'll define keyframes manually for the "sitting down" motion

# Joint names for reference
joint_names = [
    "head", "neck", "left shoulder", "right shoulder",
    "left elbow", "right elbow", "left hand", "right hand",
    "spine", "left hip", "right hip", "left knee",
    "right knee", "left foot", "right foot"
]

# Define keyframes for the sitting down motion
# Each keyframe is a dictionary of joint positions (x, y)
keyframes = []

# Initial standing position
keyframes.append({
    "head": (WIDTH//2, 100),
    "neck": (WIDTH//2, 150),
    "left shoulder": (WIDTH//2 - 50, 200),
    "right shoulder": (WIDTH//2 + 50, 200),
    "left elbow": (WIDTH//2 - 80, 250),
    "right elbow": (WIDTH//2 + 80, 250),
    "left hand": (WIDTH//2 - 100, 300),
    "right hand": (WIDTH//2 + 100, 300),
    "spine": (WIDTH//2, 250),
    "left hip": (WIDTH//2 - 50, 300),
    "right hip": (WIDTH//2 + 50, 300),
    "left knee": (WIDTH//2 - 80, 380),
    "right knee": (WIDTH//2 + 80, 380),
    "left foot": (WIDTH//2 - 100, 450),
    "right foot": (WIDTH//2 + 100, 450),
})

# Slight bend in knees
keyframes.append({
    "head": (WIDTH//2, 100),
    "neck": (WIDTH//2, 150),
    "left shoulder": (WIDTH//2 - 50, 200),
    "right shoulder": (WIDTH//2 + 50, 200),
    "left elbow": (WIDTH//2 - 80, 250),
    "right elbow": (WIDTH//2 + 80, 250),
    "left hand": (WIDTH//2 - 100, 300),
    "right hand": (WIDTH//2 + 100, 300),
    "spine": (WIDTH//2, 260),
    "left hip": (WIDTH//2 - 50, 300),
    "right hip": (WIDTH//2 + 50, 300),
    "left knee": (WIDTH//2 - 80, 400),
    "right knee": (WIDTH//2 + 80, 400),
    "left foot": (WIDTH//2 - 100, 450),
    "right foot": (WIDTH//2 + 100, 450),
})

# Start bending forward
keyframes.append({
    "head": (WIDTH//2, 120),
    "neck": (WIDTH//2, 170),
    "left shoulder": (WIDTH//2 - 45, 210),
    "right shoulder": (WIDTH//2 + 45, 210),
    "left elbow": (WIDTH//2 - 70, 260),
    "right elbow": (WIDTH//2 + 70, 260),
    "left hand": (WIDTH//2 - 90, 310),
    "right hand": (WIDTH//2 + 90, 310),
    "spine": (WIDTH//2, 270),
    "left hip": (WIDTH//2 - 45, 310),
    "right hip": (WIDTH//2 + 45, 310),
    "left knee": (WIDTH//2 - 70, 410),
    "right knee": (WIDTH//2 + 70, 410),
    "left foot": (WIDTH//2 - 90, 450),
    "right foot": (WIDTH//2 + 90, 450),
})

# Sitting down (heavy weight)
keyframes.append({
    "head": (WIDTH//2, 150),
    "neck": (WIDTH//2, 200),
    "left shoulder": (WIDTH//2 - 30, 230),
    "right shoulder": (WIDTH//2 + 30, 230),
    "left elbow": (WIDTH//2 - 50, 270),
    "right elbow": (WIDTH//2 + 50, 270),
    "left hand": (WIDTH//2 - 70, 310),
    "right hand": (WIDTH//2 + 70, 310),
    "spine": (WIDTH//2, 300),
    "left hip": (WIDTH//2 - 30, 340),
    "right hip": (WIDTH//2 + 30, 340),
    "left knee": (WIDTH//2 - 50, 430),
    "right knee": (WIDTH//2 + 50, 430),
    "left foot": (WIDTH//2 - 70, 450),
    "right foot": (WIDTH//2 + 70, 450),
})

# Final seated position
keyframes.append({
    "head": (WIDTH//2, 160),
    "neck": (WIDTH//2, 210),
    "left shoulder": (WIDTH//2 - 25, 240),
    "right shoulder": (WIDTH//2 + 25, 240),
    "left elbow": (WIDTH//2 - 40, 280),
    "right elbow": (WIDTH//2 + 40, 280),
    "left hand": (WIDTH//2 - 60, 320),
    "right hand": (WIDTH//2 + 60, 320),
    "spine": (WIDTH//2, 310),
    "left hip": (WIDTH//2 - 25, 350),
    "right hip": (WIDTH//2 + 25, 350),
    "left knee": (WIDTH//2 - 40, 440),
    "right knee": (WIDTH//2 + 40, 440),
    "left foot": (WIDTH//2 - 60, 450),
    "right foot": (WIDTH//2 + 60, 450),
})

# Repeat the final pose to hold for a bit
keyframes.extend([keyframes[-1]] * 10)

# Interpolate between keyframes for smooth motion
def interpolate_frames(frame1, frame2, t):
    """Interpolate between two keyframes by time t (0 <= t <= 1)"""
    result = {}
    for joint in frame1:
        x1, y1 = frame1[joint]
        x2, y2 = frame2[joint]
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        result[joint] = (x, y)
    return result

# Animation loop
current_frame = 0
interpolation_steps = 10  # number of frames to interpolate between keyframes

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Interpolate between current and next keyframe
    next_frame = min(current_frame + 1, len(keyframes) - 1)
    t = current_frame % 1
    frame = interpolate_frames(keyframes[current_frame], keyframes[next_frame], t)

    # Draw the point-light stimulus
    for joint in joint_names:
        x, y = frame[joint]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

    # Update current frame
    current_frame += 1 / interpolation_steps
    if current_frame >= len(keyframes) - 1:
        current_frame = 0  # Loop the animation
