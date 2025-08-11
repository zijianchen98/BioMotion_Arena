
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping Woman")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
amplitude = 40  # Jump height
frequency = 0.05  # Movement speed
arm_amplitude = math.pi / 3  # Arm swing range
leg_amplitude = math.pi / 4  # Leg movement range

# Body dimensions
torso_length = 60
shoulder_width = 35
hip_width = 30
arm_length = 40
upper_leg_length = 45
lower_leg_length = 50

def calculate_positions(t):
    # Body center vertical movement (sine wave)
    body_y = height//2 - amplitude * math.sin(t * frequency)
    body_x = width//2

    # Key joint positions
    head = (body_x, int(body_y - torso_length - 20))
    shoulder_l = (body_x - shoulder_width, int(body_y - torso_length))
    shoulder_r = (body_x + shoulder_width, int(body_y - torso_length))
    hip_l = (body_x - hip_width, int(body_y))
    hip_r = (body_x + hip_width, int(body_y))

    # Arm movements (synchronized with jump)
    arm_phase = math.sin(t * frequency)  # Sync with vertical movement
    elbow_angle = -arm_amplitude * arm_phase
    wrist_angle = elbow_angle * 0.7

    # Left arm
    elbow_l = (
        int(shoulder_l[0] + arm_length * math.cos(elbow_angle)),
        int(shoulder_l[1] + arm_length * math.sin(elbow_angle))
    )
    wrist_l = (
        int(elbow_l[0] + arm_length * math.cos(wrist_angle)),
        int(elbow_l[1] + arm_length * math.sin(wrist_angle))
    )

    # Right arm (mirror left)
    elbow_r = (
        int(shoulder_r[0] + arm_length * math.cos(-elbow_angle)),
        int(shoulder_r[1] + arm_length * math.sin(-elbow_angle))
    )
    wrist_r = (
        int(elbow_r[0] + arm_length * math.cos(-wrist_angle)),
        int(elbow_r[1] + arm_length * math.sin(-wrist_angle))
    )

    # Leg movements (offset phase from arms)
    leg_phase = math.sin(t * frequency + math.pi)  # Opposite phase to body
    knee_angle = leg_amplitude * leg_phase

    # Left leg
    knee_l = (
        int(hip_l[0] + upper_leg_length * math.cos(knee_angle)),
        int(hip_l[1] + upper_leg_length * math.sin(knee_angle))
    )
    ankle_l = (
        int(knee_l[0] + lower_leg_length * math.cos(knee_angle * 0.8)),
        int(knee_l[1] + lower_leg_length * math.sin(knee_angle * 0.8))
    )

    # Right leg
    knee_r = (
        int(hip_r[0] + upper_leg_length * math.cos(-knee_angle)),
        int(hip_r[1] + upper_leg_length * math.sin(-knee_angle))
    )
    ankle_r = (
        int(knee_r[0] + lower_leg_length * math.cos(-knee_angle * 0.8)),
        int(knee_r[1] + lower_leg_length * math.sin(-knee_angle * 0.8))
    )

    # Additional points for natural motion
    neck = (body_x, int(body_y - torso_length))
    chest = (body_x, int(body_y - torso_length//2))
    waist = (body_x, body_y)

    return [
        head, neck, shoulder_l, shoulder_r, elbow_l, wrist_l,
        elbow_r, wrist_r, chest, hip_l, hip_r, knee_l, ankle_l,
        knee_r, ankle_r, waist
    ]

# Main loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    
    # Calculate and draw points
    points = calculate_positions(t)
    for point in points[:15]:  # Ensure exactly 15 points
        pygame.draw.circle(screen, white, point, 5)

    pygame.display.flip()
    clock.tick(30)
    t += 1
