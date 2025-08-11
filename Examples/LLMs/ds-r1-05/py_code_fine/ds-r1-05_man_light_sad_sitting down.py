
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Point positions for standing (initial) and sitting (final) poses
# Using 15 points: head, neck, shoulders, elbows, wrists, thoracic spine, hips, knees, ankles
standing_pose = [
    (0.0, -100.0),    # 0: head
    (0.0, -80.0),     # 1: neck
    (-30.0, -80.0),   # 2: left shoulder
    (30.0, -80.0),    # 3: right shoulder
    (-40.0, -50.0),   # 4: left elbow
    (40.0, -50.0),    # 5: right elbow
    (-50.0, -20.0),   # 6: left wrist
    (50.0, -20.0),    # 7: right wrist
    (0.0, -50.0),     # 8: thoracic spine
    (-20.0, 0.0),     # 9: left hip
    (20.0, 0.0),      # 10: right hip
    (-20.0, 50.0),    # 11: left knee
    (20.0, 50.0),     # 12: right knee
    (-20.0, 100.0),   # 13: left ankle
    (20.0, 100.0)     # 14: right ankle
]

sitting_pose = [
    (0.0, -70.0),     # head
    (0.0, -55.0),     # neck
    (-30.0, -55.0),   # left shoulder
    (30.0, -55.0),    # right shoulder
    (-45.0, -30.0),   # left elbow
    (45.0, -30.0),    # right elbow
    (-60.0, -10.0),   # left wrist
    (60.0, -10.0),    # right wrist
    (0.0, -30.0),     # thoracic spine
    (-15.0, 40.0),    # left hip
    (15.0, 40.0),     # right hip
    (-15.0, 75.0),    # left knee
    (15.0, 75.0),     # right knee
    (-10.0, 100.0),   # left ankle
    (10.0, 100.0)     # right ankle
]

# Parameters for animation
scale = 2.0
center_x, center_y = width // 2, height - 150
total_frames = 60  # 2 seconds at 30 FPS
clock = pygame.time.Clock()
FPS = 30

# Main animation loop
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate interpolation factor with smooth easing
    t = frame / total_frames
    t_ease = (1.0 - math.cos(t * math.pi)) / 2.0  # Smooth start and end
    
    # Interpolate each point
    current_pose = []
    for i in range(15):
        x = standing_pose[i][0] * (1 - t_ease) + sitting_pose[i][0] * t_ease
        y = standing_pose[i][1] * (1 - t_ease) + sitting_pose[i][1] * t_ease
        current_pose.append((x, y))
    
    # Clear screen to black
    screen.fill((0, 0, 0))
    
    # Draw the 15 points as white circles
    for point in current_pose:
        x, y = point
        screen_x = center_x + int(x * scale)
        screen_y = center_y + int(y * scale)
        pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 3)
    
    pygame.display.flip()
    clock.tick(FPS)
    
    # Update frame counter
    frame = (frame + 1) % total_frames

pygame.quit()
sys.exit()
