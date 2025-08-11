
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
hip_offset = 20
thigh_length = 40
lower_leg_length = 35
upper_arm_length = 30
lower_arm_length = 25
shoulder_offset = 30
torso_offset = 40
head_offset = 20
thigh_amplitude = math.pi / 4
thigh_speed = 5
arm_amplitude = math.pi / 3
arm_speed = thigh_speed
bounce_amplitude = 5
bounce_speed = 5
forward_speed = 2

# Initialize time
t = 0

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    t += 0.05

    # Calculate mid-hip position with bounce
    mid_hip_x = 200 + t * forward_speed
    mid_hip_y = height//2 + bounce_amplitude * math.sin(t * bounce_speed)

    # Torso and shoulders
    torso_x = mid_hip_x
    torso_y = mid_hip_y - torso_offset
    left_shoulder = (torso_x - shoulder_offset, torso_y)
    right_shoulder = (torso_x + shoulder_offset, torso_y)
    head = (torso_x, torso_y - head_offset)

    # Hips
    left_hip = (mid_hip_x - hip_offset, mid_hip_y)
    right_hip = (mid_hip_x + hip_offset, mid_hip_y)

    # Leg calculations
    thigh_angle_left = thigh_amplitude * math.sin(t * thigh_speed)
    thigh_angle_right = thigh_amplitude * math.sin(t * thigh_speed + math.pi)
    
    left_knee = (
        left_hip[0] + thigh_length * math.cos(thigh_angle_left),
        left_hip[1] + thigh_length * math.sin(thigh_angle_left)
    )
    right_knee = (
        right_hip[0] + thigh_length * math.cos(thigh_angle_right),
        right_hip[1] + thigh_length * math.sin(thigh_angle_right)
    )
    
    lower_leg_angle_left = thigh_angle_left - math.pi/2
    lower_leg_angle_right = thigh_angle_right - math.pi/2
    
    left_ankle = (
        left_knee[0] + lower_leg_length * math.cos(lower_leg_angle_left),
        left_knee[1] + lower_leg_length * math.sin(lower_leg_angle_left)
    )
    right_ankle = (
        right_knee[0] + lower_leg_length * math.cos(lower_leg_angle_right),
        right_knee[1] + lower_leg_length * math.sin(lower_leg_angle_right)
    )

    # Arm calculations
    arm_phase = math.pi
    upper_arm_angle_left = arm_amplitude * math.sin(t * arm_speed + arm_phase)
    upper_arm_angle_right = arm_amplitude * math.sin(t * arm_speed + arm_phase + math.pi)
    
    left_elbow = (
        left_shoulder[0] + upper_arm_length * math.cos(upper_arm_angle_left),
        left_shoulder[1] + upper_arm_length * math.sin(upper_arm_angle_left)
    )
    right_elbow = (
        right_shoulder[0] + upper_arm_length * math.cos(upper_arm_angle_right),
        right_shoulder[1] + upper_arm_length * math.sin(upper_arm_angle_right)
    )
    
    lower_arm_angle_left = upper_arm_angle_left - math.pi/2
    lower_arm_angle_right = upper_arm_angle_right - math.pi/2
    
    left_wrist = (
        left_elbow[0] + lower_arm_length * math.cos(lower_arm_angle_left),
        left_elbow[1] + lower_arm_length * math.sin(lower_arm_angle_left)
    )
    right_wrist = (
        right_elbow[0] + lower_arm_length * math.cos(lower_arm_angle_right),
        right_elbow[1] + lower_arm_length * math.sin(lower_arm_angle_right)
    )

    # Torso point
    torso_point = (torso_x, (torso_y + mid_hip_y) // 2)

    # Create points list
    points = [
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        torso_point,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        (mid_hip_x, mid_hip_y)
    ]

    # Draw all points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    clock.tick(30)

    # Reset position when off screen
    if mid_hip_x > width + 100:
        t = 0

pygame.quit()
sys.exit()
