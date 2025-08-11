
import pygame
import numpy as np
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
POINT_COLOR = (255, 255, 255)  # White
POINT_RADIUS = 5
FPS = 60
NUM_POINTS = 15

# Point-light positions relative to body centroid
# Points: head, neck, shoulders (2), elbows (2), wrists (2), hips (3), knees (2), ankles (2)
BODY_STRUCTURE = {
    'head': 0, 'neck': 1,
    'l_shoulder': 2, 'r_shoulder': 3,
    'l_elbow': 4, 'r_elbow': 5,
    'l_wrist': 6, 'r_wrist': 7,
    'mid_hip': 8, 'l_hip': 9, 'r_hip': 10,
    'l_knee': 11, 'r_knee': 12,
    'l_ankle': 13, 'r_ankle': 14
}

# Biomechanical parameters for a walking motion
VERTICAL_BOUNCE = 20
HORIZONTAL_SHIFT = 25
ARM_SWING = 30
LEG_SWING = 40
CYCLE_DURATION = 120  # frames for a complete walk cycle
SADNESS_FACTOR = 0.7  # Reduction factor for sad, light-weight motion

def calculate_positions(frame):
    t = frame / CYCLE_DURATION * 2 * math.pi
    points = np.zeros((NUM_POINTS, 2))
    
    # Reduced motion parameters for sad, light movement
    bounce = math.sin(t) * VERTICAL_BOUNCE * SADNESS_FACTOR
    shift = math.sin(t) * HORIZONTAL_SHIFT * SADNESS_FACTOR
    arm_swing = math.sin(t) * ARM_SWING * SADNESS_FACTOR
    leg_swing = math.sin(t) * LEG_SWING * SADNESS_FACTOR
    
    # Torso points (vertical bounce)
    points[BODY_STRUCTURE['head']] = [0, -120 + bounce]
    points[BODY_STRUCTURE['neck']] = [0, -90 + bounce]
    points[BODY_STRUCTURE['mid_hip']] = [0, -15 + bounce]
    points[BODY_STRUCTURE['l_hip']] = [-20, -20 + bounce]
    points[BODY_STRUCTURE['r_hip']] = [20, -20 + bounce]
    
    # Arms (swinging in opposition to legs)
    points[BODY_STRUCTURE['l_shoulder']] = [-45, -70 + bounce]
    points[BODY_STRUCTURE['r_shoulder']] = [45, -70 + bounce]
    points[BODY_STRUCTURE['l_elbow']] = [
        -45 - arm_swing, 
        -25 + bounce + abs(arm_swing)*0.2
    ]
    points[BODY_STRUCTURE['r_elbow']] = [
        45 + arm_swing, 
        -25 + bounce + abs(arm_swing)*0.2
    ]
    points[BODY_STRUCTURE['l_wrist']] = [
        points[BODY_STRUCTURE['l_elbow']][0] - 25, 
        points[BODY_STRUCTURE['l_elbow']][1] + 20
    ]
    points[BODY_STRUCTURE['r_wrist']] = [
        points[BODY_STRUCTURE['r_elbow']][0] + 25, 
        points[BODY_STRUCTURE['r_elbow']][1] + 20
    ]
    
    # Legs with phase offset (natural walking opposition)
    left_phase_offset = math.pi
    points[BODY_STRUCTURE['l_knee']] = [
        -20 + math.sin(t + left_phase_offset) * HORIZONTAL_SHIFT * SADNESS_FACTOR,
        30 + bounce + abs(math.sin(t + left_phase_offset)) * 20
    ]
    points[BODY_STRUCTURE['r_knee']] = [
        20 + shift, 
        30 + bounce + abs(math.sin(t)) * 20
    ]
    points[BODY_STRUCTURE['l_ankle']] = [
        points[BODY_STRUCTURE['l_knee']][0], 
        70 + bounce - abs(math.sin(t + left_phase_offset)) * 10
    ]
    points[BODY_STRUCTURE['r_ankle']] = [
        points[BODY_STRUCTURE['r_knee']][0], 
        70 + bounce - abs(math.sin(t)) * 10
    ]
    
    # Subtle head tilt for sadness
    points[BODY_STRUCTURE['head']][0] = math.sin(t * 0.5) * 5
    points[BODY_STRUCTURE['head']][1] += math.sin(t * 0.5) * 3
    
    return points

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Walking")
    clock = pygame.time.Clock()
    
    centroid_x, centroid_y = WIDTH // 2, HEIGHT // 2
    frame_count = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BACKGROUND_COLOR)
        
        # Calculate point positions
        points = calculate_positions(frame_count)
        
        # Draw each point
        for point in points:
            pygame.draw.circle(
                screen, 
                POINT_COLOR, 
                (int(centroid_x + point[0]), int(centroid_y + point[1])), 
                POINT_RADIUS
            )
        
        pygame.display.flip()
        clock.tick(FPS)
        frame_count = (frame_count + 1) % CYCLE_DURATION
    
    pygame.quit()

if __name__ == "__main__":
    main()
