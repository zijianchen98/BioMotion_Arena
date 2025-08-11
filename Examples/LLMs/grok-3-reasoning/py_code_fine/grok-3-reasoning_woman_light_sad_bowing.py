
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Sad Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 points representing body parts (initial positions, standing upright)
points = {
    "head": [400, 100],
    "neck": [400, 120],
    "torso_center": [400, 200],
    "left_shoulder": [380, 140],
    "right_shoulder": [420, 140],
    "left_elbow": [370, 220],
    "right_elbow": [430, 220],
    "left_wrist": [360, 300],
    "right_wrist": [440, 300],
    "left_hip": [390, 300],
    "right_hip": [410, 300],
    "left_knee": [390, 400],
    "right_knee": [410, 400],
    "left_ankle": [390, 500],
    "right_ankle": [410, 500]
}

# Animation parameters
clock = pygame.time.Clock()
FPS = 60
bow_angle = 0  # Angle of torso in degrees (0 = upright, increases as bowing)
max_bow_angle = 70  # Maximum bowing angle
bow_speed = 0.5  # Degrees per frame (slower for sadness)

# Segment lengths (for biomechanical consistency)
torso_length = points["torso_center"][1] - points["neck"][1]  # 80 pixels
neck_length = points["neck"][1] - points["head"][1]  # 20 pixels
upper_arm_length = points["left_elbow"][1] - points["left_shoulder"][1]  # 80 pixels
forearm_length = points["left_wrist"][1] - points["left_elbow"][1]  # 80 pixels

# Main loop
running = True
bowing_down = True  # Direction of bowing

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bowing angle (slow and deliberate for sadness)
    if bowing_down:
        bow_angle += bow_speed
        if bow_angle >= max_bow_angle:
            bowing_down = False
    else:
        bow_angle -= bow_speed
        if bow_angle <= 0:
            bowing_down = True

    # Convert angle to radians
    theta = math.radians(bow_angle)

    # Update upper body positions based on bowing angle
    # Hips are the pivot point, legs remain stationary
    pivot_x, pivot_y = (points["left_hip"][0] + points["right_hip"][0]) // 2, points["left_hip"][1]

    # Torso center rotates around hips
    torso_angle = theta
    torso_dx = torso_length * math.sin(torso_angle)
    torso_dy = torso_length * math.cos(torso_angle)
    points["torso_center"][0] = pivot_x - torso_dx
    points["torso_center"][1] = pivot_y - torso_dy

    # Neck rotates with torso, attached to torso center
    neck_dx = neck_length * math.sin(torso_angle)
    neck_dy = neck_length * math.cos(torso_angle)
    points["neck"][0] = points["torso_center"][0] - neck_dx
    points["neck"][1] = points["torso_center"][1] - neck_dy

    # Head tilts slightly more than torso for sadness
    head_angle = theta + math.radians(10)  # Extra 10 degrees for head droop
    head_dx = neck_length * math.sin(head_angle)
    head_dy = neck_length * math.cos(head_angle)
    points["head"][0] = points["neck"][0] - head_dx
    points["head"][1] = points["neck"][1] - head_dy

    # Shoulders rotate with torso
    shoulder_offset = 20  # Horizontal distance from torso center to shoulders
    points["left_shoulder"][0] = points["torso_center"][0] - shoulder_offset * math.cos(torso_angle)
    points["left_shoulder"][1] = points["torso_center"][1] - shoulder_offset * math.sin(torso_angle)
    points["right_shoulder"][0] = points["torso_center"][0] + shoulder_offset * math.cos(torso_angle)
    points["right_shoulder"][1] = points["torso_center"][1] + shoulder_offset * math.sin(torso_angle)

    # Arms follow shoulders, keeping segment lengths constant
    # Left arm
    left_elbow_angle = torso_angle  # Arms hang naturally
    elbow_dx = upper_arm_length * math.sin(left_elbow_angle)
    elbow_dy = upper_arm_length * math.cos(left_elbow_angle)
    points["left_elbow"][0] = points["left_shoulder"][0] - elbow_dx
    points["left_elbow"][1] = points["left_shoulder"][1] - elbow_dy
    wrist_dx = forearm_length * math.sin(left_elbow_angle)
    wrist_dy = forearm_length * math.cos(left_elbow_angle)
    points["left_wrist"][0] = points["left_elbow"][0] - wrist_dx
    points["left_wrist"][1] = points["left_elbow"][1] - wrist_dy

    # Right arm
    right_elbow_angle = torso_angle
    elbow_dx = upper_arm_length * math.sin(right_elbow_angle)
    elbow_dy = upper_arm_length * math.cos(right_elbow_angle)
    points["right_elbow"][0] = points["right_shoulder"][0] - elbow_dx
    points["right_elbow"][1] = points["right_shoulder"][1] - elbow_dy
    wrist_dx = forearm_length * math.sin(right_elbow_angle)
    wrist_dy = forearm_length * math.cos(right_elbow_angle)
    points["right_wrist"][0] = points["right_elbow"][0] - wrist_dx
    points["right_wrist"][1] = points["right_elbow"][1] - wrist_dy

    # Clear screen
    screen.fill(BLACK)

    # Draw all 15 points
    for pos in points.values():
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
