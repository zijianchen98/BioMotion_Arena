
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_RADIUS = 5
NUM_POINTS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Limb lengths (in pixels)
L_head = 20
L_torso = 50
L_upper_arm = 30
L_forearm = 30
L_thigh = 40
L_shin = 40
L_foot = 10

# Joint angles (in degrees)
theta_max_knee = 60  # Maximum knee bend during crouch

# Motion parameters
T = 2.0  # Period of one jump cycle in seconds
A = 50  # Amplitude of hip motion
y0 = 300  # Base y-position of hips

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")
clock = pygame.time.Clock()

def calculate_positions(t):
    # Calculate hip y-position
    y_hip = y0 - A * (1 - math.cos(2 * math.pi * t / T)) / 2
    x_hip = WIDTH / 2

    # Calculate joint angles
    cos_term = math.cos(2 * math.pi * t / T)
    theta_knee = theta_max_knee * (1 - cos_term) / 2
    theta_ankle = 0  # Keep ankles straight for simplicity
    theta_hip = 0  # Keep hips straight for simplicity
    theta_shoulder = -90 * (1 - cos_term) / 2  # Arms raise during jump
    theta_elbow = 20  # Slight bend in elbows

    # Convert angles to radians
    rad = math.radians
    theta_knee = rad(theta_knee)
    theta_ankle = rad(theta_ankle)
    theta_hip = rad(theta_hip)
    theta_shoulder = rad(theta_shoulder)
    theta_elbow = rad(theta_elbow)

    # Define points
    points = []

    # Hips
    hips = (x_hip, y_hip)
    points.append(hips)

    # Left leg
    left_knee = (hips[0] + L_thigh * math.sin(theta_hip), hips[1] + L_thigh * math.cos(theta_hip))
    left_ankle = (left_knee[0] + L_shin * math.sin(theta_knee), left_knee[1] + L_shin * math.cos(theta_knee))
    left_toe = (left_ankle[0] + L_foot * math.sin(theta_ankle), left_ankle[1] + L_foot * math.cos(theta_ankle))
    points.extend([left_knee, left_ankle, left_toe])

    # Right leg (symmetric to left leg)
    right_knee = (hips[0] - L_thigh * math.sin(theta_hip), hips[1] + L_thigh * math.cos(theta_hip))
    right_ankle = (right_knee[0] - L_shin * math.sin(theta_knee), right_knee[1] + L_shin * math.cos(theta_knee))
    right_toe = (right_ankle[0] - L_foot * math.sin(theta_ankle), right_ankle[1] + L_foot * math.cos(theta_ankle))
    points.extend([right_knee, right_ankle, right_toe])

    # Torso and head
    neck = (x_hip, y_hip - L_torso)
    head = (neck[0], neck[1] - L_head)
    points.extend([neck, head])

    # Left arm
    left_shoulder = (neck[0] - 10, neck[1])  # Slightly offset from neck
    left_elbow = (left_shoulder[0] + L_upper_arm * math.sin(theta_shoulder), left_shoulder[1] + L_upper_arm * math.cos(theta_shoulder))
    left_wrist = (left_elbow[0] + L_forearm * math.sin(theta_elbow), left_elbow[1] + L_forearm * math.cos(theta_elbow))
    points.extend([left_shoulder, left_elbow, left_wrist])

    # Right arm (symmetric to left arm)
    right_shoulder = (neck[0] + 10, neck[1])  # Slightly offset from neck
    right_elbow = (right_shoulder[0] - L_upper_arm * math.sin(theta_shoulder), right_shoulder[1] + L_upper_arm * math.cos(theta_shoulder))
    right_wrist = (right_elbow[0] - L_forearm * math.sin(theta_elbow), right_elbow[1] + L_forearm * math.cos(theta_elbow))
    points.extend([right_shoulder, right_elbow, right_wrist])

    return points

running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current positions
    points = calculate_positions(t)

    # Clear screen
    screen.fill(BLACK)

    # Draw points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Update time
    t += 1 / FPS
    if t >= T:
        t = 0

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
