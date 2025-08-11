
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sad Woman Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
cycle_duration = 2.0  # Jump cycle duration in seconds
y_peak = 120          # Vertical jump height
x_speed = 150         # Horizontal movement speed (pixels/sec)
shoulder_swing = 40   # Shoulder swing amplitude
arm_swing = 60        # Arm swing amplitude
leg_swing = 50        # Leg swing amplitude

clock = pygame.time.Clock()

def get_body_position(t):
    """Calculate body position using parabolic trajectory"""
    x = width//4 + (x_speed * t) % (width//2)
    normalized_time = (t % cycle_duration) / cycle_duration
    y = height//2 - y_peak * (1 - (2 * normalized_time - 1)**2)
    return x, y

def calculate_points(t, body_x, body_y):
    """Calculate 15 joint positions for the figure"""
    points = []
    phase = 2 * math.pi * (t % cycle_duration) / cycle_duration

    # Head
    points.append((body_x, body_y - 50))

    # Shoulders
    shoulder_offset = shoulder_swing * math.sin(phase)
    points.append((body_x - 25 - shoulder_offset, body_y + 5))
    points.append((body_x + 25 + shoulder_offset, body_y + 5))

    # Elbows
    elbow_phase = phase * 2
    points.append((
        body_x - 45 - shoulder_offset - arm_swing * math.sin(elbow_phase),
        body_y + 30
    ))
    points.append((
        body_x + 45 + shoulder_offset + arm_swing * math.sin(elbow_phase),
        body_y + 30
    ))

    # Wrists
    points.append((
        body_x - 60 - shoulder_offset - arm_swing * math.sin(elbow_phase + math.pi/3),
        body_y + 60
    ))
    points.append((
        body_x + 60 + shoulder_offset + arm_swing * math.sin(elbow_phase + math.pi/3),
        body_y + 60
    ))

    # Hips
    hip_phase = phase + math.pi
    points.append((body_x - 20, body_y + 30))
    points.append((body_x + 20, body_y + 30))

    # Knees
    knee_phase = phase * 1.5
    points.append((
        body_x - 25 + leg_swing * math.sin(knee_phase),
        body_y + 100
    ))
    points.append((
        body_x + 25 - leg_swing * math.sin(knee_phase),
        body_y + 100
    ))

    # Ankles
    ankle_phase = phase * 1.8
    points.append((
        body_x - 30 + leg_swing * math.sin(ankle_phase + math.pi/4),
        body_y + 160
    ))
    points.append((
        body_x + 30 - leg_swing * math.sin(ankle_phase + math.pi/4),
        body_y + 160
    ))

    # Additional points for 15 total
    points.append((body_x, body_y - 25))  # Neck
    points.append((body_x, body_y + 10))  # Torso

    return points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = pygame.time.get_ticks() / 1000  # Get time in seconds
    body_x, body_y = get_body_position(t)
    points = calculate_points(t, body_x, body_y)

    # Drawing
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
