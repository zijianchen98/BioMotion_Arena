#!/usr/bin/env python3
import pygame
import math
import sys

#
# This program creates a simplified “biological motion” style point-light display
# of a 15-joint figure walking in place.  The figure is drawn in white against
# a solid black background, and updates smoothly to simulate a realistic walking
# motion.  Press ESC or close the window to exit.
#

# --------------------------------------------------------------------------------
# GLOBALS & CONSTANTS
# --------------------------------------------------------------------------------
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
FPS           = 60

# Scale for drawing the figure on screen
SCALE         = 200
# Center of the screen (used to translate figure onto screen)
CENTER_X      = WINDOW_WIDTH  // 2
CENTER_Y      = WINDOW_HEIGHT // 2

# Lengths of limbs / body segments (in abstract units)
PELVIS_TO_SPINE       = 0.25
SPINE_TO_HEAD         = 0.35
HALF_HIP_WIDTH        = 0.1
UPPER_LEG_LENGTH      = 0.3
LOWER_LEG_LENGTH      = 0.3
HALF_SHOULDER_WIDTH   = 0.15
UPPER_ARM_LENGTH      = 0.25
FOREARM_LENGTH        = 0.25

# --------------------------------------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------------------------------------

def rotate_point(x, y, theta):
    """
    Rotate point (x, y) around the origin (0, 0) by angle theta (radians).
    Return the rotated point (x_r, y_r).
    """
    x_r = x*math.cos(theta) - y*math.sin(theta)
    y_r = x*math.sin(theta) + y*math.cos(theta)
    return x_r, y_r

def get_joint_positions(time_s):
    """
    Given the current time in seconds (time_s), compute the 2D positions of the 15 joints.
    The figure walks in place with a basic biomechanically inspired sinusoidal pattern.
    Returns a list of (x, y) tuples for the 15 points:
    
     1:  Pelvis
     2:  Left Hip
     3:  Left Knee
     4:  Left Ankle
     5:  Right Hip
     6:  Right Knee
     7:  Right Ankle
     8:  Spine
     9:  Left Shoulder
    10:  Left Elbow
    11:  Left Wrist
    12:  Right Shoulder
    13:  Right Elbow
    14:  Right Wrist
    15:  Head
    """

    # A full gait cycle is 2*pi in our parameter. We increase time to cycle more smoothly.
    t = 2.0 * math.pi * (time_s % 1.0)  # repeats every 1 second for demonstration

    # Vertical bob of the pelvis to simulate walking bounce (small amplitude)
    pelvis_vertical_bounce = 0.02 * math.sin(2 * t)

    # Hip angles (left and right out of phase by pi)
    # Using small amplitude for hips, bigger for knees
    left_hip_angle  =  0.4 * math.sin(t)
    right_hip_angle =  0.4 * math.sin(t + math.pi)

    # Knee angles
    left_knee_angle  =  0.8 * math.sin(t + math.pi)
    right_knee_angle =  0.8 * math.sin(t)

    # Arms swing in opposite phase to legs
    left_shoulder_angle  =  0.5 * math.sin(t + math.pi)
    right_shoulder_angle =  0.5 * math.sin(t)
    left_elbow_angle  =  0.4 * math.sin(t)     # small variation
    right_elbow_angle =  0.4 * math.sin(t+math.pi)

    # Pelvis at origin + vertical bounce
    pelvis_x = 0.0
    pelvis_y = pelvis_vertical_bounce
    pelvis = (pelvis_x, pelvis_y)

    # Left Hip = pelvis_x - HIP_WIDTH, pelvis_y
    left_hip  = (pelvis_x - HALF_HIP_WIDTH, pelvis_y)
    # Right Hip = pelvis_x + HIP_WIDTH, pelvis_y
    right_hip = (pelvis_x + HALF_HIP_WIDTH, pelvis_y)

    # Compute left knee
    # The knee is upper_leg_length away from the hip, at angle = left_hip_angle from vertical
    # We'll treat "vertical" as the initial down direction (0, positive). We rotate around the hip.
    lk_dx, lk_dy = rotate_point(0, UPPER_LEG_LENGTH, left_hip_angle)
    left_knee = (left_hip[0] + lk_dx, left_hip[1] + lk_dy)

    # Left ankle
    la_dx, la_dy = rotate_point(0, LOWER_LEG_LENGTH, left_knee_angle + left_hip_angle)
    left_ankle = (left_knee[0] + la_dx, left_knee[1] + la_dy)

    # Right knee
    rk_dx, rk_dy = rotate_point(0, UPPER_LEG_LENGTH, right_hip_angle)
    right_knee = (right_hip[0] + rk_dx, right_hip[1] + rk_dy)

    # Right ankle
    ra_dx, ra_dy = rotate_point(0, LOWER_LEG_LENGTH, right_knee_angle + right_hip_angle)
    right_ankle = (right_knee[0] + ra_dx, right_knee[1] + ra_dy)

    # Spine is pelvis_y plus PELVIS_TO_SPINE vertically up
    spine = (pelvis_x, pelvis_y - PELVIS_TO_SPINE)

    # Shoulders are near top of spine, offset left and right
    left_shoulder  = (spine[0] - HALF_SHOULDER_WIDTH, spine[1])
    right_shoulder = (spine[0] + HALF_SHOULDER_WIDTH, spine[1])

    # Left elbow
    le_dx, le_dy = rotate_point(0, UPPER_ARM_LENGTH, left_shoulder_angle)
    left_elbow = (left_shoulder[0] + le_dx, left_shoulder[1] + le_dy)

    # Left wrist
    lw_dx, lw_dy = rotate_point(0, FOREARM_LENGTH, left_elbow_angle + left_shoulder_angle)
    left_wrist = (left_elbow[0] + lw_dx, left_elbow[1] + lw_dy)

    # Right elbow
    re_dx, re_dy = rotate_point(0, UPPER_ARM_LENGTH, right_shoulder_angle)
    right_elbow = (right_shoulder[0] + re_dx, right_shoulder[1] + re_dy)

    # Right wrist
    rw_dx, rw_dy = rotate_point(0, FOREARM_LENGTH, right_elbow_angle + right_shoulder_angle)
    right_wrist = (right_elbow[0] + rw_dx, right_elbow[1] + rw_dy)

    # Head is above spine
    head = (spine[0], spine[1] - SPINE_TO_HEAD)

    # Collect 15 points in order:
    points = [
        pelvis,
        left_hip,
        left_knee,
        left_ankle,
        right_hip,
        right_knee,
        right_ankle,
        spine,
        left_shoulder,
        left_elbow,
        left_wrist,
        right_shoulder,
        right_elbow,
        right_wrist,
        head
    ]

    return points

def to_screen_coordinates(x, y):
    """Convert model coordinates to screen coordinates, flipping y-axis."""
    sx = int(CENTER_X + x * SCALE)
    sy = int(CENTER_Y - y * SCALE)
    return (sx, sy)

# --------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Biological Motion - Walking Point-Light Display")
    clock = pygame.time.Clock()

    running = True
    start_time = pygame.time.get_ticks()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Compute elapsed time in seconds
        now = pygame.time.get_ticks()
        elapsed_sec = (now - start_time) / 1000.0

        # Get positions of the 15 joints at this moment
        joints = get_joint_positions(elapsed_sec)

        # Drawing
        screen.fill((0, 0, 0))  # solid black background
        for (x, y) in joints:
            screen_x, screen_y = to_screen_coordinates(x, y)
            pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()