
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point lights (x, y, radius)
lights = []
num_lights = 15

# Initial positions spread around a torso-like shape
center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 50
spread_angle = 2 * math.pi / num_lights

for i in range(num_lights):
    angle = spread_angle * i
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    lights.append([x, y, 3])  # x, y, radius

# Walking parameters
walk_speed = 0.05
direction = 1  # 1 for forward, -1 for backward
step_angle = 0

def update_lights(step_angle):
    global lights
    for i in range(num_lights):
        angle = spread_angle * i + step_angle
        lights[i][0] = center_x + radius * math.cos(angle)
        lights[i][1] = center_y + radius * math.sin(angle)

def main():
    global step_angle, direction
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BLACK)
        
        # Update step angle for walking motion
        step_angle += walk_speed * direction
        update_lights(step_angle)
        
        # Draw the point lights
        for light in lights:
            pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), light[2])
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
