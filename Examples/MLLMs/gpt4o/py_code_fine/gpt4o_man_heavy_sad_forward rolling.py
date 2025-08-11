
import pygame
import math

# Initialize pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sadman Forward Rolling")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Biomechanics settings
points = [
    {"x": 0, "y": -200},  # Head
    {"x": -50, "y": -150}, {"x": 50, "y": -150},  # Shoulder joints (left, right)
    {"x": -100, "y": -100}, {"x": 100, "y": -100},  # Elbow joints (left, right)
    {"x": -150, "y": 0}, {"x": 150, "y": 0},  # Hand joints (left, right)
    {"x": -50, "y": -50}, {"x": 50, "y": -50},  # Hip joints (left, right)
    {"x": -80, "y": 100}, {"x": 80, "y": 100},  # Knee joints (left, right)
    {"x": -100, "y": 200}, {"x": 100, "y": 200},  # Foot joints (left, right)
    {"x": 0, "y": 0},  # Chest
    {"x": 0, "y": 100},  # Center of gravity
]

# Update function
def update_positions(frame):
    phase = frame * 0.05  # Gradual increment for smooth motion
    updated_points = []
    for i, point in enumerate(points):
        updated_x = point["x"] + math.sin(phase + i * 0.4) * 20
        updated_y = point["y"] + math.cos(phase + i * 0.4) * 20
        updated_points.append({"x": updated_x, "y": updated_y})
    return updated_points

# Draw function
def draw_points(screen, updated_points):
    screen.fill(BLACK)
    for point in updated_points:
        pygame.draw.circle(screen, WHITE, (int(width//2 + point["x"]), int(height//2 + point["y"])), 5)
    pygame.display.flip()

# Main loop
def main():
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update positions based on frames
        updated_points = update_positions(frame)

        # Draw the point-light stimuli
        draw_points(screen, updated_points)

        # Increment frame count
        frame += 1

        # Control the frame rate
        clock.tick(30)

# Run the animation
main()

# Quit pygame
pygame.quit()
