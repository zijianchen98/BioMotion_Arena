
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Define point-light positions (start and end coordinates for 15 points)
points = [
    # Head
    {'start': (400, 100), 'end': (400, 180)},
    # Neck
    {'start': (400, 130), 'end': (400, 200)},
    # Left Shoulder
    {'start': (360, 150), 'end': (340, 220)},
    # Right Shoulder
    {'start': (440, 150), 'end': (460, 220)},
    # Left Elbow
    {'start': (340, 200), 'end': (320, 280)},
    # Right Elbow
    {'start': (460, 200), 'end': (480, 280)},
    # Left Wrist
    {'start': (320, 250), 'end': (300, 320)},
    # Right Wrist
    {'start': (480, 250), 'end': (500, 320)},
    # Left Hip
    {'start': (370, 300), 'end': (360, 420)},
    # Right Hip
    {'start': (430, 300), 'end': (440, 420)},
    # Left Knee
    {'start': (370, 400), 'end': (340, 380)},
    # Right Knee
    {'start': (430, 400), 'end': (460, 380)},
    # Left Ankle
    {'start': (370, 500), 'end': (340, 460)},
    # Right Ankle
    {'start': (430, 500), 'end': (460, 460)},
    # Torso Center
    {'start': (400, 220), 'end': (400, 320)},
]

# Animation parameters
duration = 2.0  # Animation cycle length in seconds
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Calculate normalized time value
    t = pygame.time.get_ticks() / 1000  # Get time in seconds
    phase = (t % duration) / duration  # Normalized to [0, 1]
    
    # Smooth interpolation factor with ease-in-out
    factor = (1 - math.cos(phase * math.pi * 2)) / 2  # Smoothly oscillates between 0 and 1

    # Update and draw all points
    for point in points:
        # Calculate intermediate positions
        x = point['start'][0] + (point['end'][0] - point['start'][0]) * factor
        y = point['start'][1] + (point['end'][1] - point['start'][1]) * factor
        
        # Draw point-light as a white circle
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
