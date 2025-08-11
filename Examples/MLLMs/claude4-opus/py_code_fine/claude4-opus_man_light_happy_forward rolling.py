
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_RADIUS = 6

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Forward Rolling")
clock = pygame.time.Clock()

# Body joint positions for a human figure (15 points)
# Order: head, neck, left_shoulder, right_shoulder, left_elbow, right_elbow,
# left_wrist, right_wrist, torso, left_hip, right_hip, left_knee, right_knee,
# left_ankle, right_ankle
joint_names = [
    'head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'torso', 'left_hip', 'right_hip', 
    'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
]

def get_base_pose():
    """Define base human pose in standing position"""
    return {
        'head': (0, -40),
        'neck': (0, -25),
        'left_shoulder': (-15, -20),
        'right_shoulder': (15, -20),
        'left_elbow': (-25, -5),
        'right_elbow': (25, -5),
        'left_wrist': (-30, 10),
        'right_wrist': (30, 10),
        'torso': (0, 0),
        'left_hip': (-10, 20),
        'right_hip': (10, 20),
        'left_knee': (-12, 40),
        'right_knee': (12, 40),
        'left_ankle': (-10, 60),
        'right_ankle': (10, 60)
    }

def rotate_point(x, y, angle):
    """Rotate a point around origin"""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return x * cos_a - y * sin_a, x * sin_a + y * cos_a

def get_rolling_pose(frame, total_frames):
    """Generate pose for forward rolling motion"""
    base_pose = get_base_pose()
    
    # Rolling parameters
    roll_angle = (frame / total_frames) * 2 * math.pi
    center_x = WIDTH // 2 + (frame / total_frames) * 200 - 100
    center_y = HEIGHT // 2
    
    # Body rotation during roll
    body_rotation = roll_angle
    
    # Compress body during roll
    compression = 0.7 + 0.3 * abs(math.sin(roll_angle))
    
    pose = {}
    for joint, (x, y) in base_pose.items():
        # Apply compression
        y *= compression
        
        # Curl body into rolling position
        if joint in ['left_knee', 'right_knee']:
            y -= 15 * abs(math.sin(roll_angle))
        if joint in ['left_ankle', 'right_ankle']:
            y -= 25 * abs(math.sin(roll_angle))
        if joint in ['left_wrist', 'right_wrist']:
            y -= 20 * abs(math.sin(roll_angle))
        if joint in ['left_elbow', 'right_elbow']:
            y -= 15 * abs(math.sin(roll_angle))
        
        # Rotate entire body
        rot_x, rot_y = rotate_point(x, y, body_rotation)
        
        # Add slight bouncing motion
        bounce = 5 * abs(math.sin(roll_angle * 2))
        
        pose[joint] = (center_x + rot_x, center_y + rot_y - bounce)
    
    return pose

def main():
    running = True
    frame = 0
    total_frames = 120  # 4 seconds at 30 FPS
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Get current pose
        pose = get_rolling_pose(frame, total_frames)
        
        # Draw joints
        for joint_name in joint_names:
            x, y = pose[joint_name]
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        
        # Update frame
        frame = (frame + 1) % total_frames
    
    pygame.quit()

if __name__ == "__main__":
    main()
