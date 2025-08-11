
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Happy Woman Jumping")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 point-light positions (side view, in initial standing pose)
# Coordinates are in (x, y) format, y increases downward, so lower y is higher up
# Points: head, left shoulder, right shoulder (overlaps), left elbow, right elbow,
# left wrist, right wrist, left hip, right hip, left knee, right knee,
# left ankle, right ankle, left toe, right toe
initial_positions = {
    'head': (400, 100),
    'l_shoulder': (380, 150),
    'r_shoulder': (380, 150),  # Overlaps in side view
    'l_elbow': (360, 200),
    'r_elbow': (360, 200),
    'l_wrist': (340, 250),
    'r_wrist': (340, 250),
    'l_hip': (390, 300),
    'r_hip': (390, 300),
    'l_knee': (390, 400),
    'r_knee': (390, 400),
    'l_ankle': (390, 500),
    'r_ankle': (390, 500),
    'l_toe': (400, 510),
    'r_toe': (400, 510)
}

# Animation parameters
jump_duration = 1.5  # seconds
frames = int(FPS * jump_duration)
frame_count = 0

# Function to interpolate positions
def interpolate(start, end, t):
    return start + (end - start) * t

# Function to update positions based on frame
def get_positions(frame):
    t = frame / frames  # Normalized time [0, 1]
    positions = initial_positions.copy()
    
    # Define jump phases: 0-0.2 (crouch), 0.2-0.5 (push off), 0.5-0.8 (peak), 0.8-1 (land)
    if t < 0.2:  # Crouch
        phase_t = t / 0.2
        # Head moves down slightly
        positions['head'] = (400, interpolate(100, 120, phase_t))
        # Shoulders down
        y = interpolate(150, 170, phase_t)
        positions['l_shoulder'] = (380, y)
        positions['r_shoulder'] = (380, y)
        # Elbows bend back
        x = interpolate(360, 370, phase_t)
        y = interpolate(200, 220, phase_t)
        positions['l_elbow'] = (x, y)
        positions['r_elbow'] = (x, y)
        # Wrists swing back
        x = interpolate(340, 360, phase_t)
        y = interpolate(250, 270, phase_t)
        positions['l_wrist'] = (x, y)
        positions['r_wrist'] = (x, y)
        # Hips down
        y = interpolate(300, 320, phase_t)
        positions['l_hip'] = (390, y)
        positions['r_hip'] = (390, y)
        # Knees bend
        y = interpolate(400, 450, phase_t)
        positions['l_knee'] = (390, y)
        positions['r_knee'] = (390, y)
        # Ankles adjust
        y = interpolate(500, 550, phase_t)
        positions['l_ankle'] = (390, y)
        positions['r_ankle'] = (390, y)
        # Toes stay grounded
        positions['l_toe'] = (400, 510)
        positions['r_toe'] = (400, 510)
        
    elif t < 0.5:  # Push off
        phase_t = (t - 0.2) / 0.3
        # Parabolic motion upward (y = -at^2 + vt + y0)
        body_y_shift = -400 * phase_t**2 + 400 * phase_t  # Peaks at t=0.5
        # Head
        positions['head'] = (400, 120 - body_y_shift)
        # Shoulders
        y = 170 - body_y_shift
        positions['l_shoulder'] = (380, y)
        positions['r_shoulder'] = (380, y)
        # Arms swing up
        x = interpolate(370, 350, phase_t)
        y = interpolate(220, 150, phase_t)
        positions['l_elbow'] = (x, y - body_y_shift)
        positions['r_elbow'] = (x, y - body_y_shift)
        x = interpolate(360, 330, phase_t)
        y = interpolate(270, 100, phase_t)
        positions['l_wrist'] = (x, y - body_y_shift)
        positions['r_wrist'] = (x, y - body_y_shift)
        # Hips
        y = 320 - body_y_shift
        positions['l_hip'] = (390, y)
        positions['r_hip'] = (390, y)
        # Legs extend
        y = interpolate(450, 400, phase_t)
        positions['l_knee'] = (390, y - body_y_shift)
        positions['r_knee'] = (390, y - body_y_shift)
        y = interpolate(550, 500, phase_t)
        positions['l_ankle'] = (390, y - body_y_shift)
        positions['r_ankle'] = (390, y - body_y_shift)
        # Toes lift off
        y = interpolate(510, 480, phase_t)
        positions['l_toe'] = (400, y - body_y_shift)
        positions['r_toe'] = (400, y - body_y_shift)
        
    elif t < 0.8:  # In air (peak)
        phase_t = (t - 0.5) / 0.3
        # Continue parabolic motion
        total_t = (t - 0.2) / 0.6  # From push-off to landing
        body_y_shift = -400 * total_t**2 + 400 * total_t
        # Head
        positions['head'] = (400, 120 - body_y_shift)
        # Shoulders
        y = 170 - body_y_shift
        positions['l_shoulder'] = (380, y)
        positions['r_shoulder'] = (380, y)
        # Arms stay up
        y = 150 - body_y_shift
        positions['l_elbow'] = (350, y)
        positions['r_elbow'] = (350, y)
        y = 100 - body_y_shift
        positions['l_wrist'] = (330, y)
        positions['r_wrist'] = (330, y)
        # Hips
        y = 320 - body_y_shift
        positions['l_hip'] = (390, y)
        positions['r_hip'] = (390, y)
        # Legs slightly tuck
        y = interpolate(400, 450, phase_t)
        positions['l_knee'] = (390, y - body_y_shift)
        positions['r_knee'] = (390, y - body_y_shift)
        y = interpolate(500, 520, phase_t)
        positions['l_ankle'] = (390, y - body_y_shift)
        positions['r_ankle'] = (390, y - body_y_shift)
        y = interpolate(480, 500, phase_t)
        positions['l_toe'] = (400, y - body_y_shift)
        positions['r_toe'] = (400, y - body_y_shift)
        
    else:  # Landing
        phase_t = (t - 0.8) / 0.2
        total_t = (t - 0.2) / 0.6
        body_y_shift = -400 * total_t**2 + 400 * total_t
        # Head
        positions['head'] = (400, interpolate(120 - body_y_shift, 100, phase_t))
        # Shoulders
        y = interpolate(170 - body_y_shift, 150, phase_t)
        positions['l_shoulder'] = (380, y)
        positions['r_shoulder'] = (380, y)
        # Arms come down
        x = interpolate(350, 360, phase_t)
        y = interpolate(150 - body_y_shift, 200, phase_t)
        positions['l_elbow'] = (x, y)
        positions['r_elbow'] = (x, y)
        x = interpolate(330, 340, phase_t)
        y = interpolate(100 - body_y_shift, 250, phase_t)
        positions['l_wrist'] = (x, y)
        positions['r_wrist'] = (x, y)
        # Hips
        y = interpolate(320 - body_y_shift, 300, phase_t)
        positions['l_hip'] = (390, y)
        positions['r_hip'] = (390, y)
        # Knees bend to absorb impact
        y = interpolate(450 - body_y_shift, 400, phase_t)
        positions['l_knee'] = (390, y)
        positions['r_knee'] = (390, y)
        # Ankles
        y = interpolate(520 - body_y_shift, 500, phase_t)
        positions['l_ankle'] = (390, y)
        positions['r_ankle'] = (390, y)
        # Toes
        y = interpolate(500 - body_y_shift, 510, phase_t)
        positions['l_toe'] = (400, y)
        positions['r_toe'] = (400, y)
    
    return positions

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Get current positions
    positions = get_positions(frame_count)
    
    # Draw point-lights
    for pos in positions.values():
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)
    
    # Update frame count
    frame_count += 1
    if frame_count > frames:
        frame_count = 0  # Loop animation
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
