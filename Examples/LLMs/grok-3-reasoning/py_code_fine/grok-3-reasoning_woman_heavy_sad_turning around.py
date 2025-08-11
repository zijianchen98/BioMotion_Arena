
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Sad Woman Turning Around")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define initial 3D positions for 15 points (x, y, z) in arbitrary units
# y-axis up, x-axis right, z-axis out (facing viewer initially)
# Adjusted for sadness (slumped posture) and body thickness
points = [
    (0, 1.4, 0.1),      # 0: Head (slightly down and forward)
    (0, 1.2, 0.05),     # 1: Neck
    (0, 1.0, 0),        # 2: Torso (center of rotation)
    (-0.2, 1.3, 0.05),  # 3: Left shoulder (slumped forward)
    (0.2, 1.3, 0.05),   # 4: Right shoulder
    (-0.25, 1.0, 0.02), # 5: Left elbow
    (0.25, 1.0, 0.02),  # 6: Right elbow
    (-0.3, 0.7, 0),     # 7: Left wrist
    (0.3, 0.7, 0),      # 8: Right wrist
    (-0.15, 0.8, -0.02),# 9: Left hip
    (0.15, 0.8, -0.02), # 10: Right hip
    (-0.15, 0.4, -0.01),# 11: Left knee
    (0.15, 0.4, -0.01), # 12: Right knee
    (-0.15, 0.1, 0),    # 13: Left ankle
    (0.15, 0.1, 0)      # 14: Right ankle
]

# Animation parameters
TOTAL_TIME = 2.0  # Duration in seconds
FPS = 60
TOTAL_FRAMES = int(TOTAL_TIME * FPS)
frame = 0

# Scaling factor to map units to pixels
SCALE = 200
OFFSET_X = WIDTH // 2
OFFSET_Y = HEIGHT // 2

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Compute rotation angle (0 to 180 degrees over TOTAL_TIME)
    t = frame / TOTAL_FRAMES  # Normalized time [0, 1]
    theta = math.pi * t  # Linear rotation from 0 to π radians (180 degrees)
    
    # Lists to store 2D positions
    points_2d = []
    
    # Process each point
    for i, (x, y, z) in enumerate(points):
        # For ankles (13, 14), keep fixed to simulate pivoting feet
        if i in [13, 14]:
            # Slight adjustment for realism (e.g., small shift)
            x_rot = x
            z_rot = z
        else:
            # Rotate around y-axis through torso (origin at torso)
            # Translate point relative to torso, rotate, translate back
            x_rel = x - points[2][0]
            z_rel = z - points[2][2]
            x_rot = x_rel * math.cos(theta) + z_rel * math.sin(theta)
            z_rot = -x_rel * math.sin(theta) + z_rel * math.cos(theta)
            # Add back torso position (torso stays at x=0, z=0)
            x_rot += points[2][0]
            z_rot += points[2][2]
        
        # For sadness and heavy weight, adjust y-position dynamically
        # Slow, slight vertical oscillation
        if i not in [13, 14]:  # Exclude ankles
            y_adj = y + 0.02 * math.sin(2 * math.pi * t) - 0.05 * (1 - math.cos(math.pi * t))
        else:
            y_adj = y  # Ankles stay grounded
        
        # Orthographic projection (ignore z for 2D display)
        # Map to screen coordinates
        screen_x = int(x_rot * SCALE + OFFSET_X)
        screen_y = int(-y_adj * SCALE + OFFSET_Y)  # Negative y to flip (y increases upward)
        
        points_2d.append((screen_x, screen_y))
    
    # Draw points
    for x, y in points_2d:
        pygame.draw.circle(screen, WHITE, (x, y), 5)
    
    # Update frame
    frame += 1
    if frame > TOTAL_FRAMES:
        frame = 0  # Loop animation
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
