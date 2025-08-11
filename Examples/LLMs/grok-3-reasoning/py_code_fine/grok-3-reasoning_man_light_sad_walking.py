
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
T = 2.0  # Period in seconds
A = 0.35  # Hip angle amplitude in radians
G = 0.17  # Shoulder angle amplitude in radians
K = 0.52  # Knee angle amplitude in radians
L_upper_arm = 0.2
L_forearm = 0.2
L_thigh = 0.25
L_shank = 0.25
s = 400  # Scale factor

def compute_positions(t):
    theta_hip_left = A * math.sin(2 * math.pi * t / T)
    theta_hip_right = A * math.sin(2 * math.pi * (t / T + 0.5))
    theta_knee_left = K * (1 - math.cos(4 * math.pi * t / T)) / 2
    theta_knee_right = K * (1 - math.cos(4 * math.pi * (t / T + 0.5))) / 2
    theta_shoulder_left = -G * math.sin(2 * math.pi * t / T)
    theta_shoulder_right = G * math.sin(2 * math.pi * t / T)

    torso = (0, 0)
    neck = (0, 0.2)
    head = (0, 0.35)
    left_shoulder = (-0.1, 0.2)
    right_shoulder = (0.1, 0.2)
    left_hip = (-0.05, -0.1)
    right_hip = (0.05, -0.1)

    left_elbow = (left_shoulder[0] + L_upper_arm * math.sin(theta_shoulder_left),
                  left_shoulder[1] - L_upper_arm * math.cos(theta_shoulder_left))
    left_wrist = (left_elbow[0] + L_forearm * math.sin(theta_shoulder_left),
                  left_elbow[1] - L_forearm * math.cos(theta_shoulder_left))
    right_elbow = (right_shoulder[0] + L_upper_arm * math.sin(theta_shoulder_right),
                   right_shoulder[1] - L_upper_arm * math.cos(theta_shoulder_right))
    right_wrist = (right_elbow[0] + L_forearm * math.sin(theta_shoulder_right),
                   right_elbow[1] - L_forearm * math.cos(theta_shoulder_right))

    left_knee = (left_hip[0] + L_thigh * math.sin(theta_hip_left),
                 left_hip[1] - L_thigh * math.cos(theta_hip_left))
    left_ankle = (left_knee[0] + L_shank * math.sin(theta_hip_left - theta_knee_left),
                  left_knee[1] - L_shank * math.cos(theta_hip_left - theta_knee_left))
    right_knee = (right_hip[0] + L_thigh * math.sin(theta_hip_right),
                  right_hip[1] - L_thigh * math.cos(theta_hip_right))
    right_ankle = (right_knee[0] + L_shank * math.sin(theta_hip_right - theta_knee_right),
                   right_knee[1] - L_shank * math.cos(theta_hip_right - theta_knee_right))

    points = [head, neck, torso, left_shoulder, left_elbow, left_wrist, right_shoulder, right_elbow, right_wrist, left_hip, left_knee, left_ankle, right_hip, right_knee, right_ankle]
    return points

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    current_time = 0
    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0
        current_time += delta_time
        t = current_time % T
        points = compute_positions(t)
        screen.fill((0, 0, 0))
        for point in points:
            screen_x = WIDTH / 2 + s * point[0]
            screen_y = HEIGHT / 2 + s * point[1]
            pygame.draw.circle(screen, (255, 255, 255), (int(screen_x), int(screen_y)), 5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
