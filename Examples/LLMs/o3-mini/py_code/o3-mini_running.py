
"""
This program uses pygame to animate a point‐light display of a running man.
Exactly 15 white points (representing key joints) are drawn moving on a black background.
The 15 points represent (in order):
   0 – Head
   1 – Left Shoulder
   2 – Right Shoulder
   3 – Left Elbow
   4 – Right Elbow
   5 – Left Wrist
   6 – Right Wrist
   7 – Left Hip
   8 – Right Hip
   9 – Left Knee
  10 – Right Knee
  11 – Left Ankle
  12 – Right Ankle
  13 – Pelvis (center of hips)
  14 – Chest (center of shoulders)
  
The limb motions (arms and legs) are computed using sinusoidal oscillations,
and the whole figure translates horizontally to simulate running.
The animation is designed to be smooth, realistic, and biomechanically plausible.
"""

import sys
import math
import pygame

# ----- Simulation parameters -----
FPS = 60 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Running cycle period (seconds)
T = 0.8

# Amplitude of oscillation in radians for limbs 
ARM_AMP = 0.3      # approx 17 degrees
LEG_AMP = 0.3      # approx 17 degrees

# Limb lengths (in pixels)
upper_arm_length = 20
lower_arm_length = 20
upper_leg_length = 30
lower_leg_length = 30

# Body offsets (all relative to a central pelvis position)
chest_offset = -30   # chest is 30 pixels above pelvis
head_offset = -20    # head is 20 pixels above chest
shoulder_horizontal = 15
hip_horizontal = 10

# Running speed (pixels per second)
RUN_SPEED = 150

def get_body_points(t, base_x, base_y):
    """
    Given time t and the pelvis position (base_x, base_y), compute the 
    positions of the 15 marker points.
    Returns a list of (x, y) tuples, one per marker.
    The coordinate system is pygame-style (y grows downward).
    """
    # Pelvis position (joint 13)
    pelvis = (base_x, base_y)
    
    # Chest, between shoulders (joint 14)
    chest = (base_x, base_y + chest_offset)
    
    # Head (joint 0) is above chest
    head = (base_x, chest[1] + head_offset)
    
    # Shoulders (joints 1 and 2)
    left_shoulder = (base_x - shoulder_horizontal, chest[1])
    right_shoulder = (base_x + shoulder_horizontal, chest[1])
    
    # Calculate arm swinging angles.
    # For both arms, the base angle (when stationary) is straight down (3*pi/2 in pygame coords)
    # Left arm: phase 0; Right arm: phase shifted by pi (opposite phase)
    left_arm_angle = (3 * math.pi / 2) + ARM_AMP * math.sin(2 * math.pi * t / T)
    right_arm_angle = (3 * math.pi / 2) + ARM_AMP * math.sin(2 * math.pi * t / T + math.pi)
    
    # Left arm: elbow (joint 3) and wrist (joint 5)
    lx_elbow = left_shoulder[0] + upper_arm_length * math.cos(left_arm_angle)
    ly_elbow = left_shoulder[1] + upper_arm_length * math.sin(left_arm_angle)
    left_elbow = (lx_elbow, ly_elbow)
    
    lx_wrist = lx_elbow + lower_arm_length * math.cos(left_arm_angle)
    ly_wrist = ly_elbow + lower_arm_length * math.sin(left_arm_angle)
    left_wrist = (lx_wrist, ly_wrist)
    
    # Right arm: elbow (joint 4) and wrist (joint 6)
    rx_elbow = right_shoulder[0] + upper_arm_length * math.cos(right_arm_angle)
    ry_elbow = right_shoulder[1] + upper_arm_length * math.sin(right_arm_angle)
    right_elbow = (rx_elbow, ry_elbow)
    
    rx_wrist = rx_elbow + lower_arm_length * math.cos(right_arm_angle)
    ry_wrist = ry_elbow + lower_arm_length * math.sin(right_arm_angle)
    right_wrist = (rx_wrist, ry_wrist)
    
    # Hips (joints 7 and 8)
    left_hip = (base_x - hip_horizontal, base_y)
    right_hip = (base_x + hip_horizontal, base_y)
    
    # Calculate leg swinging angles.
    # For both legs, the base angle is straight down (pi/2).
    # Left leg: phase 0; Right leg: phase shifted by pi.
    left_leg_angle = (math.pi / 2) + LEG_AMP * math.sin(2 * math.pi * t / T)
    right_leg_angle = (math.pi / 2) + LEG_AMP * math.sin(2 * math.pi * t / T + math.pi)
    
    # Left leg: knee (joint 9) and ankle (joint 11)
    lx_knee = left_hip[0] + upper_leg_length * math.cos(left_leg_angle)
    ly_knee = left_hip[1] + upper_leg_length * math.sin(left_leg_angle)
    left_knee = (lx_knee, ly_knee)
    
    lx_ankle = lx_knee + lower_leg_length * math.cos(left_leg_angle)
    ly_ankle = ly_knee + lower_leg_length * math.sin(left_leg_angle)
    left_ankle = (lx_ankle, ly_ankle)
    
    # Right leg: knee (joint 10) and ankle (joint 12)
    rx_knee = right_hip[0] + upper_leg_length * math.cos(right_leg_angle)
    ry_knee = right_hip[1] + upper_leg_length * math.sin(right_leg_angle)
    right_knee = (rx_knee, ry_knee)
    
    rx_ankle = rx_knee + lower_leg_length * math.cos(right_leg_angle)
    ry_ankle = ry_knee + lower_leg_length * math.sin(right_leg_angle)
    right_ankle = (rx_ankle, ry_ankle)
    
    # Assemble the 15 points in the required order:
    # 0: Head
    # 1: Left Shoulder
    # 2: Right Shoulder
    # 3: Left Elbow
    # 4: Right Elbow
    # 5: Left Wrist
    # 6: Right Wrist
    # 7: Left Hip
    # 8: Right Hip
    # 9: Left Knee
    # 10: Right Knee
    # 11: Left Ankle
    # 12: Right Ankle
    # 13: Pelvis
    # 14: Chest
    points = [
        head, 
        left_shoulder, 
        right_shoulder, 
        left_elbow, 
        right_elbow, 
        left_wrist, 
        right_wrist, 
        left_hip, 
        right_hip, 
        left_knee, 
        right_knee, 
        left_ankle, 
        right_ankle, 
        pelvis, 
        chest
    ]
    
    return points

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion: Running")
    clock = pygame.time.Clock()
    
    # Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Starting time and figure horizontal position
    start_ticks = pygame.time.get_ticks()
    base_x = 100  # initial x position (pelvis)
    base_y = WINDOW_HEIGHT // 2  + 50  # base y position
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # time delta in seconds
        
        # Handle events (exit on quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Compute elapsed time in seconds for the running cycle
        current_time = (pygame.time.get_ticks() - start_ticks) / 1000.0
        
        # Update horizontal position (simulate forward running)
        base_x += RUN_SPEED * dt
        
        # Wrap around if the figure leaves the screen
        if base_x - 50 > WINDOW_WIDTH:
            base_x = -50
            
        # Get the 15 marker positions for current time and base position
        points = get_body_points(current_time, base_x, base_y)
        
        # Draw background and points
        screen.fill(BLACK)
        for point in points:
            # Draw each point as a filled circle with radius 4.
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 4)
        
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()