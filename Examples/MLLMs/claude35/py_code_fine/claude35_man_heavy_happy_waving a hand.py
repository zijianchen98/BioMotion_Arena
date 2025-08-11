
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_COUNT = 15

# Point-light configuration (initial positions)
points = np.array([
    [WIDTH // 2, HEIGHT // 2 - 100],  # Head
    [WIDTH // 2 - 20, HEIGHT // 2 - 50],  # Left shoulder
    [WIDTH // 2 + 20, HEIGHT // 2 - 50],  # Right shoulder
    [WIDTH // 2 - 20, HEIGHT // 2 + 50],  # Left hand
    [WIDTH // 2 - 20, HEIGHT // 2 + 150],  # Left foot
    [WIDTH // 2 + 20, HEIGHT // 2 + 50],  # Right hand
    [WIDTH // 2 + 20, HEIGHT // 2 + 150],  # Right foot
    [WIDTH // 2 - 50, HEIGHT // 2 - 30],  # Left elbow
    [WIDTH // 2 + 50, HEIGHT // 2 - 30],  # Right elbow
    [WIDTH // 2 - 40, HEIGHT // 2 + 30],  # Left knee
    [WIDTH // 2 + 40, HEIGHT // 2 + 30],  # Right knee
    [WIDTH // 2 - 50, HEIGHT // 2 - 80],  # Head left
    [WIDTH // 2 + 50, HEIGHT // 2 - 80],  # Head right
    [WIDTH // 2 - 40, HEIGHT // 2 + 20],  # Center torso left
    [WIDTH // 2 + 40, HEIGHT // 2 + 20],  # Center torso right
])

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    # Main animation loop
    running = True
    phase = 0
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Update point positions for waving motion
        wave_amplitude = 20
        wave_frequency = 0.05
        for i in range(len(points)):
            if i in [3, 5]:  # Waving hands
                points[i][1] += wave_amplitude * np.sin(phase + i)
        
        # Draw points
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, point.astype(int), 5)
        
        # Update display
        pygame.display.flip()

        # Increase phase for smooth wave motion
        phase += wave_frequency
        clock.tick(60)  # Frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
