
import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Scale factor
scale = 200

# Constants
hip_width = 0.2
shoulder_width = 0.3
shoulder_height = 0.4
head_height = 0.6
l_thigh = 0.4
l_shank = 0.4
l_foot = 0.1
l_upper_arm = 0.3
l_forearm = 0.3

# Key frames
key_frames = [
    {'t': 0.0, 'y_pelvis': 1.0, 'theta_hip_left': 0, 'theta_hip_right': 0, 'theta_knee_left': 0, 'theta_knee_right': 0, 'theta_ankle_left': 0, 'theta_ankle_right': 0, 'theta_shoulder_left': 0, 'theta_shoulder_right': 0, 'theta_elbow_left': 0, 'theta_elbow_right': 0},
    {'t': 0.3, 'y_pelvis': 0.8, 'theta_hip_left': math.radians(30), 'theta_hip_right': math.radians(-30), 'theta_knee_left': math.radians(60), 'theta_knee_right': math.radians(60), 'theta_ankle_left': math.radians(-10), 'theta_ankle_right': math.radians(-10), 'theta_shoulder_left': math.radians(-30), 'theta_shoulder_right': math.radians(-30), 'theta_elbow_left': math.radians(30), 'theta_elbow_right': math.radians(30)},
    {'t': 0.4, 'y_pelvis': 1.3, 'theta_hip_left': 0, 'theta_hip_right': 0, 'theta_knee_left': 0, 'theta_knee_right': 0, 'theta_ankle_left': 0, 'theta_ankle_right': 0, 'theta_shoulder_left': math.radians(30), 'theta_shoulder_right': math.radians(30), 'theta_elbow_left': 0, 'theta_elbow_right': 0},
    {'t': 0.5, 'y_pelvis': 1.3, 'theta_hip_left': 0, 'theta_hip_right': 0, 'theta_knee_left': 0, 'theta_knee_right': 0, 'theta_ankle_left': 0, 'theta_ankle_right': 0, 'theta_shoulder_left': math.radians(30), 'theta_shoulder_right': math.radians(30), 'theta_elbow_left': 0, 'theta_elbow_right': 0},
    {'t': 0.6, 'y_pelvis': 1.0, 'theta_hip_left': math.radians(30), 'theta_hip_right': math.radians(-30), 'theta_knee_left': math.radians(60), 'theta_knee_right': math.radians(60), 'theta_ankle_left': math.radians(-10), 'theta_ankle_right': math.radians(-10), 'theta_shoulder_left': 0, 'theta_shoulder_right': 0, 'theta_elbow_left': 0, 'theta_elbow_right': 0},
    {'t': 0.7, 'y_pelvis': 0.8, 'theta_hip_left': math.radians(30), 'theta_hip_right': math.radians(-30), 'theta_knee_left': math.radians(60), 'theta_knee_right': math.radians(60), 'theta_ankle_left': math.radians(-10), 'theta_ankle_right': math.radians(-10), 'theta_shoulder_left': 0, 'theta_shoulder_right': 0, 'theta_elbow_left': 0, 'theta_elbow_right': 0},
    {'t': 1.0, 'y_pelvis': 1.0, 'theta_hip_left': 0, 'theta_hip_right': 0, 'theta_knee_left': 0, 'theta_knee_right': 0, 'theta_ankle_left': 0, 'theta_ankle_right': 0, 'theta_shoulder_left': 0, 'theta_shoulder_right': 0, 'theta_elbow_left': 0, 'theta_elbow_right': 0},
]

# Period of the animation
T = 2.0  # seconds

def interpolate_keyframes(t, key_frames):
    for i in range(len(key_frames) - 1):
        if key_frames[i]['t'] <= t < key_frames[i+1]['t']:
            break
    else:
        i = len(key_frames) - 2
    t0 = key_frames[i]['t']
    t1 = key_frames[i+1]['t']
    alpha = (t - t0) / (t1 - t0) if t1 > t0 else 0
    interpolated = {}
    for key in key_frames[i].keys():
        if key != 't':
            val0 = key_frames[i][key]
            val1 = key_frames[i+1][key]
            interpolated[key] = val0 * (1 - alpha) + val1 * alpha
    return interpolated

def compute_positions(params):
    y_pelvis = params['y_pelvis']
    theta_hip_left = params['theta_hip_left']
    theta_hip_right = params['theta_hip_right']
    theta_knee_left = params['theta_knee_left']
    theta_knee_right = params['theta_knee_right']
    theta_ankle_left = params['theta_ankle_left']
    theta_ankle_right = params['theta_ankle_right']
    theta_shoulder_left = params['theta_shoulder_left']
    theta_shoulder_right = params['theta_shoulder_right']
    theta_elbow_left = params['theta_elbow_left']
    theta_elbow_right = params['theta_elbow_right']

    pelvis = (0, y_pelvis)
    left_hip = (pelvis[0] - hip_width / 2, pelvis[1])
    right_hip = (pelvis[0] + hip_width / 2, pelvis[1])
    left_shoulder = (pelvis[0] - shoulder_width / 2, pelvis[1] + shoulder_height)
    right_shoulder = (pelvis[0] + shoulder_width / 2, pelvis[1] + shoulder_height)
    head = (pelvis[0], pelvis[1] + head_height)

    # Left leg
    left_knee = (left_hip[0] + l_thigh * math.sin(theta_hip_left), left_hip[1] - l_thigh * math.cos(theta_hip_left))
    left_ankle = (left_knee[0] + l_shank * math.sin(theta_hip_left + theta_knee_left), left_knee[1] - l_shank * math.cos(theta_hip_left + theta_knee_left))
    left_toe = (left_ankle[0] + l_foot * math.cos(theta_ankle_left), left_ankle[1] + l_foot * math.sin(theta_ankle_left))

    # Right leg
    right_knee = (right_hip[0] + l_thigh * math.sin(theta_hip_right), right_hip[1] - l_thigh * math.cos(theta_hip_right))
    right_ankle = (right_knee[0] + l_shank * math.sin(theta_hip_right + theta_knee_right), right_knee[1] - l_shank * math.cos(theta_hip_right + theta_knee_right))
    right_toe = (right_ankle[0] + l_foot * math.cos(theta_ankle_right), right_ankle[1] + l_foot * math.sin(theta_ankle_right))

    # Left arm
    left_elbow = (left_shoulder[0] + l_upper_arm * math.sin(theta_shoulder_left), left_shoulder[1] - l_upper_arm * math.cos(theta_shoulder_left))
    left_wrist = (left_elbow[0] + l_forearm * math.sin(theta_shoulder_left + theta_elbow_left), left_elbow[1] - l_forearm * math.cos(theta_shoulder_left + theta_elbow_left))

    # Right arm
    right_elbow = (right_shoulder[0] + l_upper_arm * math.sin(theta_shoulder_right), right_shoulder[1] - l_upper_arm * math.cos(theta_shoulder_right))
    right_wrist = (right_elbow[0] + l_forearm * math.sin(theta_shoulder_right + theta_elbow_right), right_elbow[1] - l_forearm * math.cos(theta_shoulder_right + theta_elbow_right))

    points = [
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        left_toe,
        right_toe
    ]
    return points

# Main loop
clock = pygame.time.Clock()
running = True
start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()
    t = ((current_time - start_time) % T) / T
    interpolated = interpolate_keyframes(t, key_frames)
    points = compute_positions(interpolated)

    screen.fill(BLACK)
    for point in points:
        screen_x = width / 2 + point[0] * scale
        screen_y = height / 2 - point[1] * scale
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
