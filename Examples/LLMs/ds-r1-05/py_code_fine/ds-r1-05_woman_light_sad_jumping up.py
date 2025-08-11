
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion: Sad Woman Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
jump_amplitude = 60  # Vertical jump height
jump_cycle = 1.5     # Seconds per complete jump cycle
swing_amplitude = 25 # Horizontal limb movement range
gravity_factor = 0.8 # Gravity simulation factor

class PointLight:
    def __init__(self, x_offset, y_offset, limb_phase):
        self.base_x = screen_width // 2 + x_offset
        self.base_y = screen_height // 2 + y_offset
        self.limb_phase = limb_phase  # Phase offset for limb movement
        self.x = self.base_x
        self.y = self.base_y

    def update(self, time, vertical_offset, balance_shift):
        # Vertical movement with gravity simulation
        self.y = self.base_y + vertical_offset - 15 * math.sin(self.limb_phase + time * 4)
        
        # Horizontal balance movement
        self.x = self.base_x + balance_shift * 0.8 + swing_amplitude * math.sin(time * 2 + self.limb_phase)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 6)

# Create 15 points representing body joints
points = [
    # Head and torso (3 points)
    PointLight(0, -110, 0),
    PointLight(0, -80, 0),
    PointLight(0, -50, 0),
    
    # Arms (4 points)
    PointLight(-35, -90, math.pi/2),
    PointLight(-55, -60, math.pi),
    PointLight(35, -90, math.pi/2),
    PointLight(55, -60, 0),
    
    # Legs (6 points)
    PointLight(-20, 10, math.pi/1.5),
    PointLight(-20, 50, math.pi),
    PointLight(-25, 90, math.pi*1.2),
    PointLight(20, 10, math.pi/1.5),
    PointLight(20, 50, math.pi),
    PointLight(25, 90, math.pi*0.8),
    
    # Feet (2 points)
    PointLight(-40, 110, math.pi/2),
    PointLight(40, 110, math.pi/2)
]

clock = pygame.time.Clock()
running = True
time_elapsed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate vertical movement with gravity simulation
    jump_progress = (time_elapsed % jump_cycle) / jump_cycle
    vertical_offset = -jump_amplitude * (math.sin(jump_progress * math.pi * 2) ** 2)
    
    # Calculate horizontal balance shift
    balance_shift = swing_amplitude * math.sin(time_elapsed * 2.5)

    # Update all points
    for point in points:
        point.update(time_elapsed, vertical_offset, balance_shift)

    # Draw frame
    screen.fill(BLACK)
    for point in points:
        point.draw(screen)
    pygame.display.flip()

    time_elapsed += 0.02  # Increment time
    clock.tick(48)        # Maintain 48 FPS

pygame.quit()
