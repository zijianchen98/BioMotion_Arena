
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Jump")
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Jump parameters
x0 = 100  # initial x position
y0 = 500  # ground level
vx = 150  # horizontal velocity (pixels/sec)
vy = 450  # initial vertical velocity (pixels/sec)
g = 980  # gravity (pixels/sec²)
t_jump = 0.0
jump_duration = 2 * vy / g

# Arm parameters
arm_amplitude = math.pi / 3  # 60 degrees
arm_speed = 2 * math.pi / jump_duration  # Full cycle per jump

def calculate_positions(t):
    x_hip = (x0 + vx * t) % width
    y_hip = y0 + vy * t - 0.5 * g * t**2

    arm_angle = math.sin(t * arm_speed) * arm_amplitude

    # Calculate all joint positions
    points = []
    # Head
    points.append((x_hip, y_hip - 50))
    # Shoulders
    l_shoulder = (x_hip - 30, y_hip - 30)
    r_shoulder = (x_hip + 30, y_hip - 30)
    points.extend([l_shoulder, r_shoulder])
    # Elbows
    points.append((
        l_shoulder[0] - 20 * math.sin(arm_angle),
        l_shoulder[1] + 20 * math.cos(arm_angle)
    ))
    points.append((
        r_shoulder[0] + 20 * math.sin(arm_angle),
        r_shoulder[1] + 20 * math.cos(arm_angle)
    ))
    # Wrists
    points.append((
        points[3][0] - 20 * math.sin(arm_angle),
        points[3][1] + 20 * math.cos(arm_angle)
    ))
    points.append((
        points[4][0] + 20 * math.sin(arm_angle),
        points[4][1] + 20 * math.cos(arm_angle)
    ))
    # Hips
    l_hip = (x_hip - 20, y_hip)
    r_hip = (x_hip + 20, y_hip)
    points.extend([l_hip, r_hip])
    # Knees
    leg_extension = (y0 - y_hip) * 0.3
    points.append((l_hip[0], l_hip[1] + 50 - leg_extension))
    points.append((r_hip[0], r_hip[1] + 50 - leg_extension))
    # Ankles
    points.append((points[9][0], points[9][1] + 50))
    points.append((points[10][0], points[10][1] + 50))
    # Torso and chest
    points.append((x_hip, (y_hip - 30 + y_hip) // 2))
    points.append((x_hip, (y_hip - 50 + y_hip - 30) // 2))

    return points

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0
    t_jump += dt

    # Update position and reset jump
    if t_jump >= jump_duration:
        x0 = (x0 + vx * jump_duration) % width
        t_jump = 0.0

    current_points = calculate_positions(t_jump)

    # Draw frame
    screen.fill(black)
    for point in current_points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)
    pygame.display.flip()

pygame.quit()
sys.exit()
