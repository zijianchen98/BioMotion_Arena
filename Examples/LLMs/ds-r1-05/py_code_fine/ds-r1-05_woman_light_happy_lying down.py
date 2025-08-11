
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_COUNT = 15
BACKGROUND_COLOR = (0, 0, 0)  # Black
POINT_COLOR = (255, 255, 255)  # White
POINT_RADIUS = 5
MOTION_PERIOD = 3.5  # Seconds for complete motion cycle
PHASE_OFFSET = 0.25  # Phase offset for secondary points

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Lying Down")
clock = pygame.time.Clock()

# Define biomechanical points (relative positions when lying down)
# Structure: head, shoulders, spine, hips, knees, feet, elbows, hands
points_lying = [
    (0, -50),      # 0: head
    (-25, -30),    # 1: left shoulder
    (25, -30),     # 2: right shoulder
    (0, -10),      # 3: upper spine
    (0, 10),       # 4: lower spine
    (-20, 25),     # 5: left hip
    (20, 25),      # 6: right hip
    (-20, 50),     # 7: left knee
    (20, 50),      # 8: right knee
    (-25, 75),     # 9: left foot
    (25, 75),      # 10: right foot
    (-40, -15),    # 11: left elbow
    (40, -15),     # 12: right elbow
    (-50, 0),      # 13: left hand
    (50, 0)        # 14: right hand
]

# Standing positions (intermediate state)
points_standing = [
    (0, -100),     # head
    (-25, -75),    # left shoulder
    (25, -75),     # right shoulder
    (0, -55),      # upper spine
    (0, -20),      # lower spine
    (-20, 0),      # left hip
    (20, 0),       # right hip
    (-20, 40),     # left knee
    (20, 40),      # right knee
    (-25, 85),     # left foot
    (25, 85),      # right foot
    (-25, -25),    # left elbow
    (25, -25),     # right elbow
    (-25, 5),      # left hand
    (25, 5)        # right hand
]

def interpolate_points(start, end, t, damping=0.4):
    """Smooth interpolation with easing for natural movement"""
    ease_t = math.sin(t * math.pi * 0.5)  # Ease-in/out effect
    return [
        (x1 + (x2 - x1) * ease_t * damping, y1 + (y2 - y1) * ease_t)
        for (x1, y1), (x2, y2) in zip(start, end)
    ]

def apply_secondary_motion(points, phase):
    """Add subtle secondary movements for realism"""
    head_x, head_y = points[0]
    phase_offset = phase * 2 * math.pi
    return [
        # Head wobble
        (head_x + math.sin(phase_offset * 4) * 1.2, head_y + math.cos(phase_offset * 4) * 0.8),
        # Shoulders (sinusoidal movement)
        (points[1][0] + math.sin(phase_offset * 3) * 1.5, points[1][1] + math.cos(phase_offset * 2) * 0.7),
        (points[2][0] + math.cos(phase_offset * 3) * 1.5, points[2][1] + math.sin(phase_offset * 2) * 0.7),
        # Spine points (subtle movement)
        (points[3][0] + math.sin(phase_offset * 2) * 0.5, points[3][1]),
        (points[4][0] + math.sin(phase_offset * 1.8) * 0.8, points[4][1]),
        # Hips (minimal movement)
        points[5],
        points[6],
        # Knees (subtle flexing)
        (points[7][0] + math.sin(phase_offset * 3.5) * 1.0, points[7][1]),
        (points[8][0] + math.sin(phase_offset * 3.2) * 1.0, points[8][1]),
        # Feet (relaxed movement)
        (points[9][0] + math.sin(phase_offset * 2.5) * 1.5, points[9][1] + math.cos(phase_offset * 4) * 0.5),
        (points[10][0] + math.cos(phase_offset * 2.5) * 1.5, points[10][1] + math.sin(phase_offset * 4) * 0.5),
        # Elbows
        (points[11][0] + math.sin(phase_offset * 5) * 1.2, points[11][1] + math.cos(phase_offset * 3) * 0.7),
        (points[12][0] + math.cos(phase_offset * 5) * 1.2, points[12][1] + math.sin(phase_offset * 3) * 0.7),
        # Hands (relaxed movement)
        (points[13][0] + math.sin(phase_offset * 6) * 3.5, points[13][1] + math.cos(phase_offset * 2) * 1.0),
        (points[14][0] + math.cos(phase_offset * 6) * 3.5, points[14][1] + math.sin(phase_offset * 2) * 1.0)
    ]

# Main animation loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BACKGROUND_COLOR)
    
    # Calculate animation phase (0-1)
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    phase = (elapsed % MOTION_PERIOD) / MOTION_PERIOD
    motion_phase = math.sin(phase * math.pi)  # Sinusoidal motion pacing
    
    # Choose current pose based on phase
    if phase < 0.3:  # Standing to lying transition
        current_points = interpolate_points(points_standing, points_lying, phase * 3.33)
    elif phase < 0.7:  # Holding lying position
        current_points = interpolate_points(points_lying, points_lying, (phase - 0.3) / 0.4)
    else:  # Returning to standing
        current_points = interpolate_points(points_lying, points_standing, (phase - 0.7) / 0.3)
    
    # Apply secondary movements for realistic body dynamics
    current_points = apply_secondary_motion(current_points, phase)
    
    # Draw points (scale and position in screen center)
    for x, y in current_points:
        px = WIDTH // 2 + int(x * 3)
        py = HEIGHT // 2 + int(y * 3)
        pygame.draw.circle(screen, POINT_COLOR, (px, py), POINT_RADIUS)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
