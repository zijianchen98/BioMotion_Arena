
import pygame
import math
import sys
import numpy as np

# Initialize PyGame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Walking")
clock = pygame.time.Clock()
FPS = 30

# Animation parameters
CYCLE_DURATION = 2.0  # Seconds for a complete walk cycle
BOB_AMPLITUDE = 15    # Vertical bobbing range for walking motion
SCALE = 1.8           # Scaling factor for display

# Define 15 body points: head, neck, shoulders, elbows, wrists, 
# chest, hips, knees, and ankles (indices 0-14)
POINT_COUNT = 15
body_points = [
    (0.0, 7.0),    # Head
    (0.0, 6.0),     # Neck
    (-1.0, 5.3),    # Left shoulder
    (1.0, 5.3),     # Right shoulder
    (-1.8, 4.0),    # Left elbow
    (1.8, 4.0),     # Right elbow
    (-2.5, 2.5),    # Left wrist
    (2.5, 2.5),     # Right wrist
    (0.0, 4.2),     # Chest (sternum)
    (-0.9, 3.0),    # Left hip
    (0.9, 3.0),     # Right hip
    (-1.3, 1.6),    # Left knee
    (1.3, 1.6),     # Right knee
    (-1.3, 0.0),    # Left ankle
    (1.3, 0.0)      # Right ankle
]

# Key walking poses for natural motion interpolation
key_poses = [
    {  # Left foot forward, right arm forward
        'phase': 0.0,
        'positions': [
            (0.0, 7.0), (-0.2, 6.1), (-1.3, 5.1), (0.8, 5.1), 
            (-1.9, 4.2), (1.4, 4.3), (-2.7, 3.2), (2.5, 3.0),
            (0.0, 4.1), (-0.7, 2.6), (1.1, 2.8), (-0.9, 1.0),
            (2.0, 1.0), (-1.3, -0.2), (1.1, 0.0)
        ]
    },
    {  # Middle pose 1
        'phase': 0.25,
        'positions': [
            (0.0, 7.0), (0.1, 6.0), (-1.0, 5.2), (1.0, 5.2),
            (-1.6, 4.0), (1.6, 4.0), (-2.4, 2.8), (2.4, 2.8),
            (0.0, 4.1), (-0.8, 2.7), (0.8, 2.7), (-1.2, 1.3),
            (1.2, 1.3), (-1.2, 0.1), (1.2, 0.1)
        ]
    },
    {  # Right foot forward, left arm forward
        'phase': 0.5,
        'positions': [
            (0.0, 7.0), (0.2, 6.1), (-0.8, 5.1), (1.3, 5.1),
            (-1.4, 4.3), (1.9, 4.2), (-2.5, 3.0), (2.7, 3.2),
            (0.0, 4.1), (-1.1, 2.8), (0.7, 2.6), (-2.0, 1.0),
            (0.9, 1.0), (-1.1, 0.0), (1.3, -0.2)
        ]
    },
    {  # Middle pose 2
        'phase': 0.75,
        'positions': [
            (0.0, 7.0), (-0.1, 6.0), (-1.0, 5.2), (1.0, 5.2),
            (-1.6, 4.0), (1.6, 4.0), (-2.4, 2.8), (2.4, 2.8),
            (0.0, 4.1), (-0.8, 2.7), (0.8, 2.7), (-1.2, 1.3),
            (1.2, 1.3), (-1.2, 0.1), (1.2, 0.1)
        ]
    }
]

def interpolate(a, b, alpha):
    return a + (b - a) * alpha

def get_interpolated_position(cycle_progress):
    # Find surrounding keyframes for current progress
    current_phase = cycle_progress
    key_before = None
    key_after = None
    
    for i, pose in enumerate(key_poses):
        if pose['phase'] <= current_phase:
            key_before = pose
        else:
            key_after = pose
            break
    else:
        key_before = key_poses[-1]
        key_after = key_poses[0]
        current_phase -= 1.0
    
    # Calculate interpolation parameter
    alpha = 0.0
    if key_after:
        range_phases = key_after['phase'] - key_before['phase']
        if range_phases < 0:
            range_phases += 1.0
        alpha = (current_phase - key_before['phase']) / range_phases

    # Interpolate between key positions
    interpolated = []
    for pt_idx in range(POINT_COUNT):
        x1, y1 = key_before['positions'][pt_idx]
        if key_after:
            x2, y2 = key_after['positions'][pt_idx]
        else:
            x2, y2 = key_poses[0]['positions'][pt_idx]
            
        x = interpolate(x1, x2, alpha)
        y = interpolate(y1, y2, alpha)
        interpolated.append((x, y))
        
    return interpolated

def apply_vertical_bob(positions, cycle_progress):
    # Calculate natural vertical bobbing during gait
    bob_factor = math.sin(cycle_progress * 2 * math.pi)
    return [(x, y + bob_factor * BOB_AMPLITUDE * 0.01) for x, y in positions]

def transform_point(x, y):
    # Convert normalized coordinates to screen space
    return (WIDTH//2 + int(x * SCALE * 50), 
            HEIGHT//2 - int(y * SCALE * 50))

def draw_figure(screen, positions):
    screen.fill((0, 0, 0))  # Black background
    
    # Draw all 15 points
    for x, y in positions:
        screen_x, screen_y = transform_point(x, y)
        pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 5)

# Main animation loop
start_time = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate current phase in walk cycle
    elapsed = pygame.time.get_ticks() - start_time
    elapsed_seconds = elapsed / 1000.0
    cycle_progress = (elapsed_seconds % CYCLE_DURATION) / CYCLE_DURATION
    
    # Get current body positions
    base_positions = get_interpolated_position(cycle_progress)
    positions = apply_vertical_bob(base_positions, cycle_progress)
    
    # Render the point-light figure
    draw_figure(screen, positions)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
