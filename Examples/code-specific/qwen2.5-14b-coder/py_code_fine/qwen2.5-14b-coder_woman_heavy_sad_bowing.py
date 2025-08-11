
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
NUM_LIGHTS = 15

# Frame rate
FPS = 60

# Animation parameters
frame = 0
total_frames = 120  # Duration of the animation in frames

def get_light_positions(frame):
    # Define the positions of the point-lights for the bowing action
    # This is a simplified example; in a real scenario, you would need more complex calculations
    lights = []
    t = frame / total_frames
    
    # Head
    head_x = WIDTH // 2 + 50 * math.sin(2 * math.pi * t)
    head_y = HEIGHT // 2 - 100 + 50 * math.cos(2 * math.pi * t)
    lights.append((head_x, head_y))
    
    # Torso
    torso_x = WIDTH // 2
    torso_y = HEIGHT // 2
    lights.append((torso_x, torso_y))
    
    # Arms
    arm_length = 100
    left_arm_angle = math.pi / 4 + math.pi * t
    right_arm_angle = -math.pi / 4 + math.pi * t
    left_arm_x = torso_x + arm_length * math.cos(left_arm_angle)
    left_arm_y = torso_y + arm_length * math.sin(left_arm_angle)
    right_arm_x = torso_x + arm_length * math.cos(right_arm_angle)
    right_arm_y = torso_y + arm_length * math.sin(right_arm_angle)
    lights.append((left_arm_x, left_arm_y))
    lights.append((right_arm_x, right_arm_y))
    
    # Legs
    leg_length = 150
    left_leg_angle = -math.pi / 4 + math.pi * t
    right_leg_angle = math.pi / 4 + math.pi * t
    left_leg_x = torso_x + leg_length * math.cos(left_leg_angle)
    left_leg_y = torso_y + leg_length * math.sin(left_leg_angle)
    right_leg_x = torso_x + leg_length * math.cos(right_leg_angle)
    right_leg_y = torso_y + leg_length * math.sin(right_leg_angle)
    lights.append((left_leg_x, left_leg_y))
    lights.append((right_leg_x, right_leg_y))
    
    # Additional lights for weight
    weight_x = torso_x
    weight_y = torso_y + 100 + 50 * math.sin(2 * math.pi * t)
    lights.append((weight_x, weight_y))
    
    # Fill remaining lights
    while len(lights) < NUM_LIGHTS:
        x = WIDTH // 2 + 50 * math.sin(2 * math.pi * t + len(lights) * 0.5)
        y = HEIGHT // 2 + 50 * math.cos(2 * math.pi * t + len(lights) * 0.5)
        lights.append((x, y))
    
    return lights

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    light_positions = get_light_positions(frame)
    
    for x, y in light_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    
    pygame.display.flip()
    
    frame += 1
    if frame >= total_frames:
        frame = 0
    
    clock.tick(FPS)

pygame.quit()
