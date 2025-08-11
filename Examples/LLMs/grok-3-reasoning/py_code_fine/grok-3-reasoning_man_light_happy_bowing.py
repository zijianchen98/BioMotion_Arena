
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))

# Define initial points
initial_points = [
    (400, 550),  # head
    (370, 500),  # left shoulder
    (430, 500),  # right shoulder
    (350, 450),  # left elbow
    (450, 450),  # right elbow
    (340, 400),  # left wrist
    (460, 400),  # right wrist
    (335, 390),  # left hand
    (465, 390),  # right hand
    (380, 350),  # left hip
    (420, 350),  # right hip
    (380, 250),  # left knee
    (420, 250),  # right knee
    (380, 150),  # left ankle
    (420, 150)   # right ankle
]

# Define rotation center
cx, cy = 400, 350

# Define rotate_point function
def rotate_point(point, angle):
    x, y = point
    dx = x - cx
    dy = y - cy
    rad = math.radians(angle)
    x_new = cx + dx * math.cos(rad) - dy * math.sin(rad)
    y_new = cy + dx * math.sin(rad) + dy * math.cos(rad)
    return (int(x_new), int(y_new))

# Main loop
running = True
clock = pygame.time.Clock()
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Compute current angle
    if frame < 30:
        angle = (frame / 30.0) * 45
    else:
        angle = ((60 - frame) / 30.0) * 45
    frame = (frame + 1) % 60
    
    # Compute current points
    current_points = []
    for i in range(15):
        if i < 9:  # upper body
            current_points.append(rotate_point(initial_points[i], angle))
        else:  # lower body
            current_points.append(initial_points[i])
    
    # Draw
    screen.fill((0, 0, 0))
    for point in current_points:
        pygame.draw.circle(screen, (255, 255, 255), point, 5)
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
