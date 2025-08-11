 

import pygame 

import numpy as np 

from pygame.locals import * 

# Constants 

SCREEN_WIDTH = 800 

SCREEN_HEIGHT = 600 

POINT_RADIUS = 5 

BACKGROUND_COLOR = (0, 0, 0) 

POINT_COLOR = (255, 255, 255) 

FPS = 60 

# Indices 

HEAD = 0 

LEFT_SHOULDER = 1 

RIGHT_SHOULDER = 2 

LEFT_ELBOW = 3 

RIGHT_ELBOW = 4 

LEFT_WRIST = 5 

RIGHT_WRIST = 6 

LEFT_HAND = 7 

RIGHT_HAND = 8 

LEFT_HIP = 9 

RIGHT_HIP = 10 

LEFT_KNEE = 11 

RIGHT_KNEE = 12 

LEFT_ANKLE = 13 

RIGHT_ANKLE = 14 

# Base positions 

base_positions = np.zeros((15, 3)) 

# Set y coordinates 

base_positions[:,1] = [10, 9, 9, 8, 8, 7, 7, 6.5, 6.5, 5, 5, 3, 3, 1, 1] 

# Set x coordinates 

base_positions[[HEAD, LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_ELBOW, RIGHT_ELBOW, LEFT_WRIST, RIGHT_WRIST, LEFT_HAND, RIGHT_HAND, LEFT_HIP, RIGHT_HIP, LEFT_KNEE, RIGHT_KNEE, LEFT_ANKLE, RIGHT_ANKLE], 0] = [0, -1, 1, -1.5, 1.5, -1.5, 1.5, -1.5, 1.5, -0.5, 0.5, -0.5, 0.5, -0.5, 0.5] 

# Amplitudes 

arm_z_amplitude = 1.0 

leg_z_amplitude = 1.5 

# Initialize Pygame 

pygame.init() 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

pygame.display.set_caption("Point-Light Walker Turning Around") 

clock = pygame.time.Clock() 

running = True 

t = 0 

dt = 1 / FPS 

walk_speed = 2 * np.pi / 1.0 

turning_speed = 2 * np.pi / 5.0 

while running: 

    for event in pygame.event.get(): 

        if event.type == QUIT: 

            running = False 

    screen.fill(BACKGROUND_COLOR) 

    # Compute phi and theta 

    phi = walk_speed * t 

    theta = turning_speed * t 

    # Update z coordinates 

    base_positions[LEFT_ELBOW,2] = -arm_z_amplitude * np.sin(phi) 

    base_positions[LEFT_WRIST,2] = -arm_z_amplitude * np.sin(phi) 

    base_positions[LEFT_HAND,2] = -arm_z_amplitude * np.sin(phi) 

    base_positions[RIGHT_ELBOW,2] = arm_z_amplitude * np.sin(phi) 

    base_positions[RIGHT_WRIST,2] = arm_z_amplitude * np.sin(phi) 

    base_positions[RIGHT_HAND,2] = arm_z_amplitude * np.sin(phi) 

    base_positions[LEFT_KNEE,2] = leg_z_amplitude * np.sin(phi) * 0.5 

    base_positions[LEFT_ANKLE,2] = leg_z_amplitude * np.sin(phi) 

    base_positions[RIGHT_KNEE,2] = -leg_z_amplitude * np.sin(phi) * 0.5 

    base_positions[RIGHT_ANKLE,2] = -leg_z_amplitude * np.sin(phi) 

    # Compute rotation matrix 

    rotation_matrix = np.array([[np.cos(theta), 0, np.sin(theta)], 

                                [0, 1, 0], 

                                [-np.sin(theta), 0, np.cos(theta)]]) 

    # Apply rotation 

    rotated_positions = base_positions @ rotation_matrix.T 

    # Project to 2D 

    x_2d = rotated_positions[:,0] 

    y_2d = rotated_positions[:,1] 

    # Scale to screen 

    screen_x = (x_2d + 4) / 8 * SCREEN_WIDTH 

    screen_y = SCREEN_HEIGHT - (y_2d / 11 * SCREEN_HEIGHT) 

    # Draw points 

    for i in range(15): 

        pygame.draw.circle(screen, POINT_COLOR, (int(screen_x[i]), int(screen_y[i])), POINT_RADIUS) 

    pygame.display.flip() 

    t += dt 

    clock.tick(FPS) 

pygame.quit() 

