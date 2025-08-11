
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
speed_x = 120  # Horizontal movement speed
jump_amplitude = 80  # Vertical jump height
jump_frequency = 0.8  # Jump cycle speed
arm_amplitude = 35  # Arm swing magnitude
arm_frequency = 1.8  # Arm movement speed
leg_amplitude = 40  # Leg movement magnitude
leg_frequency = 1.2  # Leg movement speed

def calculate_positions(t):
    # Base body position calculations
    cycle_time = t % (2 * math.pi)  # Use sine wave periodicity
    x_center = (width * 0.1 + speed_x * t) % (width + 300)
    vertical_offset = jump_amplitude * math.sin(cycle_time * jump_frequency)
    y_center = height * 0.7 - vertical_offset

    # Phase calculations for limb movements
    arm_phase_left = arm_amplitude * math.sin(cycle_time * arm_frequency)
    arm_phase_right = arm_amplitude * math.sin(cycle_time * arm_frequency + math.pi)
    leg_phase_left = leg_amplitude * math.sin(cycle_time * leg_frequency + math.pi/2)
    leg_phase_right = leg_amplitude * math.sin(cycle_time * leg_frequency - math.pi/2)

    # Define 15 joint positions with biomechanical relationships
    return [
        # Head (1)
        (x_center, y_center - 50),
        # Shoulders (2)
        (x_center - 35, y_center - 20),
        (x_center + 35, y_center - 20),
        # Elbows (2)
        (x_center - 35 + arm_phase_left, y_center + 15),
        (x_center + 35 + arm_phase_right, y_center + 15),
        # Hands (2)
        (x_center - 35 + arm_phase_left * 1.5, y_center + 40),
        (x_center + 35 + arm_phase_right * 1.5, y_center + 40),
        # Hips (2)
        (x_center - 25, y_center + 30),
        (x_center + 25, y_center + 30),
        # Knees (2)
        (x_center - 25, y_center + 30 + leg_phase_left),
        (x_center + 25, y_center + 30 + leg_phase_right),
        # Ankles (2)
        (x_center - 25, y_center + 30 + leg_phase_left * 1.2),
        (x_center + 25, y_center + 30 + leg_phase_right * 1.2),
        # Feet (2)
        (x_center - 30, y_center + 30 + leg_phase_left * 1.2 + 20),
        (x_center + 30, y_center + 30 + leg_phase_right * 1.2 + 20),
    ]

# Main animation loop
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = (pygame.time.get_ticks() - start_time) / 1000
    screen.fill(BLACK)
    
    # Get and draw all points
    points = calculate_positions(current_time)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
