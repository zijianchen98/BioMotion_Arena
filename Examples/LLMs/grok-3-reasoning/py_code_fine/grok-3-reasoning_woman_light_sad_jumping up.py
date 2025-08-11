
import pygame
import math
import time

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Constants
L_torso = 50
L_neck = 10
L_head = 5
L_upper_arm = 30
L_lower_arm = 30
L_thigh = 40
L_shin = 40
shoulder_width = 20
hip_width = 20

# Key frames for animation
keyframes = [
    {'frame': 0, 'y_waist': 0, 'θ_thigh_left': 0, 'θ_shin_left': 0, 'θ_upper_arm_left': 0, 'θ_lower_arm_left': 0,
     'θ_thigh_right': 0, 'θ_shin_right': 0, 'θ_upper_arm_right': 0, 'θ_lower_arm_right': 0},
    {'frame': 10, 'y_waist': -20, 'θ_thigh_left': 30, 'θ_shin_left': -60, 'θ_upper_arm_left': 20, 'θ_lower_arm_left': 0,
     'θ_thigh_right': -30, 'θ_shin_right': 60, 'θ_upper_arm_right': -20, 'θ_lower_arm_right': 0},
    {'frame': 15, 'y_waist': 0, 'θ_thigh_left': 0, 'θ_shin_left': 0, 'θ_upper_arm_left': 45, 'θ_lower_arm_left': 0,
     'θ_thigh_right': 0, 'θ_shin_right': 0, 'θ_upper_arm_right': -45, 'θ_lower_arm_right': 0},
    {'frame': 30, 'y_waist': 50, 'θ_thigh_left': 0, 'θ_shin_left': 0, 'θ_upper_arm_left': 0, 'θ_lower_arm_left': 0,
     'θ_thigh_right': 0, 'θ_shin_right': 0, 'θ_upper_arm_right': 0, 'θ_lower_arm_right': 0},
    {'frame': 45, 'y_waist': 0, 'θ_thigh_left': 0, 'θ_shin_left': 0, 'θ_upper_arm_left': 45, 'θ_lower_arm_left': 0,
     'θ_thigh_right': 0, 'θ_shin_right': 0, 'θ_upper_arm_right': -45, 'θ_lower_arm_right': 0},
    {'frame': 60, 'y_waist': 0, 'θ_thigh_left': 0, 'θ_shin_left': 0, 'θ_upper_arm_left': 0, 'θ_lower_arm_left': 0,
     'θ_thigh_right': 0, 'θ_shin_right': 0, 'θ_upper_arm_right': 0, 'θ_lower_arm_right': 0},
]

total_frames = 60
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ground_y = 550

# Interpolation function
def interpolate_keyframes(keyframes, f):
    for i in range(len(keyframes) - 1):
        if keyframes[i]['frame'] <= f <= keyframes[i+1]['frame']:
            t = (f - keyframes[i]['frame']) / (keyframes[i+1]['frame'] - keyframes[i]['frame'])
            interpolated = {}
            for key in keyframes[i]:
                if key != 'frame':
                    val0 = keyframes[i][key]
                    val1 = keyframes[i+1][key]
                    interpolated[key] = val0 + t * (val1 - val0)
            return interpolated
    if f == keyframes[-1]['frame']:
        return {k: v for k, v in keyframes[-1].items() if k != 'frame'}
    return None

# Function to compute positions of points
def compute_positions(values):
    y_waist = values['y_waist']
    P_waist = (0, y_waist)
    P_shoulders = (P_waist[0], P_waist[1] + L_torso)
    P_neck = (P_shoulders[0], P_shoulders[1] + L_neck)
    P_head = (P_neck[0], P_neck[1] + L_head)

    # Left arm
    θ_upper_arm_left = math.radians(values['θ_upper_arm_left'])
    θ_lower_arm_left = math.radians(values['θ_lower_arm_left'])
    P_left_shoulder = (P_shoulders[0] - shoulder_width / 2, P_shoulders[1])
    P_left_elbow = (P_left_shoulder[0] + L_upper_arm * math.sin(θ_upper_arm_left),
                   P_left_shoulder[1] - L_upper_arm * math.cos(θ_upper_arm_left))
    P_left_wrist = (P_left_elbow[0] + L_lower_arm * math.sin(θ_lower_arm_left),
                    P_left_elbow[1] - L_lower_arm * math.cos(θ_lower_arm_left))

    # Right arm
    θ_upper_arm_right = math.radians(values['θ_upper_arm_right'])
    θ_lower_arm_right = math.radians(values['θ_lower_arm_right'])
    P_right_shoulder = (P_shoulders[0] + shoulder_width / 2, P_shoulders[1])
    P_right_elbow = (P_right_shoulder[0] + L_upper_arm * math.sin(θ_upper_arm_right),
                    P_right_shoulder[1] - L_upper_arm * math.cos(θ_upper_arm_right))
    P_right_wrist = (P_right_elbow[0] + L_lower_arm * math.sin(θ_lower_arm_right),
                     P_right_elbow[1] - L_lower_arm * math.cos(θ_lower_arm_right))

    # Left leg
    θ_thigh_left = math.radians(values['θ_thigh_left'])
    θ_shin_left = math.radians(values['θ_shin_left'])
    P_left_hip = (P_waist[0] - hip_width / 2, P_waist[1])
    P_left_knee = (P_left_hip[0] + L_thigh * math.sin(θ_thigh_left),
                   P_left_hip[1] - L_thigh * math.cos(θ_thigh_left))
    P_left_ankle = (P_left_knee[0] + L_shin * math.sin(θ_shin_left),
                    P_left_knee[1] - L_shin * math.cos(θ_shin_left))

    # Right leg
    θ_thigh_right = math.radians(values['θ_thigh_right'])
    θ_shin_right = math.radians(values['θ_shin_right'])
    P_right_hip = (P_waist[0] + hip_width / 2, P_waist[1])
    P_right_knee = (P_right_hip[0] + L_thigh * math.sin(θ_thigh_right),
                    P_right_hip[1] - L_thigh * math.cos(θ_thigh_right))
    P_right_ankle = (P_right_knee[0] + L_shin * math.sin(θ_shin_right),
                     P_right_knee[1] - L_shin * math.cos(θ_shin_right))

    # Collect all points
    points = [
        P_head, P_neck, P_left_shoulder, P_right_shoulder, P_left_elbow, P_right_elbow,
        P_left_wrist, P_right_wrist, P_waist, P_left_hip, P_right_hip, P_left_knee,
        P_right_knee, P_left_ankle, P_right_ankle
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
    elapsed = current_time - start_time
    f = (elapsed * FPS) % total_frames
    values = interpolate_keyframes(keyframes, f)

    if values is not None:
        points = compute_positions(values)
        screen.fill(BLACK)
        for point in points:
            screen_x = width / 2 + point[0]
            screen_y = ground_y - point[1]
            pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), 5)
        pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
