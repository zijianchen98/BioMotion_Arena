
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Man Jumping Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point-light properties
num_lights = 15
lights = []

# Happy man model (simplified)
# Using basic geometric shapes to represent limbs and body
body_radius = 20
leg_length = 40
arm_length = 30
head_radius = 15

# Initial position and angle
x, y = width // 2, height - body_radius
angle = 0

# Jump parameters
jump_height = 100
jump_speed = 5
gravity = 1
is_jumping = False
velocity = 0

# Main loop
running = True
clock = pygame.time.Clock()

def draw_happy_man(x, y, angle):
    # Draw body
    pygame.draw.circle(screen, white, (int(x), int(y)), body_radius)
    
    # Draw legs
    leg_angle = math.radians(angle)
    leg_end_x = x + leg_length * math.cos(leg_angle)
    leg_end_y = y - leg_length * math.sin(leg_angle)
    pygame.draw.line(screen, white, (x, y), (int(leg_end_x), int(leg_end_y)), 3)
    
    # Draw arms
    arm_angle = math.radians(-angle)
    arm_end_x = x + arm_length * math.cos(arm_angle)
    arm_end_y = y - arm_length * math.sin(arm_angle)
    pygame.draw.line(screen, white, (x, y), (int(arm_end_x), int(arm_end_y)), 3)
    
    # Draw head
    head_x = x
    head_y = y - body_radius - head_radius
    pygame.draw.circle(screen, white, (int(head_x), int(head_y)), head_radius)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                velocity = -jump_speed

    # Update position
    if is_jumping:
        y += velocity
        velocity += gravity
        if y >= height - body_radius:
            y = height - body_radius
            is_jumping = False
            velocity = 0

    # Update angle for jumping motion
    if is_jumping:
        angle += 10
    else:
        angle = 0

    # Clear screen
    screen.fill(black)

    # Draw happy man
    draw_happy_man(x, y, angle)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
