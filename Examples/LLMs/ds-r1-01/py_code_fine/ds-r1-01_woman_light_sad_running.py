
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
fps = 30
speed = 0.8  # Slower speed for sad motion
amplitude_arm = math.pi/8  # Reduced arm swing
amplitude_leg = math.pi/6   # Reduced leg lift
frequency = 0.4  # Slower step frequency
torso_bob_amplitude = 5    # Reduced vertical movement

# Limb lengths
upper_arm_length = 30
lower_arm_length = 25
upper_leg_length = 40
lower_leg_length = 35
shoulder_width = 20
hip_width = 25

# Initial torso position
torso_x = width // 2
torso_y = height // 2

# Main loop
t = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Update time parameter
    t += 1/fps * speed

    # Calculate vertical torso movement
    torso_y_current = torso_y + torso_bob_amplitude * math.sin(2 * math.pi * frequency * t)

    # Calculate limb angles with phase relationships
    # Arms (opposite phase)
    left_upper_arm_angle = amplitude_arm * math.sin(2 * math.pi * frequency * t)
    right_upper_arm_angle = -left_upper_arm_angle
    
    # Legs (opposite phase with offset)
    leg_phase_offset = math.pi/2  # For more natural gait
    left_upper_leg_angle = amplitude_leg * math.sin(2 * math.pi * frequency * t + leg_phase_offset)
    right_upper_leg_angle = -left_upper_leg_angle

    # Calculate joint positions
    # Head and neck (forward head position for sad posture)
    head_pos = (torso_x, torso_y_current - 40)
    neck_pos = (torso_x, torso_y_current - 25)

    # Shoulders with forward slump
    left_shoulder_pos = (torso_x - shoulder_width, torso_y_current - 15)
    right_shoulder_pos = (torso_x + shoulder_width, torso_y_current - 15)

    # Arms with elbow bend
    left_elbow_pos = (
        left_shoulder_pos[0] + upper_arm_length * math.cos(left_upper_arm_angle),
        left_shoulder_pos[1] + upper_arm_length * math.sin(left_upper_arm_angle)
    )
    left_hand_pos = (
        left_elbow_pos[0] + lower_arm_length * math.cos(left_upper_arm_angle * 0.7),
        left_elbow_pos[1] + lower_arm_length * math.sin(left_upper_arm_angle * 0.7)
    )

    right_elbow_pos = (
        right_shoulder_pos[0] + upper_arm_length * math.cos(right_upper_arm_angle),
        right_shoulder_pos[1] + upper_arm_length * math.sin(right_upper_arm_angle)
    )
    right_hand_pos = (
        right_elbow_pos[0] + lower_arm_length * math.cos(right_upper_arm_angle * 0.7),
        right_elbow_pos[1] + lower_arm_length * math.sin(right_upper_arm_angle * 0.7)
    )

    # Hips with wider stance
    left_hip_pos = (torso_x - hip_width, torso_y_current + 25)
    right_hip_pos = (torso_x + hip_width, torso_y_current + 25)

    # Legs with knee bend
    left_knee_pos = (
        left_hip_pos[0] + upper_leg_length * math.cos(left_upper_leg_angle),
        left_hip_pos[1] + upper_leg_length * math.sin(left_upper_leg_angle)
    )
    left_ankle_pos = (
        left_knee_pos[0] + lower_leg_length * math.cos(left_upper_leg_angle * 1.2),
        left_knee_pos[1] + lower_leg_length * math.sin(left_upper_leg_angle * 1.2)
    )

    right_knee_pos = (
        right_hip_pos[0] + upper_leg_length * math.cos(right_upper_leg_angle),
        right_hip_pos[1] + upper_leg_length * math.sin(right_upper_leg_angle)
    )
    right_ankle_pos = (
        right_knee_pos[0] + lower_leg_length * math.cos(right_upper_leg_angle * 1.2),
        right_knee_pos[1] + lower_leg_length * math.sin(right_upper_leg_angle * 1.2)
    )

    # Torso points
    lower_torso_pos = (torso_x, torso_y_current + 20)

    # Create list of all 15 points
    points = [
        head_pos, neck_pos, left_shoulder_pos, right_shoulder_pos,
        left_elbow_pos, right_elbow_pos, left_hand_pos, right_hand_pos,
        lower_torso_pos, left_hip_pos, right_hip_pos, left_knee_pos,
        right_knee_pos, left_ankle_pos, right_ankle_pos
    ]

    # Draw all points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
