
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happyman Jumping with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Point-light parameters
NUM_LIGHTS = 15
lights = []

class PointLight:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        self.position = np.array([0.0, 0.0, 0.0])  # x, y, z position
        
    def update(self, t, jump_params):
        # Base position - moving forward
        x = jump_params['start_x'] + jump_params['amplitude'] * np.sin(t * jump_params['frequency'])
        
        # Jumping motion (parabolic)
        z = jump_params['height'] * np.sin(t * jump_params['frequency'])**2
        
        # Adding small random vertical movement to simulate weight
        y = np.random.normal(0, 2)
        
        self.position = np.array([x, y, z])
        
    def project(self, width, height):
        # Simple perspective projection
        scale = 400 / (400 + self.position[2])
        x2d = int(self.position[0] * scale + width / 2)
        y2d = int(self.position[1] * scale + height / 2)
        return (x2d, y2d)

# Initialize lights
for i in range(NUM_LIGHTS):
    # Vary the radius slightly to create depth
    radius = np.random.uniform(2, 4)
    # Vary the initial offset to make the "body"
    offset = np.random.uniform(-20, 20)
    
    if i == 0:
        # Head light (larger, in front)
        light = PointLight(WHITE, radius)
        light.position = np.array([offset, np.random.uniform(30, 40), 0])
    elif i == 1:
        # Torso light
        light = PointLight(WHITE, radius)
        light.position = np.array([offset, np.random.uniform(10, 30), 0])
    elif i == 2:
        # Left arm light
        light = PointLight(WHITE, radius)
        light.position = np.array([offset-15, np.random.uniform(25, 35), 0])
    elif i == 3:
        # Right arm light
        light = PointLight(WHITE, radius)
        light.position = np.array([offset+15, np.random.uniform(25, 35), 0])
    elif i == 4:
        # Left leg light
        light = PointLight(WHITE, radius)
        light.position = np.array([offset-10, np.random.uniform(-20, -5), 0])
    elif i == 5:
        # Right leg light
        light = PointLight(WHITE, radius)
        light.position = np.array([offset+10, np.random.uniform(-20, -5), 0])
    else:
        # Additional body contour lights
        angle = 2 * np.pi * i / (NUM_LIGHTS - 6)
        r = np.random.uniform(-30, 30)
        light = PointLight(WHITE, radius)
        light.position = np.array([offset + r * np.cos(angle), np.random.uniform(5, 25), 0])
    
    lights.append(light)

# Jump parameters
jump_params = {
    'start_x': WIDTH // 4,
    'amplitude': 100,
    'frequency': 0.5,
    'height': 150
}

# Main animation loop
running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update lights
    for light in lights:
        light.update(t, jump_params)
        x2d, y2d = light.project(WIDTH, HEIGHT)
        
        # Only draw lights that are within the screen bounds
        if 0 <= x2d < WIDTH and 0 <= y2d < HEIGHT:
            pygame.draw.circle(screen, light.color, (x2d, y2d), light.radius)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)
    
    # Increment time
    t += 0.05
    
    # Reset animation when complete
    if t > 2 * np.pi * jump_params['frequency']:
        t = 0

# Quit pygame
pygame.quit()
sys.exit()
