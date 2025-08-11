
import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Joint positions for a standing woman (initial pose)
# 15 points representing major body joints
joint_names = [
    'head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'spine', 'left_hip', 'right_hip', 'left_knee',
    'right_knee', 'left_ankle', 'right_ankle'
]

# Initial standing pose (normalized coordinates, will be scaled)
initial_pose = {
    'head': (0, -0.45),
    'neck': (0, -0.35),
    'left_shoulder': (-0.12, -0.3),
    'right_shoulder': (0.12, -0.3),
    'left_elbow': (-0.15, -0.15),
    'right_elbow': (0.15, -0.15),
    'left_wrist': (-0.18, 0),
    'right_wrist': (0.18, 0),
    'spine': (0, -0.1),
    'left_hip': (-0.08, 0.1),
    'right_hip': (0.08, 0.1),
    'left_knee': (-0.08, 0.25),
    'right_knee': (0.08, 0.25),
    'left_ankle': (-0.08, 0.4),
    'right_ankle': (0.08, 0.4)
}

# Final sitting pose
sitting_pose = {
    'head': (0, -0.3),
    'neck': (0, -0.2),
    'left_shoulder': (-0.12, -0.15),
    'right_shoulder': (0.12, -0.15),
    'left_elbow': (-0.2, -0.05),
    'right_elbow': (0.2, -0.05),
    'left_wrist': (-0.25, 0.05),
    'right_wrist': (0.25, 0.05),
    'spine': (0, 0),
    'left_hip': (-0.08, 0.15),
    'right_hip': (0.08, 0.15),
    'left_knee': (-0.15, 0.15),
    'right_knee': (0.15, 0.15),
    'left_ankle': (-0.15, 0.3),
    'right_ankle': (0.15, 0.3)
}

def interpolate_poses(pose1, pose2, t):
    """Interpolate between two poses with easing for natural motion"""
    # Apply easing function for more natural movement
    eased_t = 0.5 * (1 - math.cos(math.pi * t))
    
    interpolated = {}
    for joint in pose1:
        x1, y1 = pose1[joint]
        x2, y2 = pose2[joint]
        x = x1 + (x2 - x1) * eased_t
        y = y1 + (y2 - y1) * eased_t
        interpolated[joint] = (x, y)
    
    return interpolated

def scale_and_center_pose(pose, scale=200, center_x=WIDTH//2, center_y=HEIGHT//2):
    """Scale and center the pose on the screen"""
    scaled_pose = {}
    for joint, (x, y) in pose.items():
        scaled_x = center_x + x * scale
        scaled_y = center_y + y * scale
        scaled_pose[joint] = (scaled_x, scaled_y)
    return scaled_pose

def add_subtle_sway(pose, time, amplitude=5):
    """Add subtle body sway for more natural movement"""
    sway_x = amplitude * math.sin(time * 0.5)
    swayed_pose = {}
    for joint, (x, y) in pose.items():
        swayed_pose[joint] = (x + sway_x, y)
    return swayed_pose

# Animation parameters
animation_duration = 3.0  # seconds
frame_count = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                frame_count = 0  # Reset animation

    # Calculate animation progress (0 to 1)
    time_elapsed = frame_count / FPS
    if time_elapsed <= animation_duration:
        t = time_elapsed / animation_duration
    else:
        # Hold final pose or restart animation
        if time_elapsed > animation_duration + 1.0:  # Hold for 1 second
            frame_count = 0
            continue
        t = 1.0

    # Interpolate between poses
    current_pose = interpolate_poses(initial_pose, sitting_pose, t)
    
    # Scale and center the pose
    screen_pose = scale_and_center_pose(current_pose)
    
    # Add subtle movement for realism
    screen_pose = add_subtle_sway(screen_pose, time_elapsed)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw point lights
    for joint_name in joint_names:
        if joint_name in screen_pose:
            x, y = screen_pose[joint_name]
            # Draw white circles for joints
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    frame_count += 1

pygame.quit()
