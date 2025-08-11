
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
T = 1.2  # Gait cycle time in seconds (adjusted for heaviness)
scale = 200  # Pixels per unit

# Limb lengths
W_hip = 0.1  # Half width between hips
L_thigh = 0.245
L_shank = 0.245
L_torso = 0.3
W_shoulder = 0.15
L_upper_arm = 0.186
L_forearm = 0.146
L_neck = 0.1
L_head = 0.1

# Angle amplitudes
A_hip = math.radians(20)
B_knee = math.radians(30)
A_arm = math.radians(25)  # Increased for happiness
C_elbow = math.radians(10)
D_vert = 0.03  # Increased for heaviness

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
t = 0  # Time

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update time
    dt = clock.tick(FPS) / 1000.0
    t += dt

    # Compute angles
    omega = 2 * math.pi / T
    theta_hip_R = A_hip * math.sin(omega * t)
    theta_hip_L = A_hip * math.sin(omega * t + math.pi)
    theta_knee_R = B_knee * (1 - math.cos(omega * t))
    theta_knee_L = B_knee * (1 - math.cos(omega * t + math.pi))
    theta_shoulder_R = -A_arm * math.sin(omega * t)
    theta_shoulder_L = -A_arm * math.sin(omega * t + math.pi)
    theta_elbow_R = C_elbow
    theta_elbow_L = C_elbow

    # Compute positions
    x_pelvis = 0
    y_pelvis = -D_vert * math.cos(2 * omega * t)

    # Hips
    x_left_hip = x_pelvis - W_hip
    y_left_hip = y_pelvis
    x_right_hip = x_pelvis + W_hip
    y_right_hip = y_pelvis

    # Knees
    x_left_knee = x_left_hip + L_thigh * math.sin(theta_hip_L)
    y_left_knee = y_left_hip - L_thigh * math.cos(theta_hip_L)
    x_right_knee = x_right_hip + L_thigh * math.sin(theta_hip_R)
    y_right_knee = y_right_hip - L_thigh * math.cos(theta_hip_R)

    # Ankles
    theta_shank_L = theta_hip_L - theta_knee_L
    x_left_ankle = x_left_knee + L_shank * math.sin(theta_shank_L)
    y_left_ankle = y_left_knee - L_shank * math.cos(theta_shank_L)
    theta_shank_R = theta_hip_R - theta_knee_R
    x_right_ankle = x_right_knee + L_shank * math.sin(theta_shank_R)
    y_right_ankle = y_right_knee - L_shank * math.cos(theta_shank_R)

    # Center of shoulders
    x_shoulder_center = x_pelvis
    y_shoulder_center = y_pelvis - L_torso

    # Neck and head
    x_neck = x_shoulder_center
    y_neck = y_shoulder_center - L_neck
    x_head = x_neck
    y_head = y_neck - L_head

    # Shoulders
    x_left_shoulder = x_shoulder_center - W_shoulder
    y_left_shoulder = y_shoulder_center
    x_right_shoulder = x_shoulder_center + W_shoulder
    y_right_shoulder = y_shoulder_center

    # Elbows
    x_left_elbow = x_left_shoulder + L_upper_arm * math.sin(theta_shoulder_L)
    y_left_elbow = y_left_shoulder - L_upper_arm * math.cos(theta_shoulder_L)
    x_right_elbow = x_right_shoulder + L_upper_arm * math.sin(theta_shoulder_R)
    y_right_elbow = y_right_shoulder - L_upper_arm * math.cos(theta_shoulder_R)

    # Wrists
    theta_forearm_L = theta_shoulder_L - theta_elbow_L
    x_left_wrist = x_left_elbow + L_forearm * math.sin(theta_forearm_L)
    y_left_wrist = y_left_elbow - L_forearm * math.cos(theta_forearm_L)
    theta_forearm_R = theta_shoulder_R - theta_elbow_R
    x_right_wrist = x_right_elbow + L_forearm * math.sin(theta_forearm_R)
    y_right_wrist = y_right_elbow - L_forearm * math.cos(theta_forearm_R)

    # Collect all points
    points = [
        (x_pelvis, y_pelvis),
        (x_left_hip, y_left_hip),
        (x_right_hip, y_right_hip),
        (x_left_knee, y_left_knee),
        (x_right_knee, y_right_knee),
        (x_left_ankle, y_left_ankle),
        (x_right_ankle, y_right_ankle),
        (x_shoulder_center, y_shoulder_center),
        (x_neck, y_neck),
        (x_head, y_head),
        (x_left_shoulder, y_left_shoulder),
        (x_right_shoulder, y_right_shoulder),
        (x_left_elbow, y_left_elbow),
        (x_right_elbow, y_right_elbow),
        (x_left_wrist, y_left_wrist),
        (x_right_wrist, y_right_wrist),
    ]

    # Adjust x-positions to center the motion
    avg_x_ankles = (x_left_ankle + x_right_ankle) / 2
    points = [(x - avg_x_ankles, y) for x, y in points]

    # Map to screen coordinates
    screen_points = [(WIDTH / 2 + scale * x, HEIGHT / 2 - scale * y) for x, y in points]

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw points
    for px, py in screen_points:
        pygame.draw.circle(screen, (255, 255, 255), (int(px), int(py)), 5)

    # Update display
    pygame.display.flip()

pygame.quit()
