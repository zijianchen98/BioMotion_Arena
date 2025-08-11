
import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing")

# Define joint positions
# These positions roughly represent a standing body in a bowing motion
# Each tuple represents (x_offset, y_offset) to the center
JOINTS = [(0, -250), (-50, -200), (50, -200), (-75, -150), (75, -150),
          (0, -100), (-50, -50), (50, -50), (-30, 0), (30, 0),
          (0, 50), (-50, 100), (50, 100), (-75, 200), (75, 200)]

# Motion parameters
num_frames = 120  # Frames for one bowing cycle
angle_start, angle_end = 0, 40  # Bowing angle range in degrees
angle_increment = (angle_end - angle_start) / num_frames  # Angle increment per frame

# Helper function to rotate points for bowing motion
def rotate_point(origin, point, angle):
    x0, y0 = origin
    x, y = point
    angle_rad = math.radians(angle)
    new_x = x0 + (x - x0) * math.cos(angle_rad) - (y - y0) * math.sin(angle_rad)
    new_y = y0 + (x - x0) * math.sin(angle_rad) + (y - y0) * math.cos(angle_rad)
    return (new_x, new_y)

# Function to update points for bowing motion
def update_points(points, frame):
    center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen
    angle = angle_start + frame * angle_increment
    angle = angle % (angle_end * 2)  # Make the bowing motion cyclic
    if angle > angle_end:
        angle = angle_end * 2 - angle  # Reverse motion after reaching peak
    transformed_points = [rotate_point(center, (center[0] + x, center[1] + y), angle) for x, y in points]
    return transformed_points

# Main loop
clock = pygame.time.Clock()
frame = 0

running = True
while running:
    screen.fill(BLACK)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update joint positions for the bowing motion
    positions = update_points(JOINTS, frame)

    # Draw the joints
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)

    # Update frame
    frame = (frame + 1) % num_frames

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame when done
pygame.quit()
