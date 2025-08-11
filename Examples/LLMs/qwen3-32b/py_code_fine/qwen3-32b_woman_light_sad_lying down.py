
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Lying Down - Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate and animation settings
FPS = 60
clock = pygame.time.Clock()

# Define a simple 2D skeleton structure (15 joints) for a person lying down
# We'll simulate the motion by rotating and translating these joints over time
# Each joint is represented as a dictionary with position and angle

# Initial joint positions (relative to center of body)
joint_structure = [
    {"name": "left_ankle", "offset": (0, 0)},
    {"name": "left_knee", "offset": (0, -50)},
    {"name": "left_hip", "offset": (0, -100)},
    {"name": "pelvis", "offset": (0, -150)},
    {"name": "right_hip", "offset": (0, -100)},
    {"name": "right_knee", "offset": (0, -50)},
    {"name": "right_ankle", "offset": (0, 0)},
    {"name": "spine_lower", "offset": (0, -180)},
    {"name": "spine_upper", "offset": (0, -220)},
    {"name": "neck", "offset": (0, -260)},
    {"name": "head", "offset": (0, -290)},
    {"name": "left_shoulder", "offset": (-50, -240)},
    {"name": "left_elbow", "offset": (-90, -220)},
    {"name": "left_wrist", "offset": (-120, -210)},
    {"name": "right_shoulder", "offset": (50, -240)},
    {"name": "right_elbow", "offset": (90, -220)},
    {"name": "right_wrist", "offset": (120, -210)},
]

# Extract joint positions for easier access
joint_positions = [j["offset"] for j in joint_structure]
joint_count = len(joint_positions)

# Animation parameters
center_x, center_y = WIDTH // 2, HEIGHT // 2
angle = 0  # Initial rotation angle
phase = 0  # Initial phase for smooth motion

# Function to rotate a point around a center
def rotate_point(point, angle, center):
    px, py = point
    cx, cy = center
    s = math.sin(angle)
    c = math.cos(angle)
    px -= cx
    py -= cy
    xnew = px * c - py * s
    ynew = px * s + py * c
    return (xnew + cx, ynew + cy)

# Function to apply a smooth, sad-like motion to the joints
def animate_joints(joints, phase):
    animated = []
    for i, (x, y) in enumerate(joints):
        # Add subtle, slow, and sad-like movement
        if i < 7:  # Legs
            x += math.sin(phase + i * 0.3) * 10
            y += math.cos(phase + i * 0.3) * 5
        elif i < 9:  # Spine
            y += math.sin(phase + i * 0.5) * 3
        elif i < 11:  # Head
            y += math.sin(phase + i * 0.4) * 2
        elif i < 14:  # Left arm
            x += math.sin(phase + i * 0.2) * 5
            y += math.cos(phase + i * 0.2) * 3
        elif i < 17:  # Right arm
            x += math.sin(phase + i * 0.2 + 3) * 5
            y += math.cos(phase + i * 0.2 + 3) * 3
        animated.append((x, y))
    return animated

# Main animation loop
def main():
    global angle, phase
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Generate current joint positions
        joints = []
        for dx, dy in joint_positions:
            x = center_x + dx
            y = center_y + dy
            joints.append((x, y))

        # Apply motion
        joints = animate_joints(joints, phase)

        # Draw the point-lights
        for x, y in joints:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        # Update phase for smooth motion
        phase += 0.01

        # Update display and control frame rate
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
