
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Point-Light Biological Motion')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point-light parameters
num_points = 15
point_radii = 5

# Positions and velocities
positions = [(width // 2, 200 + i * 30) for i in range(num_points)]
velocities_x = [10 * math.sin(i * (math.pi / 6)) for i in range(num_points)]
velocities_y = [10 * math.cos(i * (math.pi / 6)) for i in range(num_points)]

def draw_dots():
    screen.fill(black)
    for pos in positions:
        pygame.draw.circle(screen, white, pos, point_radii)
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Update positions
    for i in range(num_points):
        positions[i] = (int(positions[i][0] + velocities_x[i]), int(positions[i][1] + velocities_y[i]))
    
    # Check boundary condition
    for i in range(num_points):
        if positions[i][0] < 0 or positions[i][0] > width:
            velocities_x[i] = -velocities_x[i]
        if positions[i][1] < 0 or positions[i][1] > height:
            velocities_y[i] = -velocities_y[i]
    
    # Draw new positions
    draw_dots()
    pygame.time.delay(50)  # Adjust the delay as needed to control the speed of the animation

# Quit Pygame
pygame.quit()
