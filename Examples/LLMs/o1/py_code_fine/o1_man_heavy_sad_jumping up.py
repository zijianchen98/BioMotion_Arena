#!/usr/bin/env python3
import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define 15 joints (x, y) in "crouch" posture (sad posture, slightly hunched)
keyframe_crouch = [
    (0, -120),  # Head
    (0, -100),  # Neck
    ( 15, -95), # R Shoulder
    ( 25, -70), # R Elbow
    ( 30, -50), # R Wrist
    (-15, -95), # L Shoulder
    (-25, -70), # L Elbow
    (-30, -50), # L Wrist
    (0, -80),   # Torso Center
    ( 10, -60), # R Hip
    ( 10, -30), # R Knee
    ( 10,  0 ), # R Ankle
    (-10, -60), # L Hip
    (-10, -30), # L Knee
    (-10,  0 )  # L Ankle
]

# Define 15 joints (x, y) in "peak jump" posture (body slightly extended)
keyframe_peak = [
    (0, -140),  # Head
    (0, -120),  # Neck
    ( 20, -115),# R Shoulder
    ( 35, -90), # R Elbow
    ( 40, -70), # R Wrist
    (-20, -115),# L Shoulder
    (-35, -90), # L Elbow
    (-40, -70), # L Wrist
    (0, -100),  # Torso Center
    ( 15, -80), # R Hip
    ( 15, -50), # R Knee
    ( 15, -20), # R Ankle
    (-15, -80), # L Hip
    (-15, -50), # L Knee
    (-15, -20)  # L Ankle
]

def interpolate_points(frame):
    """
    Interpolate between crouch and peak jump over 120 frames total.
    0-60 frames: move from crouch to peak,
    60-120 frames: move from peak back to crouch.
    """
    cycle_frames = 120
    f = frame % cycle_frames  # current frame in cycle
    if f < 60:
        alpha = f / 60.0  # 0 -> 1
    else:
        alpha = 1.0 - (f - 60) / 60.0  # 1 -> 0

    # Smooth vertical offset to mimic jump (sinusoidal peak around middle)
    jump_height = 60.0 * math.sin(math.pi * f / 60.0)

    points = []
    for i in range(len(keyframe_crouch)):
        x1, y1 = keyframe_crouch[i]
        x2, y2 = keyframe_peak[i]
        x = x1 + alpha * (x2 - x1)
        y = y1 + alpha * (y2 - y1)
        # Add the overall jump offset to Y
        y -= jump_height
        points.append((x, y))
    return points

def draw_points(points):
    # Draw 15 white circles on black background
    for (x, y) in points:
        # Shift to screen center
        sx = int(WIDTH // 2 + x)
        sy = int(HEIGHT // 2 + y)
        pygame.draw.circle(screen, (255, 255, 255), (sx, sy), 5)

frame_count = 0
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    biomotion_points = interpolate_points(frame_count)
    draw_points(biomotion_points)

    pygame.display.flip()
    frame_count += 1

pygame.quit()
sys.exit()