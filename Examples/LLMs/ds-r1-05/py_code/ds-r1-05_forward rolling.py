
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
ground_level = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-light Biological Motion: Forward Roll")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Animation parameters
FPS = 60
total_animation_time = 2.0  # seconds
bend_duration = 0.3  # seconds
roll_duration = 1.4  # seconds (1.7 - 0.3)

# Standing pose relative to hip center
standing_pose = [
    (0, -150),    # head
    (0, -100),    # shoulder center
    (-40, -100),  # left shoulder
    (40, -100),   # right shoulder
    (-70, -70),   # left elbow
    (70, -70),    # right elbow
    (-70, -20),   # left wrist
    (70, -20),    # right wrist
    (0, -50),     # spine (mid back)
    (-20, 0),     # left hip
    (20, 0),      # right hip
    (-20, 100),   # left knee
    (20, 100),    # right knee
    (-20, 200),   # left ankle
    (20, 200)     # right ankle
]

# Tucked pose relative to the center of the circle for rolling (radius R)
R = 100
tucked_pose = [
    (0, -100),    # head
    (0, -60),     # shoulder center
    (-40, -60),   # left shoulder
    (40, -60),    # right shoulder
    (-70, -20),   # left elbow
    (70, -20),    # right elbow
    (-70, 100),   # left wrist
    (70, 100),    # right wrist
    (0, -20),     # spine
    (-40, 30),    # left hip
    (40, 30),     # right hip
    (-40, 80),    # left knee
    (40, 80),     # right knee
    (-40, 60),    # left ankle
    (40, 60)      # right ankle
]

# Initial position for the standing pose (hip center)
initial_x_hip = 400
initial_y_hip = ground_level - 200  # 200 above ground

# Setup for the tucked pose center at the start of roll
initial_x_tucked = 400
initial_y_tucked = ground_level - R

# Calculate position after full roll (at t=1.7)
end_x_tucked = initial_x_tucked + 2 * math.pi * R

# Game loop
clock = pygame.time.Clock()
elapsed_time = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)
    
    points = []
    t = elapsed_time
    
    if t < bend_duration:  # Bending phase
        fraction = t / bend_duration
        for i in range(15):
            # Standing pose position
            sx = initial_x_hip + standing_pose[i][0]
            sy = initial_y_hip + standing_pose[i][1]
            # Tucked pose position at end of bend (t=0.3)
            tx = initial_x_tucked + tucked_pose[i][0]
            ty = initial_y_tucked + tucked_pose[i][1]
            # Interpolate
            x = sx + fraction * (tx - sx)
            y = sy + fraction * (ty - sy)
            points.append((x, y))
            
    elif t < bend_duration + roll_duration:  # Rolling phase
        t_roll = t - bend_duration
        # Calculate angle: 0 to 2*pi over roll_duration
        angle = (t_roll / roll_duration) * 2 * math.pi
        # Horizontal displacement of circle center (rolling without slipping)
        d = angle * R
        x_center = initial_x_tucked + d
        y_center = initial_y_tucked
        # Calculate the points by rotating the tucked pose
        for i in range(15):
            x_rel = tucked_pose[i][0]
            y_rel = tucked_pose[i][1]
            # Rotate clockwise (using rotation matrix for clockwise rotation)
            x_rot = x_rel * math.cos(angle) + y_rel * math.sin(angle)
            y_rot = -x_rel * math.sin(angle) + y_rel * math.cos(angle)
            x = x_center + x_rot
            y = y_center + y_rot
            points.append((x, y))
            
    else:  # Standing back up (t from 1.7 to 2.0)
        if t > total_animation_time:
            t = total_animation_time
        fraction = (t - (bend_duration + roll_duration)) / (total_animation_time - (bend_duration + roll_duration))
        for i in range(15):
            # Tucked pose position at end of roll (t=1.7)
            tx = end_x_tucked + tucked_pose[i][0]
            ty = initial_y_tucked + tucked_pose[i][1]
            # Standing pose position
            sx = initial_x_hip + standing_pose[i][0]
            sy = initial_y_hip + standing_pose[i][1]
            # Interpolate
            x = tx + fraction * (sx - tx)
            y = ty + fraction * (sy - ty)
            points.append((x, y))
    
    # Draw points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)
    
    # Update display
    pygame.display.flip()
    
    # Update time
    elapsed_time += 1.0 / FPS
    if elapsed_time >= total_animation_time:
        elapsed_time = 0.0
    
    clock.tick(FPS)

pygame.quit()
sys.exit()
