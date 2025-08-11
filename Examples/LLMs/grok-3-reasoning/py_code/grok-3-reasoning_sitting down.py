
import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define standing positions
standing = [
    (0, 0.9),  # head
    (0, 0.8),  # neck
    (0, 0.5),  # waist
    (-0.15, 0.8),  # left shoulder
    (0.15, 0.8),  # right shoulder
    (-0.15, 0.6),  # left elbow
    (0.15, 0.6),  # right elbow
    (-0.15, 0.4),  # left wrist
    (0.15, 0.4),  # right wrist
    (-0.1, 0.5),  # left hip
    (0.1, 0.5),  # right hip
    (-0.1, 0.3),  # left knee
    (0.1, 0.3),  # right knee
    (-0.1, 0.1),  # left ankle
    (0.1, 0.1),  # right ankle
]

# Define seated positions
seated = [
    (0, 0.6),  # head
    (0, 0.5),  # neck
    (0, 0.2),  # waist
    (-0.15, 0.5),  # left shoulder
    (0.15, 0.5),  # right shoulder
    (-0.15, 0.4),  # left elbow
    (0.15, 0.4),  # right elbow
    (-0.15, 0.3),  # left wrist
    (0.15, 0.3),  # right wrist
    (-0.1, 0.2),  # left hip
    (0.1, 0.2),  # right hip
    (0.1, 0.2),  # left knee
    (0.3, 0.2),  # right knee
    (0.1, 0.0),  # left ankle
    (0.3, 0.0),  # right ankle
]

# Scale and offset
scale = 300
offset_y = 350  # y_pixel = offset_y - y * scale

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main loop
running = True
start_time = time.time()
total_time = 2.0  # seconds

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.time() - start_time
    if current_time > total_time:
        start_time = time.time()  # Reset start time to loop the animation
        current_time = 0

    t = current_time / total_time

    # Clear screen
    screen.fill(black)

    # Draw points
    for i in range(15):
        x_stand, y_stand = standing[i]
        x_seat, y_seat = seated[i]
        x = (1 - t) * x_stand + t * x_seat
        y = (1 - t) * y_stand + t * y_seat
        x_pixel = 200 + x * scale
        y_pixel = offset_y - y * scale
        pygame.draw.circle(screen, white, (int(x_pixel), int(y_pixel)), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
