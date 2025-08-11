
import pygame
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Set up the clock
clock = pygame.time.Clock()
FPS = 30

# Define segment lengths
l_torso = 100
l_head = 20
l_upper_arm = 50
l_forearm = 50
l_thigh = 60
l_shin = 60
w_shoulder = 20
w_hip = 20

# Define maximum angles
theta_head_max = 90 * math.pi / 180  # 90 degrees in radians

# Animation parameters
animation_duration = 2  # seconds for one cycle
t = 0  # time variable

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Compute theta_p
    theta_p = (t / animation_duration) * 2 * math.pi
    # Compute curling factor
    curling = (1 - math.cos(theta_p)) / 2

    # Compute joint angles
    theta_head = theta_head_max * curling
    theta_shoulder_left = (180 - 90 * curling) * math.pi / 180
    theta_elbow_left = 90 * curling * math.pi / 180
    theta_shoulder_right = (180 - 90 * curling) * math.pi / 180
    theta_elbow_right = 90 * curling * math.pi / 180
    theta_hip_left = (180 - 90 * curling) * math.pi / 180
    theta_knee_left = 90 * curling * math.pi / 180
    theta_hip_right = (180 - 90 * curling) * math.pi / 180
    theta_knee_right = 90 * curling * math.pi / 180

    # Compute positions
    pelvis = (400, 300)
    neck = (pelvis[0] + l_torso * math.sin(theta_p), pelvis[1] - l_torso * math.cos(theta_p))
    head = (neck[0] + l_head * math.sin(theta_p + theta_head), neck[1] - l_head * math.cos(theta_p + theta_head))
    left_shoulder = (neck[0] - w_shoulder * math.cos(theta_p), neck[1] - w_shoulder * math.sin(theta_p))
    right_shoulder = (neck[0] + w_shoulder * math.cos(theta_p), neck[1] + w_shoulder * math.sin(theta_p))
    left_elbow = (left_shoulder[0] + l_upper_arm * math.sin(theta_p + theta_shoulder_left), left_shoulder[1] - l_upper_arm * math.cos(theta_p + theta_shoulder_left))
    right_elbow = (right_shoulder[0] + l_upper_arm * math.sin(theta_p + theta_shoulder_right), right_shoulder[1] - l_upper_arm * math.cos(theta_p + theta_shoulder_right))
    left_wrist = (left_elbow[0] + l_forearm * math.sin(theta_p + theta_shoulder_left + theta_elbow_left), left_elbow[1] - l_forearm * math.cos(theta_p + theta_shoulder_left + theta_elbow_left))
    right_wrist = (right_elbow[0] + l_forearm * math.sin(theta_p + theta_shoulder_right + theta_elbow_right), right_elbow[1] - l_forearm * math.cos(theta_p + theta_shoulder_right + theta_elbow_right))
    left_hip = (pelvis[0] - w_hip * math.cos(theta_p), pelvis[1] - w_hip * math.sin(theta_p))
    right_hip = (pelvis[0] + w_hip * math.cos(theta_p), pelvis[1] + w_hip * math.sin(theta_p))
    left_knee = (left_hip[0] + l_thigh * math.sin(theta_p + theta_hip_left), left_hip[1] - l_thigh * math.cos(theta_p + theta_hip_left))
    right_knee = (right_hip[0] + l_thigh * math.sin(theta_p + theta_hip_right), right_hip[1] - l_thigh * math.cos(theta_p + theta_hip_right))
    left_ankle = (left_knee[0] + l_shin * math.sin(theta_p + theta_hip_left + theta_knee_left), left_knee[1] - l_shin * math.cos(theta_p + theta_hip_left + theta_knee_left))
    right_ankle = (right_knee[0] + l_shin * math.sin(theta_p + theta_hip_right + theta_knee_right), right_knee[1] - l_shin * math.cos(theta_p + theta_hip_right + theta_knee_right))

    # List of points
    points = [head, neck, pelvis, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle]

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw points
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 5)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

    # Update time
    t += 1 / FPS
    if t >= animation_duration:
        t = 0  # loop the animation

# Quit Pygame
pygame.quit()
