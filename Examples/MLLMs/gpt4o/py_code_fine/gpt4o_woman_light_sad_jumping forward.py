
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set title and colors
pygame.display.set_caption("Point-Light Biological Motion (Sad Woman Jumping Forward)")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Key points representing the jumping sad woman (relative positions)
# (x, y) offsets for body parts
points = [
    (0, -150),  # Head
    (-50, -100), (50, -100),  # Shoulders
    (-70, -50), (70, -50),  # Elbows
    (-80, 0), (80, 0),  # Hands
    (0, -50),  # Chest
    (-50, 50), (50, 50),  # Hips
    (-60, 150), (60, 150),  # Knees
    (-70, 250), (70, 250),  # Feet
]

# Function to calculate biomechanical motion (smooth jumping animation)
def update_points(frame_num, base_x, base_y, amplitude, frequency):
    animated_points = []
    for x, y in points:
        # Add biomechanical jump effect: sinusoidal vertical oscillation
        offset_y = amplitude * math.sin(frequency * frame_num + x * 0.01)
        animated_points.append((base_x + x, base_y + y - offset_y))
    return animated_points

# Animation parameters
frame_num = 0
base_x, base_y = WIDTH // 2, HEIGHT // 2 + 100  # Base position
amplitude = 40  # Jump height amplitude
frequency = 0.1  # Oscillation frequency for jumping motion

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the animation frame
    frame_num += 1

    # Clear the screen
    screen.fill(BLACK)

    # Update animated points for the jumping sad woman
    animated_points = update_points(frame_num, base_x, base_y, amplitude, frequency)

    # Draw the points on the screen
    for point in animated_points:
        pygame.draw.circle(screen, WHITE, point, 5)  # Point-lights

    # Refresh the screen
    pygame.display.flip()

    # Ensure smooth frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
