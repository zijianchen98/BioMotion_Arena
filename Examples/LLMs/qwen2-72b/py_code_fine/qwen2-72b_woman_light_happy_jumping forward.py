
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Happy Woman Jumping Forward')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []
for _ in range(num_lights):
    lights.append([random.randint(0, screen_width), random.randint(0, screen_height), 0])

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(black)
    
    # Update and draw the point lights
    for i, (x, y, vy) in enumerate(lights):
        # Simulate a jump
        vy += 0.1  # Gravity
        if x > screen_width or x < 0 or y > screen_height:
            # Reset position and velocity when out of bounds
            lights[i] = [random.randint(0, screen_width), random.randint(0, screen_height), 0]
        else:
            # Move the light
            x += 1  # Simulate forward movement
            y -= vy  # Jumping motion
            lights[i] = [x, y, vy]
        
        # Draw the point light
        pygame.draw.circle(screen, white, (int(x), int(y)), 2)
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

pygame.quit()
