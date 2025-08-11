
import pygame
import math
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman with Heavy Weight Waving Hand")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Joint positions (simplified 15-point skeleton)
# We'll define a basic stick figure with 15 points
# Each joint is represented as (x, y, angle, length to next joint)
# We'll use a simplified kinematic model to animate waving

# Joint hierarchy (parent index)
# We use a simple 2D skeletal structure for a waving hand
# 0 - Head center
# 1 - Left shoulder
# 2 - Left elbow
# 3 - Left wrist (hand)
# 4 - Right shoulder
# 5 - Right elbow
# 6 - Right wrist
# 7 - Spine top
# 8 - Spine bottom
# 9 - Left hip
# 10 - Left knee
# 11 - Left ankle
# 12 - Right hip
# 13 - Right knee
# 14 - Right ankle

# Lengths between joints (in pixels)
joint_lengths = [
    40,  # Head to shoulder
    30,  # Shoulder to elbow
    30,  # Elbow to wrist
    30,  # Shoulder to elbow (other arm)
    30,  # Elbow to wrist (other arm)
    40,  # Spine top to bottom
    30,  # Spine bottom to hip (left)
    30,  # Hip to knee (left)
    30,  # Knee to ankle (left)
    30,  # Spine bottom to hip (right)
    30,  # Hip to knee (right)
    30,  # Knee to ankle (right)
    20,  # Head to top of spine
    20,  # Head to other shoulder
    20,  # Head to other shoulder
]

# Initial joint angles (in radians)
joint_angles = [0.0] * 15

# Position of the root (head)
root_x = WIDTH // 2
root_y = HEIGHT // 2 - 100

# Time variable for animation
time = 0.0

def calculate_joint_positions(joint_angles, root_x, root_y):
    positions = []
    x, y = root_x, root_y
    positions.append((x, y))  # Head

    # Left arm
    x += joint_lengths[0] * math.cos(joint_angles[1])
    y += joint_lengths[0] * math.sin(joint_angles[1])
    positions.append((x, y))  # Left shoulder

    x += joint_lengths[1] * math.cos(joint_angles[2])
    y += joint_lengths[1] * math.sin(joint_angles[2])
    positions.append((x, y))  # Left elbow

    x += joint_lengths[2] * math.cos(joint_angles[3])
    y += joint_lengths[2] * math.sin(joint_angles[3])
    positions.append((x, y))  # Left wrist

    # Right arm
    x = root_x
    y = root_y
    x -= joint_lengths[3] * math.cos(joint_angles[4])
    y -= joint_lengths[3] * math.sin(joint_angles[4])
    positions.append((x, y))  # Right shoulder

    x -= joint_lengths[4] * math.cos(joint_angles[5])
    y -= joint_lengths[4] * math.sin(joint_angles[5])
    positions.append((x, y))  # Right elbow

    x -= joint_lengths[5] * math.cos(joint_angles[6])
    y -= joint_lengths[5] * math.sin(joint_angles[6])
    positions.append((x, y))  # Right wrist

    # Spine
    x = root_x
    y = root_y + joint_lengths[12]
    positions.append((x, y))  # Spine top

    x = root_x
    y = root_y + joint_lengths[12] + joint_lengths[6]
    positions.append((x, y))  # Spine bottom

    # Left leg
    x = root_x
    y = root_y + joint_lengths[12] + joint_lengths[6]
    x -= joint_lengths[7] * math.cos(joint_angles[9])
    y += joint_lengths[7] * math.sin(joint_angles[9])
    positions.append((x, y))  # Left hip

    x -= joint_lengths[8] * math.cos(joint_angles[10])
    y += joint_lengths[8] * math.sin(joint_angles[10])
    positions.append((x, y))  # Left knee

    x -= joint_lengths[9] * math.cos(joint_angles[11])
    y += joint_lengths[9] * math.sin(joint_angles[11])
    positions.append((x, y))  # Left ankle

    # Right leg
    x = root_x
    y = root_y + joint_lengths[12] + joint_lengths[6]
    x += joint_lengths[10] * math.cos(joint_angles[13])
    y += joint_lengths[10] * math.sin(joint_angles[13])
    positions.append((x, y))  # Right hip

    x += joint_lengths[11] * math.cos(joint_angles[14])
    y += joint_lengths[11] * math.sin(joint_angles[14])
    positions.append((x, y))  # Right knee

    x += joint_lengths[12] * math.cos(joint_angles[14])
    y += joint_lengths[12] * math.sin(joint_angles[14])
    positions.append((x, y))  # Right ankle

    return positions

def update_joint_angles(joint_angles, time):
    # Waving animation - left arm moves in a smooth wave
    joint_angles[1] = 0.0 + 0.5 * math.sin(time * 0.5)  # Left shoulder
    joint_angles[2] = 0.0 + 0.5 * math.sin(time * 0.5 + 1.0)  # Left elbow
    joint_angles[3] = 0.0 + 0.5 * math.sin(time * 0.5 + 2.0)  # Left wrist

    # Right arm remains still
    joint_angles[4] = 0.0
    joint_angles[5] = 0.0
    joint_angles[6] = 0.0

    # Spine and body remain still
    joint_angles[7] = 0.0
    joint_angles[8] = 0.0
    joint_angles[9] = 0.0
    joint_angles[10] = 0.0
    joint_angles[11] = 0.0
    joint_angles[12] = 0.0
    joint_angles[13] = 0.0
    joint_angles[14] = 0.0

    return joint_angles

def main():
    global time
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update joint angles
        joint_angles = update_joint_angles(joint_angles, time)
        time += 0.05

        # Calculate joint positions
        positions = calculate_joint_positions(joint_angles, root_x, root_y)

        # Draw point-lights
        for x, y in positions:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
