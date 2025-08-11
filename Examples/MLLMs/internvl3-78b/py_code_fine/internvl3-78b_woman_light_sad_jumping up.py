
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sad Woman Jumping Up - Point-Light Animation')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point definitions
points = [
    (width // 2, height - 100),  # Base point
    (width // 2 - 30, height - 80), (width // 2 + 30, height - 80),  # Feet
    (width // 2 - 50, height - 120), (width // 2 + 50, height - 120),  # Ankles
    (width // 2 - 70, height - 160), (width // 2 + 70, height - 160),  # Knees
    (width // 2 - 90, height - 200), (width // 2 + 90, height - 200),  # Hips
    (width // 2 - 110, height - 240), (width // 2 + 110, height - 240),  # Shoulders
    (width // 2 - 130, height - 280), (width // 2 + 130, height - 280),  # Elbows
    (width // 2 - 130, height - 360), (width // 2 + 130, height - 360),  # Wrists
    (width // 2 - 130, height - 420), (width // 2 + 130, height - 420),  # Hands
    (width // 2, height - 420)  # Head
]

# Animation parameters
max_height = 400
def animate_jump(points, t, speed=0.1):
    new_points = []
    for x, y in points:
        amplitude = (max_height - y) / 100
        new_y = y + amplitude * math.sin(t * speed)
        new_points.append((x, new_y))
    return new_points

# Main loop
clock = pygame.time.Clock()
t = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Update points
    t += 1
    animated_points = animate_jump(points, t)

    # Draw points
    for x, y in animated_points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    # Update display
    pygame.display.flip()

    # Control framerate
    clock.tick(60)

# Quit Pygame
pygame.quit()
