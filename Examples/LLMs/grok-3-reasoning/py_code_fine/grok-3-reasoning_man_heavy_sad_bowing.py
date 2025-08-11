
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define the original points relative to the pelvis at (0, 0)
original_points = [
    (0, -150),    # head
    (-40, -100),  # left shoulder
    (40, -100),   # right shoulder
    (-60, -50),   # left elbow
    (60, -50),    # right elbow
    (-70, 0),     # left wrist
    (70, 0),      # right wrist
    (-75, 10),    # left hand
    (75, 10),     # right hand
    (-20, 0),     # left hip
    (20, 0),      # right hip
    (-20, 100),   # left knee
    (20, 100),    # right knee
    (-20, 200),   # left ankle
    (20, 200),    # right ankle
]

# Offset to center the figure on the screen
offset_x = screen_width // 2
offset_y = screen_height // 2

# Function to rotate a point around (0, 0)
def rotate_point(point, theta_deg):
    theta_rad = math.radians(theta_deg)
    x, y = point
    x_new = x * math.cos(theta_rad) - y * math.sin(theta_rad)
    y_new = x * math.sin(theta_rad) + y * math.cos(theta_rad)
    return (x_new, y_new)

# Main loop
running = True
t = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate theta based on time for bowing motion
    frame = t % 60
    if frame < 30:
        theta = (frame / 30.0) * 45  # Bow down
    else:
        theta = ((60 - frame) / 30.0) * 45  # Bow up

    # Update positions
    points = []
    for i, p in enumerate(original_points):
        if i < 9:  # Upper body points (head to hands)
            rotated_p = rotate_point(p, theta)
            points.append(rotated_p)
        else:  # Lower body points (hips to ankles)
            points.append(p)

    # Draw the points
    screen.fill((0, 0, 0))  # Black background
    for point in points:
        screen_x = offset_x + point[0]
        screen_y = offset_y - point[1]  # Invert y-axis for Pygame
        pygame.draw.circle(screen, (255, 255, 255), (int(screen_x), int(screen_y)), 5)

    pygame.display.flip()
    clock.tick(30)  # 30 FPS
    t += 1

pygame.quit()
