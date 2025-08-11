
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Happy Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 joints (x, y) in initial standing position (center of screen)
# These represent head, shoulders, elbows, wrists, hips, knees, ankles, and a few torso points
initial_positions = [
    (400, 100),  # 0: Head
    (400, 200),  # 1: Neck
    (360, 250),  # 2: Left shoulder
    (440, 250),  # 3: Right shoulder
    (340, 350),  # 4: Left elbow
    (460, 350),  # 5: Right elbow
    (320, 450),  # 6: Left wrist
    (480, 450),  # 7: Right wrist
    (400, 300),  # 8: Upper torso
    (400, 400),  # 9: Lower torso (hips)
    (360, 500),  # 10: Left knee
    (440, 500),  # 11: Right knee
    (360, 580),  # 12: Left ankle
    (440, 580),  # 13: Right ankle
    (400, 250),  # 14: Mid torso
]

# Animation parameters
FPS = 60
clock = pygame.time.Clock()
time = 0  # Animation time variable
bow_duration = 2  # Duration of one bow cycle in seconds
bow_angle_max = math.pi / 4  # Max bow angle (45 degrees)

# Function to calculate joint positions during the bow
def get_bowing_positions(t):
    # Normalize time to a 0-1 cycle over bow_duration, then repeat
    cycle = (math.sin(2 * math.pi * t / bow_duration) + 1) / 2  # Oscillates 0 to 1
    angle = bow_angle_max * cycle  # Bow angle varies smoothly
    
    # Happy and heavy: slight bounce in hips and slower upper body motion
    hip_shift = 10 * math.sin(4 * math.pi * t / bow_duration)  # Bounce effect
    positions = initial_positions.copy()
    
    # Rotate upper body around hips (point 9)
    pivot_x, pivot_y = positions[9]
    for i in range(9):  # Head to lower torso
        x, y = initial_positions[i]
        # Translate to origin relative to pivot
        rel_x = x - pivot_x
        rel_y = y - pivot_y
        # Apply rotation
        new_rel_x = rel_x * math.cos(angle) - rel_y * math.sin(angle)
        new_rel_y = rel_x * math.sin(angle) + rel_y * math.cos(angle)
        # Translate back and apply slight happy bounce to head
        positions[i] = (
            pivot_x + new_rel_x,
            pivot_y + new_rel_y + (5 * cycle if i == 0 else 0)
        )
    
    # Adjust hips with bounce (happy + heavy feel)
    positions[9] = (pivot_x, pivot_y + hip_shift)
    
    # Legs bend slightly at knees, ankles stay grounded
    for i in [10, 11]:  # Knees
        x, y = initial_positions[i]
        positions[i] = (x, y - 20 * cycle)  # Knees move up slightly
    
    return positions

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update time
    time += 1 / FPS
    
    # Clear screen
    screen.fill(BLACK)
    
    # Calculate current positions
    positions = get_bowing_positions(time)
    
    # Draw the 15 point-lights
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
