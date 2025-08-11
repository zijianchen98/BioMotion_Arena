
"""
This program shows a point‐light biological motion animation.
It depicts a happy, heavy‐weighted woman turning in place.
Fifteen white “point‐lights” represent key joints of the body moving
in a biomechanically plausible manner against a solid black background.
The animation uses a simple 3D skeletal model (with 15 joints),
a global rotation about the vertical axis,
and subtle sinusoidal oscillations on the arms and torso to simulate natural movement.
"""

import sys
import math
import pygame

# Screen parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Projection parameters
PERSPECTIVE_SCALE = 300      # scale factor for perspective
CAMERA_Z = 3.0               # constant added to z coordinate in projection

# Define joint indices with descriptive comments:
# 0: head
# 1: left shoulder
# 2: right shoulder
# 3: left elbow
# 4: right elbow
# 5: left wrist
# 6: right wrist
# 7: torso (upper trunk)
# 8: belly (lower trunk)
# 9: left hip
# 10: right hip
# 11: left knee
# 12: right knee
# 13: left ankle
# 14: right ankle

# Define the skeleton in local 3D coordinates (x, y, z)
# (All positions in meters, roughly scaled to approximate a human figure)
# The coordinate system: x horizontal (positive to right), y vertical (positive up), z depth (positive going out of screen)
skeleton = [
    ( 0.0,   1.8,  0.0),   # 0: head
    (-0.2,   1.6,  0.0),   # 1: left shoulder
    ( 0.2,   1.6,  0.0),   # 2: right shoulder
    (-0.5,   1.4,  0.0),   # 3: left elbow
    ( 0.5,   1.4,  0.0),   # 4: right elbow
    (-0.7,   1.2,  0.0),   # 5: left wrist
    ( 0.7,   1.2,  0.0),   # 6: right wrist
    ( 0.0,   1.2,  0.0),   # 7: torso (upper trunk)
    ( 0.0,   1.1,  0.0),   # 8: belly (lower trunk)
    (-0.2,   1.0,  0.0),   # 9: left hip
    ( 0.2,   1.0,  0.0),   # 10: right hip
    (-0.2,   0.5,  0.0),   # 11: left knee
    ( 0.2,   0.5,  0.0),   # 12: right knee
    (-0.2,   0.0,  0.0),   # 13: left ankle
    ( 0.2,   0.0,  0.0),   # 14: right ankle
]

# Function to apply a rotation about the vertical (y) axis.
# For a given 3D point (x,y,z) and angle theta (in radians),
# new_x = x*cos(theta) + z*sin(theta)
# new_y = y
# new_z = -x*sin(theta) + z*cos(theta)
def rotate_y(point, theta):
    x, y, z = point
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    new_x = x * cos_t + z * sin_t
    new_y = y
    new_z = -x * sin_t + z * cos_t
    return (new_x, new_y, new_z)

# Perspective projection: project a 3D point (x,y,z) to 2D screen coordinates.
def project(point):
    x, y, z = point
    factor = PERSPECTIVE_SCALE / (z + CAMERA_Z)
    proj_x = SCREEN_WIDTH / 2 + x * factor
    # In pygame, y increases downwards so subtract y*factor.
    proj_y = SCREEN_HEIGHT / 2 - y * factor
    return (int(proj_x), int(proj_y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion: Happy Heavy Woman Turning")
    clock = pygame.time.Clock()

    start_ticks = pygame.time.get_ticks()  # for timing

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds since last frame
        current_time = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Global rotation angle (slow turning, heavy weight suggests a slower rotation)
        global_theta = current_time * 0.5  # radians per second

        # Build a new set of joint positions with slight oscillations:
        new_joint_positions = []
        for i, (x, y, z) in enumerate(skeleton):
            # Start with the base joint position.
            local_point = [x, y, z]

            # Add biomechanical oscillations:
            # Arms: simulate slight swing.
            if i == 3:  # left elbow
                local_point[2] += 0.05 * math.sin(2*math.pi*0.8*current_time)
            elif i == 5:  # left wrist
                local_point[2] += 0.05 * math.sin(2*math.pi*0.8*current_time + math.pi/2)
            elif i == 4:  # right elbow
                local_point[2] += 0.05 * math.sin(2*math.pi*0.8*current_time + math.pi)
            elif i == 6:  # right wrist
                local_point[2] += 0.05 * math.sin(2*math.pi*0.8*current_time + 3*math.pi/2)
            # Torso sway: a slight side-to-side motion for the torso and belly
            if i == 7 or i == 8:
                local_point[0] += 0.02 * math.sin(2*math.pi*0.5*current_time)

            # Rotate the joint around the vertical axis by the global angle.
            rotated_point = rotate_y(local_point, global_theta)
            new_joint_positions.append(rotated_point)

        # Clear the screen (solid black)
        screen.fill((0, 0, 0))

        # Draw each joint as a white circle using perspective projection.
        for point in new_joint_positions:
            screen_point = project(point)
            pygame.draw.circle(screen, (255, 255, 255), screen_point, 4)  # radius 4 pixels

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()