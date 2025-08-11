
import pygame
import sys
import math
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters for the animation
num_lights = 15
clock = pygame.time.Clock()
FPS = 60

# Parameters for the hand-waving motion
hand_base_pos = (WIDTH // 2, HEIGHT - 100)  # Base position of the hand
waving_amplitude = 50  # Maximum distance the hand moves side to side
waving_frequency = 0.5  # Frequency of waving motion in Hz

class Light:
    def __init__(self, initial_pos, max_distance, angle_range):
        self.position = list(initial_pos)
        self.max_distance = max_distance
        self.angle_range = angle_range
        self.angle = np.random.uniform(*angle_range)
        self.distance_from_hand = np.random.uniform(0, max_distance)
        self.speed = np.random.uniform(0.5, 2)
    
    def update(self, hand_pos, time, waving_offset):
        # Calculate a position along an arc relative to the hand
        angle = self.angle + (waving_offset / self.max_distance) * (self.angle_range[1] - self.angle_range[0]) / 2
        self.position[0] = hand_pos[0] + self.distance_from_hand * math.cos(angle)
        self.position[1] = hand_pos[1] + self.distance_from_hand * math.sin(angle)

        # Also add some minor vertical oscillation
        self.position[1] += 5 * math.sin(time * self.speed)

lights = []
for _ in range(num_lights):
    # Random angle range for lights (spread out around the hand)
    angle_range = (math.pi / 4, 3 * math.pi / 4)  # Roughly 45 to 135 degrees
    max_distance = np.random.uniform(30, 80)
    initial_pos = (WIDTH // 2, HEIGHT - 100)  # Start at the hand base
    lights.append(Light(initial_pos, max_distance, angle_range))

# Main animation loop
running = True
time_elapsed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    # Calculate the current position of the "hand" based on waving motion
    waving_offset = waving_amplitude * math.sin(time_elapsed * 2 * math.pi * waving_frequency)
    hand_pos = (WIDTH // 2 + waving_offset, HEIGHT - 100)
    
    # Update and draw lights
    for light in lights:
        light.update(hand_pos, time_elapsed, waving_offset)
        pygame.draw.circle(screen, WHITE, light.position, 3)
    
    pygame.display.flip()
    clock.tick(FPS)
    time_elapsed += 1 / FPS

pygame.quit()
sys.exit()
