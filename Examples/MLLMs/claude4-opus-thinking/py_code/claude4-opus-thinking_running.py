
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions (adjusted for running motion)
def points_running(frame):
    positions = []
    # Define basic structure of the body
    body_positions = [
        (-20, 0), (20, 0),  # Feet
        (-40, -40), (40, -40),  # Legs
        (-30, -80), (30, -80),  # Hips
        (-20, -120), (20, -120),  # Torso
        (0, -160),  # Head
        (-30, -140), (30, -140),  # Arms
        (-30, -100), (30, -100),
    ]
    
    # Calculate current positions based on the frame
    angle = math.radians(frame * 10)  # Change the angle with frames
    for dx, dy in body_positions:
        # Simple rotation to simulate running motion
        x = (dx * math.cos(angle)) - (dy * math.sin(angle)) + width/2
        y = (dx * math.sin(angle)) + (dy * math.cos(angle)) + height/2
        positions.append((x, y))
    
    return positions

# Main loop
running = True
clock = pygame.time.Clock()
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    screen.fill(BLACK)

    # Get the positions of the point-lights for this frame
    positions = points_running(frame)

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update display
    pygame.display.flip()

    # Increment the frame count
    frame += 1
    clock.tick(30)  # Set frame rate to 30 FPS

# Quit Pygame
pygame.quit()
