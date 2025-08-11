
import pygame
import math
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define 15 points with start (standing) and end (lying) positions
points = [
    # Head, Neck, Shoulders
    {'start': (400, 100), 'end': (300, 400)},  # Head
    {'start': (400, 150), 'end': (350, 400)},  # Neck
    {'start': (360, 200), 'end': (250, 380)},  # Left Shoulder
    {'start': (440, 200), 'end': (450, 380)},  # Right Shoulder
    
    # Arms
    {'start': (340, 250), 'end': (200, 360)},  # Left Elbow
    {'start': (460, 250), 'end': (500, 360)},  # Right Elbow
    {'start': (320, 300), 'end': (150, 340)},  # Left Wrist
    {'start': (480, 300), 'end': (550, 340)},  # Right Wrist
    
    # Core
    {'start': (400, 250), 'end': (350, 420)},  # Torso
    
    # Hips, Legs
    {'start': (380, 350), 'end': (320, 440)},  # Left Hip
    {'start': (420, 350), 'end': (380, 440)},  # Right Hip
    {'start': (380, 450), 'end': (320, 480)},  # Left Knee
    {'start': (420, 450), 'end': (380, 480)},  # Right Knee
    {'start': (380, 550), 'end': (320, 520)},  # Left Ankle
    {'start': (420, 550), 'end': (380, 520)},  # Right Ankle
]

duration = 2.5  # Animation cycle duration in seconds

running = True
time_elapsed = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Calculate eased progress using cosine for smooth motion
    progress = (time_elapsed % duration) / duration
    eased_progress = (1 - math.cos(progress * math.pi * 2)) / 2  # Full cycle ease

    # Update and draw points
    for point in points:
        sx, sy = point['start']
        ex, ey = point['end']
        x = sx + (ex - sx) * eased_progress
        y = sy + (ey - sy) * eased_progress
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 6)

    pygame.display.flip()
    clock.tick(30)
    time_elapsed += 1/30  # Update time based on frame rate

pygame.quit()
sys.exit()
