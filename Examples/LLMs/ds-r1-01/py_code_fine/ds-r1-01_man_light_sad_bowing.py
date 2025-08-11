
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
max_angle = math.radians(30)  # Maximum torso bend angle
period = 2.0  # Animation cycle duration in seconds
fps = 30  # Frames per second
clock = pygame.time.Clock()

# Body dimensions
torso_length = 100
head_offset = 20  # Vertical distance from shoulders to head
shoulder_width = 50
hip_width = 40
upper_arm_length = 40
lower_arm_length = 30
upper_leg_length = 50
lower_leg_length = 50

def compute_positions(theta):
    """Calculate joint positions based on torso angle"""
    hip_x = width // 2
    hip_y = height - 50  # Base vertical position

    # Torso calculations
    torso_dx = torso_length * math.sin(theta)
    torso_dy = torso_length * math.cos(theta)
    shoulders_x = hip_x + torso_dx
    shoulders_y = hip_y - torso_dy

    # Head position
    head_x = shoulders_x
    head_y = shoulders_y - head_offset

    # Shoulders
    left_shoulder = (shoulders_x - shoulder_width/2, shoulders_y)
    right_shoulder = (shoulders_x + shoulder_width/2, shoulders_y)

    # Arms (swing back during bow)
    arm_angle = -theta * 1.2  # Increased swing for natural movement
    left_elbow = (
        left_shoulder[0] + upper_arm_length * math.sin(arm_angle),
        left_shoulder[1] + upper_arm_length * math.cos(arm_angle)
    )
    right_elbow = (
        right_shoulder[0] + upper_arm_length * math.sin(arm_angle),
        right_shoulder[1] + upper_arm_length * math.cos(arm_angle)
    )
    left_hand = (
        left_elbow[0] + lower_arm_length * math.sin(arm_angle),
        left_elbow[1] + lower_arm_length * math.cos(arm_angle)
    )
    right_hand = (
        right_elbow[0] + lower_arm_length * math.sin(arm_angle),
        right_elbow[1] + lower_arm_length * math.cos(arm_angle)
    )

    # Hips
    left_hip = (hip_x - hip_width/2, hip_y)
    right_hip = (hip_x + hip_width/2, hip_y)

    # Legs (slight knee bend during bow)
    leg_angle = theta * 0.6
    left_knee = (
        left_hip[0] + upper_leg_length * math.sin(leg_angle),
        left_hip[1] + upper_leg_length * math.cos(leg_angle)
    )
    right_knee = (
        right_hip[0] + upper_leg_length * math.sin(leg_angle),
        right_hip[1] + upper_leg_length * math.cos(leg_angle)
    )
    left_ankle = (
        left_knee[0] + lower_leg_length * math.sin(leg_angle),
        left_knee[1] + lower_leg_length * math.cos(leg_angle)
    )
    right_ankle = (
        right_knee[0] + lower_leg_length * math.sin(leg_angle),
        right_knee[1] + lower_leg_length * math.cos(leg_angle)
    )

    # Spine points
    mid_spine = (hip_x + torso_dx/2, hip_y - torso_dy/2)
    lower_spine = (hip_x, hip_y + 20)

    return [
        (int(head_x), int(head_y)),
        (int(left_shoulder[0]), int(left_shoulder[1])),
        (int(right_shoulder[0]), int(right_shoulder[1])),
        (int(left_elbow[0]), int(left_elbow[1])),
        (int(right_elbow[0]), int(right_elbow[1])),
        (int(left_hand[0]), int(left_hand[1])),
        (int(right_hand[0]), int(right_hand[1])),
        (int(left_hip[0]), int(left_hip[1])),
        (int(right_hip[0]), int(right_hip[1])),
        (int(left_knee[0]), int(left_knee[1])),
        (int(right_knee[0]), int(right_knee[1])),
        (int(left_ankle[0]), int(left_ankle[1])),
        (int(right_ankle[0]), int(right_ankle[1])),
        (int(mid_spine[0]), int(mid_spine[1])),
        (int(lower_spine[0]), int(lower_spine[1]))
    ]

# Main animation loop
time_elapsed = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Calculate current torso angle
    theta = max_angle * math.sin(2 * math.pi * time_elapsed / period)
    
    # Get and draw points
    points = compute_positions(theta)
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    pygame.display.flip()
    time_elapsed += 1/fps
    clock.tick(fps)

pygame.quit()
sys.exit()
