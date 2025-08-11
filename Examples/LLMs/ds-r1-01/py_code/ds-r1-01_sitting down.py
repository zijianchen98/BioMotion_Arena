
import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sitting Down")

clock = pygame.time.Clock()
fps = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

duration = 2000  # Animation duration in milliseconds

# Skeleton parameters
thigh_length = 50
shin_length = 50
upper_arm_length = 40
lower_arm_length = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()
    t = (current_time % duration) / duration  # Normalized time [0, 1]

    points = []

    # Head and neck
    head_y = 100 + 200 * t
    points.append((400, int(head_y)))  # Head
    points.append((400, int(head_y + 20)))  # Neck

    # Shoulders
    shoulder_y = int(head_y + 50)
    points.append((360, shoulder_y))  # Left shoulder
    points.append((440, shoulder_y))  # Right shoulder

    # Arms
    arm_angle = math.pi/4 * (1 + t)
    # Left arm
    elbow_lx = 360 - upper_arm_length * math.cos(arm_angle)
    elbow_ly = shoulder_y + upper_arm_length * math.sin(arm_angle)
    points.append((int(elbow_lx), int(elbow_ly)))
    wrist_lx = elbow_lx - lower_arm_length * math.cos(arm_angle)
    wrist_ly = elbow_ly + lower_arm_length * math.sin(arm_angle)
    points.append((int(wrist_lx), int(wrist_ly)))
    # Right arm
    elbow_rx = 440 + upper_arm_length * math.cos(arm_angle)
    elbow_ry = shoulder_y + upper_arm_length * math.sin(arm_angle)
    points.append((int(elbow_rx), int(elbow_ry)))
    wrist_rx = elbow_rx + lower_arm_length * math.cos(arm_angle)
    wrist_ry = elbow_ry + lower_arm_length * math.sin(arm_angle)
    points.append((int(wrist_rx), int(wrist_ry)))

    # Hips
    hip_y = 300 + 200 * t
    points.append((360, int(hip_y)))  # Left hip
    points.append((440, int(hip_y)))  # Right hip

    # Legs kinematics
    def calculate_leg(hip_x, hip_y, side):
        angle_hip = math.pi - (math.pi / 2) * t
        knee_x = hip_x + thigh_length * math.cos(angle_hip)
        knee_y = hip_y + thigh_length * math.sin(angle_hip)
        points.append((int(knee_x), int(knee_y)))

        angle_knee = math.pi - (math.pi / 2) * t
        shin_angle = angle_hip - (math.pi - angle_knee)
        ankle_x = knee_x + shin_length * math.cos(shin_angle)
        ankle_y = knee_y + shin_length * math.sin(shin_angle)
        points.append((int(ankle_x), int(ankle_y)))

    calculate_leg(360, hip_y, "left")
    calculate_leg(440, hip_y, "right")

    # Torso points
    points.append((400, int(hip_y - 50)))  # Chest
    points.append((400, int(hip_y)))  # Belly

    # Draw all points
    for point in points:
        pygame.draw.circle(screen, WHITE, point, 5)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
