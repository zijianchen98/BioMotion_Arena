
import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 30

class Happyman:
    def __init__(self):
        self.num_lights = 15
        self.lights = []
        self.base_radius = 5
        self.generate_lights()
        self.time = 0

    def generate_lights(self):
        # Generate initial positions and velocities for the lights
        for i in range(self.num_lights):
            angle = 2 * np.pi * i / self.num_lights
            # Initial random positions within a certain radius
            self.lights.append({
                'pos': np.array([screen_width/2 + 150*np.cos(angle), 
                                 screen_height/2 + 150*np.sin(angle)]),
                'vel': np.array([np.cos(angle), np.sin(angle)]) * 2
            })

    def update(self, dt):
        self.time += dt
        
        # Define the rolling motion trajectory
        rolling_radius = 100
        rolling_speed = 1.5  # Speed of rolling motion
        rolling_angle = self.time * rolling_speed
        
        # Update positions based on rolling motion around the center
        for light in self.lights:
            # Position dependent on angle around the circle
            angle = 2 * np.pi * self.lights.index(light) / self.num_lights + rolling_angle
            light['pos'] = np.array([screen_width/2 + rolling_radius*np.cos(angle),
                                     screen_height/2 + rolling_radius*np.sin(angle)])
            
            # Adjust velocities to follow the circular motion
            light['vel'] = -np.array([np.sin(angle), np.cos(angle)]) * rolling_speed * 20

    def draw(self, screen):
        for light in self.lights:
            pygame.draw.circle(screen, WHITE, light['pos'].astype(int), self.base_radius)

# Create a Happyman instance
happyman = Happyman()

# Main game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # Time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update
    happyman.update(dt)

    # Draw
    screen.fill(BLACK)
    happyman.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
