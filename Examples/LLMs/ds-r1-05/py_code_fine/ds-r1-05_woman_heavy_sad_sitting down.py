
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Heavy Woman Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body points (15 points with indices)
POINTS = {
    "head": 0, "neck": 1,
    "l_shoulder": 2, "r_shoulder": 3,
    "l_elbow": 4, "r_elbow": 5,
    "l_wrist": 6, "r_wrist": 7,
    "mid_back": 8, "mid_hip": 9,
    "l_hip": 10, "r_hip": 11,
    "l_knee": 12, "r_knee": 13,
    "l_ankle": 14, "r_ankle": 15
}

# Physics and timing setup
FPS = 60
clock = pygame.time.Clock()
time_passed = 0
sitting_speed = 0.8  # Slower speed for heavy person
sway_magnitude = 0.02

def get_body_positions(phase):
    """Calculate positions of all body points based on sitting phase"""
    positions = [None] * 16
    
    # Base positions
    base_y = HEIGHT * 0.3 + (HEIGHT * 0.4 * phase)
    hip_width = 60 + 20 * math.sin(time_passed * sway_magnitude)
    
    # Head and neck
    positions[POINTS["head"]] = (WIDTH//2, base_y - 80 + 10*math.sin(time_passed*0.03))
    positions[POINTS["neck"]] = (WIDTH//2, base_y - 50)
    
    # Torso components
    positions[POINTS["mid_back"]] = (WIDTH//2, base_y - 20)
    positions[POINTS["mid_hip"]] = (WIDTH//2, base_y + 10)
    
    # Shoulders and arms
    shoulder_y = base_y - 40 + 8 * math.sin(time_passed*0.05)
    positions[POINTS["l_shoulder"]] = (WIDTH//2 - hip_width*0.9, shoulder_y)
    positions[POINTS["r_shoulder"]] = (WIDTH//2 + hip_width*0.9, shoulder_y)
    
    elbow_offset_y = 30 + 15*phase
    elbow_forward = 20 * (1 - phase)
    positions[POINTS["l_elbow"]] = (
        WIDTH//2 - hip_width*0.7 - elbow_forward,
        shoulder_y + elbow_offset_y
    )
    positions[POINTS["r_elbow"]] = (
        WIDTH//2 + hip_width*0.7 + elbow_forward,
        shoulder_y + elbow_offset_y
    )
    
    positions[POINTS["l_wrist"]] = (
        positions[POINTS["l_elbow"]][0] - 5 - 10*phase,
        positions[POINTS["l_elbow"]][1] + 30 + 5*phase
    )
    positions[POINTS["r_wrist"]] = (
        positions[POINTS["r_elbow"]][0] + 5 + 10*phase,
        positions[POINTS["r_elbow"]][1] + 30 + 5*phase
    )
    
    # Hips
    positions[POINTS["l_hip"]] = (WIDTH//2 - hip_width//2, base_y + 15)
    positions[POINTS["r_hip"]] = (WIDTH//2 + hip_width//2, base_y + 15)
    
    # Legs
    knee_spacing = 50
    positions[POINTS["l_knee"]] = (
        WIDTH//2 - knee_spacing//2 + 30*phase,
        base_y + 100 + 40*phase
    )
    positions[POINTS["r_knee"]] = (
        WIDTH//2 + knee_spacing//2 - 30*phase,
        base_y + 100 + 40*phase
    )
    
    ankle_offset = 40
    positions[POINTS["l_ankle"]] = (
        positions[POINTS["l_knee"]][0] - 5 - ankle_offset*phase,
        positions[POINTS["l_knee"]][1] + 100 + 40*phase
    )
    positions[POINTS["r_ankle"]] = (
        positions[POINTS["r_knee"]][0] + 5 + ankle_offset*phase,
        positions[POINTS["r_knee"]][1] + 100 + 40*phase
    )
    
    return positions

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update time
    time_passed += clock.tick(FPS) * 0.001  # Delta time in seconds
    phase = min(1.0, (math.sin(time_passed * sitting_speed) + 1) / 2)
    
    # Get and draw body positions
    body_positions = get_body_positions(phase)
    for point in body_positions:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
