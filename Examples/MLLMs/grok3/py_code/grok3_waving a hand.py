
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")
clock = pygame.time.Clock()

# Define point-light positions (simplified human model with 15 points)
base_positions = np.array([
    [200, 100],  # Head
    [180, 150], [220, 150],  # Shoulders
    [160, 250], [240, 250],  # Elbows
    [140, 350], [260, 350],  # Hands
    [200, 300],  # Chest
    [180, 400], [220, 400],  # Hips
    [160, 500], [200, 500], [240, 500],  # Knees
    [160, 600], [200, 600], [240, 600]  # Feet
])

# Animation parameters
frame_count = 0
max_frames = 120  # Total frames for one waving cycle
amplitude = 50  # Waving amplitude
frequency = 0.1  # Waving frequency

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))  # Black background

    # Update positions for waving motion
    positions = base_positions.copy()
    if frame_count < max_frames:
        # Move right hand in a sinusoidal wave
        wave_offset = amplitude * np.sin(2 * np.pi * frequency * (frame_count / max_frames))
        positions[6] = [base_positions[6][0] + wave_offset, base_positions[6][1]]  # Right hand

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

    # Update frame
    frame_count = (frame_count + 1) % max_frames

# Quit Pygame
pygame.quit()
