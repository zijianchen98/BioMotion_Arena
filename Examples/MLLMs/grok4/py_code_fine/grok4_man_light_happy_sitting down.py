
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Point-Light Animation - Sitting Down')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the positions of the 15 point-lights
def get_point_light_positions(frame):
    # Define the static positions for a sitting pose
    positions = [
        (400, 150), (380, 180), (420, 180),  # head
        (350, 215), (450, 215),              # shoulders
        (350, 280), (450, 280),              # elbows
        (300, 350), (500, 350),              # hands
        (360, 350), (440, 350),              # waist
        (340, 400), (460, 400),              # knees
        (340, 480), (460, 480),              # feet
    ]
    
    # Animate the sitting motion slightly for realism
    offset = math.sin(frame * 0.1) * 5
    for i in range(len(positions)):
        if i < 5:  # head and shoulders
            positions[i] = (positions[i][0], positions[i][1] + offset)
        elif 5 <= i < 11:  # elbows and waist
            positions[i] = (positions[i][0], positions[i][1] + offset * 0.5)
    
    return positions

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background
    screen.fill(BLACK)
    
    # Get the current positions of point-lights
    positions = get_point_light_positions(frame)
    
    # Draw the point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)
    
    # Update the display
    pygame.display.flip()
    
    # Increment the frame count
    frame += 1
    
    # Control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
