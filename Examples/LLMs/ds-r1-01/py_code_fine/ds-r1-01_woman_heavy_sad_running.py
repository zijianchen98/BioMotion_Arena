
import pygame
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Running")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

center_x, center_y = width // 2, height // 2

running = True
time = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Calculate positions for each of the 15 points
    points = []

    # Head
    head_x = center_x
    head_y = center_y - 50 + 5 * math.sin(time * 2)
    points.append((head_x, head_y))

    # Shoulders
    l_shoulder_x = center_x - 30 + 20 * math.sin(time)
    l_shoulder_y = center_y - 20 + 5 * math.cos(time)
    points.append((l_shoulder_x, l_shoulder_y))

    r_shoulder_x = center_x + 30 + 20 * math.sin(time + math.pi)
    r_shoulder_y = center_y - 20 + 5 * math.cos(time + math.pi)
    points.append((r_shoulder_x, r_shoulder_y))

    # Elbows
    l_elbow_x = l_shoulder_x + 25 * math.sin(time + math.pi/2)
    l_elbow_y = l_shoulder_y + 30 * math.cos(time + math.pi/2)
    points.append((l_elbow_x, l_elbow_y))

    r_elbow_x = r_shoulder_x + 25 * math.sin(time + math.pi*1.5)
    r_elbow_y = r_shoulder_y + 30 * math.cos(time + math.pi*1.5)
    points.append((r_elbow_x, r_elbow_y))

    # Wrists
    l_wrist_x = l_elbow_x + 20 * math.sin(time + math.pi)
    l_wrist_y = l_elbow_y + 25 * math.cos(time + math.pi)
    points.append((l_wrist_x, l_wrist_y))

    r_wrist_x = r_elbow_x + 20 * math.sin(time)
    r_wrist_y = r_elbow_y + 25 * math.cos(time)
    points.append((r_wrist_x, r_wrist_y))

    # Hips
    l_hip_x = center_x - 30 + 30 * math.sin(time + math.pi/2)
    l_hip_y = center_y + 30 + 10 * math.sin(time * 2)
    points.append((l_hip_x, l_hip_y))

    r_hip_x = center_x + 30 + 30 * math.sin(time + math.pi*1.5)
    r_hip_y = center_y + 30 + 10 * math.sin(time * 2 + math.pi)
    points.append((r_hip_x, r_hip_y))

    # Knees
    l_knee_x = l_hip_x + 40 * math.sin(time)
    l_knee_y = l_hip_y + 50 * math.cos(time)
    points.append((l_knee_x, l_knee_y))

    r_knee_x = r_hip_x + 40 * math.sin(time + math.pi)
    r_knee_y = r_hip_y + 50 * math.cos(time + math.pi)
    points.append((r_knee_x, r_knee_y))

    # Ankles
    l_ankle_x = l_knee_x + 30 * math.sin(time + math.pi/2)
    l_ankle_y = l_knee_y + 40 * math.cos(time + math.pi/2)
    points.append((l_ankle_x, l_ankle_y))

    r_ankle_x = r_knee_x + 30 * math.sin(time + math.pi*1.5)
    r_ankle_y = r_knee_y + 40 * math.cos(time + math.pi*1.5)
    points.append((r_ankle_x, r_ankle_y))

    # Feet
    l_foot_x = l_ankle_x + 15 * math.sin(time)
    l_foot_y = l_ankle_y + 20 * math.cos(time)
    points.append((l_foot_x, l_foot_y))

    r_foot_x = r_ankle_x + 15 * math.sin(time + math.pi)
    r_foot_y = r_ankle_y + 20 * math.cos(time + math.pi)
    points.append((r_foot_x, r_foot_y))

    # Draw all points
    for x, y in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    time += 0.03  # Slower movement for heavier appearance
    clock.tick(30)

pygame.quit()
