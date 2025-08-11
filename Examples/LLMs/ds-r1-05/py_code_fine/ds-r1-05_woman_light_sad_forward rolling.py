
import pygame
import math
import sys

# Define poses for the 15 points
standing = [
    (0, -200),   # head
    (0, -170),   # neck
    (-25, -160), # left_shoulder
    (25, -160),  # right_shoulder
    (-40, -140), # left_elbow
    (40, -140),  # right_elbow
    (-50, -120), # left_wrist
    (50, -120),  # right_wrist
    (0, -150),   # spine
    (-25, -20),  # left_hip
    (25, -20),   # right_hip
    (-25, 40),   # left_knee
    (25, 40),    # right_knee
    (-25, 110),  # left_ankle
    (25, 110)    # right_ankle
]

crouching = [
    (0, -120),    # head
    (0, -90),     # neck
    (-35, -75),   # left_shoulder
    (35, -75),    # right_shoulder
    (-50, -45),   # left_elbow
    (50, -45),    # right_elbow
    (-55, -10),   # left_wrist
    (55, -10),    # right_wrist
    (0, -60),     # spine
    (-35, 10),    # left_hip
    (35, 10),     # right_hip
    (-50, 50),    # left_knee
    (50, 50),     # right_knee
    (-45, 105),   # left_ankle
    (45, 105)     # right_ankle
]

rolled = [
    (0, -70),     # head
    (0, -50),     # neck
    (-40, -40),   # left_shoulder
    (40, -40),    # right_shoulder
    (-65, -10),   # left_elbow
    (65, -10),    # right_elbow
    (-65, 25),    # left_wrist
    (65, 25),     # right_wrist
    (0, -30),     # spine
    (-30, 40),    # left_hip
    (30, 40),     # right_hip
    (-45, 65),    # left_knee
    (45, 65),     # right_knee
    (-45, 100),   # left_ankle
    (45, 100)     # right_ankle
]

def interpolate_poses(pose1, pose2, factor):
    result = []
    for p1, p2 in zip(pose1, pose2):
        x = p1[0] + factor * (p2[0] - p1[0])
        y = p1[1] + factor * (p2[1] - p1[1])
        result.append((x, y))
    return result

def rotate_pose(pose, angle):
    rad = math.radians(angle)
    rotated_pose = []
    for x, y in pose:
        rx = x * math.cos(rad) - y * math.sin(rad)
        ry = x * math.sin(rad) + y * math.cos(rad)
        rotated_pose.append((rx, ry))
    return rotated_pose

def get_pose_at_time(normalized_time):
    if normalized_time <= 0.3:
        factor = normalized_time / 0.3
        return interpolate_poses(standing, crouching, factor)
    elif normalized_time <= 0.5:
        factor = (normalized_time - 0.3) / 0.2
        return interpolate_poses(crouching, rolled, factor)
    elif normalized_time <= 0.7:
        pose = rolled
        roll_phase_time = normalized_time - 0.5
        angle = roll_phase_time * 360 / 0.2
        return rotate_pose(pose, angle)
    elif normalized_time <= 0.9:
        factor = (normalized_time - 0.7) / 0.2
        return interpolate_poses(rolled, crouching, factor)
    else:
        factor = (normalized_time - 0.9) / 0.1
        return interpolate_poses(crouching, standing, factor)

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-light Forward Roll")
clock = pygame.time.Clock()
total_cycle_time = 5.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_sec = pygame.time.get_ticks() / 1000.0
    normalized_time = (time_sec % total_cycle_time) / total_cycle_time

    points = get_pose_at_time(normalized_time)
    screen.fill((0, 0, 0))

    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(point[0] + width/2), 
                           int(point[1] + height/2)), 
                          5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
