
import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUMBER_OF_POINTS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")

# Function to generate point-light positions for a jumping motion
def generate_jump_positions(frame_count):
    positions = []
    for frame in range(frame_count):
        t = frame / frame_count * 2 * np.pi  # Convert frame to time
        x = 300 * math.sin(t)  # Forward motion
        y = (300 - 100 * math.sin(t)) + 20 * math.sin(2 * t)  # Jump arc

        # Generate points around the body
        offsets = np.linspace(-1, 1, NUMBER_OF_POINTS)
        for offset in offsets:
            # Adjust Y position for jumping body
            positions.append((WIDTH // 2 + x + offset * 15, HEIGHT - y - offset * 10))
    return positions

# Animation loop
def main():
    running = True
    clock = pygame.time.Clock()
    
    # Generate jump positions
    jump_positions = generate_jump_positions(30)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Clear the screen
        screen.fill(BLACK)

        # Draw each point-light
        for pos in jump_positions:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

        # Update the display
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

# Run the animation
if __name__ == "__main__":
    main()
