
import pygame
import math
import numpy as np
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down - Happy Heavy Woman")
clock = pygame.time.Clock()

# Colors
BACKGROUND = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Animation parameters
FPS = 60
DURATION = 2.5  # seconds per sit-down cycle
TOTAL_POINTS = 15
POINT_SIZE = 6
CENTER_Y = HEIGHT * 0.6

# Body structure definitions (15 points)
JOINT_NAMES = [
    "head", "neck", "upper_back", "lower_back",
    "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
    "left_wrist", "right_wrist", "left_hip", "right_hip",
    "left_knee", "right_knee", "left_ankle"
]

# Initial standing pose (x, y relative to center)
INITIAL_POSE = {
    "head": (0, -160), "neck": (0, -140), "upper_back": (0, -120),
    "lower_back": (0, -90), "left_shoulder": (-35, -135), "right_shoulder": (35, -135),
    "left_elbow": (-70, -120), "right_elbow": (70, -120), "left_wrist": (-95, -90),
    "right_wrist": (95, -90), "left_hip": (-25, -60), "right_hip": (25, -60),
    "left_knee": (-25, -10), "right_knee": (25, -10), "left_ankle": (-25, 50)
}

# Final sitting pose with realistic adjustments for heavy build
SITTING_POSE = {
    "head": (0, -110), "neck": (0, -95), "upper_back": (0, -75),
    "lower_back": (0, -40), "left_shoulder": (-40, -90), "right_shoulder": (40, -90),
    "left_elbow": (-70, -70), "right_elbow": (70, -70), "left_wrist": (-95, -40),
    "right_wrist": (95, -40), "left_hip": (-35, -20), "right_hip": (35, -20),
    "left_knee": (-20, 30), "right_knee": (20, 30), "left_ankle": (-15, 80)
}

def smoothstep(t):
    """Smooth easing function for natural movement"""
    return t * t * (3 - 2 * t)

def natural_motion(t):
    """Combined motion function with realistic timing dynamics"""
    return 0.5 - 0.5 * math.cos(math.pi * (smoothstep(t) + t/3))

def get_current_pose(progress):
    """Interpolate between poses using smooth, physics-based motion"""
    t = natural_motion(progress)
    current_pose = []
    
    for joint in JOINT_NAMES:
        x0, y0 = INITIAL_POSE[joint]
        x1, y1 = SITTING_POSE[joint]
        
        # Add subtle wobble to simulate mass and inertia
        wobble = math.sin(progress * 2 * math.pi) * 2 if "hip" in joint else 0
        y_adjust = wobble * (1 - math.pow(progress - 0.5, 2))
        
        # Biomechanically constrained movement
        if "ankle" in joint:
            # Minimal ankle movement during sit
            x = x0 + (x1 - x0) * progress
            y = y0 + (y1 - y0) * 0.3 * progress
        elif "knee" in joint:
            # Knees move earlier than hips
            knee_t = min(1, progress * 1.4)
            x = x0 + (x1 - x0) * knee_t
            y = y0 + (y1 - y0) * knee_t
        elif "hip" in joint:
            # Hips descend slower due to body mass
            hip_t = progress * 0.8
            x = x0 + (x1 - x0) * hip_t
            y = y0 + (y1 - y0) * hip_t + y_adjust
        elif "back" in joint:
            # Spinal bending with different timing
            spine_t = math.sqrt(progress)
            x = x0 + (x1 - x0) * spine_t
            y = y0 + (y1 - y0) * spine_t
        else:
            # Default smooth movement
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            
        current_pose.append((x, y))
    
    return current_pose

# Animation loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate animation progress
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    progress = (elapsed % DURATION) / DURATION
    
    # Get current pose with biomechanically accurate motion
    points = get_current_pose(progress)
    
    # Draw
    screen.fill(BACKGROUND)
    
    # Render each point light with depth effect
    for i, (x, y) in enumerate(points):
        size = POINT_SIZE
        intensity = 220 + int(35 * (y + 180) / 230)
        color = (intensity, intensity, intensity)
        
        # Draw point with subtle glow effect
        pygame.draw.circle(screen, color, (WIDTH//2 + int(x), CENTER_Y + int(y)), size)
        pygame.draw.circle(screen, POINT_COLOR, (WIDTH//2 + int(x), CENTER_Y + int(y)), size//2)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
