
"""
An animation of a point‐light walker – a happy, light‐weight woman walking – using 15 white points on a black background.
Each point represents an anatomical landmark:
  0: Head
  1: Left Shoulder
  2: Right Shoulder
  3: Left Elbow
  4: Right Elbow
  5: Left Wrist
  6: Right Wrist
  7: Upper Spine
  8: Lower Spine (Pelvis)
  9: Left Hip
 10: Right Hip
 11: Left Knee
 12: Right Knee
 13: Left Ankle
 14: Right Ankle

The walking motion is created by smoothly updating joint positions using sine functions so that the limbs swing in a biomechanically plausible manner.
"""

import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion – Happy Woman Walking")

clock = pygame.time.Clock()

# Animation parameters
# Horizontal speed in pixels per second.
speed = 100  
# Cycle period (in seconds) for limb swinging
cycle_period = 1.0  

def get_joint_positions(t):
    """
    Given elapsed time (t in seconds), compute the positions of the 15 point lights.
    The base (pelvis) position moves horizontally across the screen.
    Limb swinging is simulated with sine functions.
    """
    # Compute cycle phase in radians.
    cycle = 2 * math.pi * (t / cycle_period)
    
    # Horizontal translation
    base_x = (WIDTH // 2 + speed * t) % (WIDTH + 100) - 50  # cycle around the screen
    # Vertical base (pelvis) position around mid-screen
    base_y = HEIGHT // 2

    # Define joint positions relative to the pelvis (lower spine)
    # All positions are expressed in pixels. Adjust offsets for a natural-looking figure.
    # The figure is standing upright, and vertical motion (head bobbing/lower limb oscillation)
    # is added for realism.
    
    # Head: above the upper spine. A bit of bobbing with sine wave.
    head = (base_x, base_y - 70 + 5 * math.sin(cycle))
    
    # Shoulders: left and right with slight swing; note: arms swing opposite to legs.
    left_shoulder = (base_x - 15 + 5 * math.sin(cycle + math.pi), base_y - 35)
    right_shoulder = (base_x + 15 - 5 * math.sin(cycle + math.pi), base_y - 35)
    
    # Elbows: further out from shoulders with added swing.
    left_elbow = (base_x - 30 + 8 * math.sin(cycle), base_y - 20)
    right_elbow = (base_x + 30 - 8 * math.sin(cycle), base_y - 20)
    
    # Wrists: continue the swing.
    left_wrist = (base_x - 40 + 8 * math.sin(cycle), base_y - 10)
    right_wrist = (base_x + 40 - 8 * math.sin(cycle), base_y - 10)
    
    # Upper spine (torso center): between head and pelvis.
    upper_spine = (base_x, base_y - 30)
    
    # Lower spine / Pelvis (central reference)
    lower_spine = (base_x, base_y)
    
    # Hips: slightly spread left and right.
    left_hip = (base_x - 10, base_y)
    right_hip = (base_x + 10, base_y)
    
    # Knees: vertical offset with sinusoidal oscillation.
    left_knee = (base_x - 10, base_y + 30 + 10 * math.sin(cycle))
    right_knee = (base_x + 10, base_y + 30 + 10 * math.sin(cycle + math.pi))
    
    # Ankles: further down from the knees.
    left_ankle = (base_x - 10, base_y + 60 + 10 * math.sin(cycle))
    right_ankle = (base_x + 10, base_y + 60 + 10 * math.sin(cycle + math.pi))
    
    # List ordering: exactly 15 points
    joints = [
        head,            # 0: Head
        left_shoulder,   # 1: Left Shoulder
        right_shoulder,  # 2: Right Shoulder
        left_elbow,      # 3: Left Elbow
        right_elbow,     # 4: Right Elbow
        left_wrist,      # 5: Left Wrist
        right_wrist,     # 6: Right Wrist
        upper_spine,     # 7: Upper Spine
        lower_spine,     # 8: Lower Spine (Pelvis)
        left_hip,        # 9: Left Hip
        right_hip,       #10: Right Hip
        left_knee,       #11: Left Knee
        right_knee,      #12: Right Knee
        left_ankle,      #13: Left Ankle
        right_ankle      #14: Right Ankle
    ]
    
    return joints
    

def main():
    running = True
    start_ticks = pygame.time.get_ticks()
    
    while running:
        # Calculate elapsed time in seconds
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill background black
        screen.fill((0, 0, 0))
            
        # Get joint positions for current time t.
        joints = get_joint_positions(t)
        
        # Draw each joint as a small white circle
        for pos in joints:
            pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), 4)
        
        # Update the display
        pygame.display.flip()
        
        # Limit to 60 frames per second
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()