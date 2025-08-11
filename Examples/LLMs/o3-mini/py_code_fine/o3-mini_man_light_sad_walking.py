
"""
This program uses pygame to animate a point‐light biological motion display.
It shows 15 white points (joints) moving on a black background as a “sadman with light weight” walking.
The joints represented are:
  • Head, Neck,
  • Left Shoulder, Right Shoulder,
  • Left Elbow, Right Elbow,
  • Left Hand, Right Hand,
  • Torso,
  • Left Hip, Right Hip,
  • Left Knee, Right Knee,
  • Left Foot, Right Foot.
The joint positions are computed using simple kinematic models that give a smooth, realistic walking motion.
"""

import sys
import math
import pygame

# Screen settings
WIDTH, HEIGHT = 800, 600

# Animation settings
FPS = 60
SCALE = 100  # Scale factor for converting body units to pixels.
SPEED = 100  # Horizontal speed in pixels per second.

# Limb lengths in "body units"
# Legs: hip to knee (upper leg) and knee to foot (lower leg)
LEG_UPPER = 0.6
LEG_LOWER = 0.6
# Arms: shoulder to elbow (upper arm) and elbow to hand (lower arm)
ARM_UPPER = 0.4
ARM_LOWER = 0.4

# Swing amplitudes (in radians, 30 degrees approx)
AMP_LEG = math.radians(30)
AMP_ARM = math.radians(30)

def get_joint_positions(t):
    """
    Returns a dictionary mapping joint names to (x,y) positions in screen pixels.
    The body coordinate system is defined with the torso at (0,0), y increasing downward.
    A global translation and scaling is applied so the figure appears on the screen.
    """
    # Global translation for walking motion.
    # The figure moves horizontally across the screen and loops.
    global_dx = ((SPEED * t) % (WIDTH + 200)) - 100  
    global_dy = HEIGHT // 2
    
    # Base (neutral) joint positions in body units:
    # Torso center at (0,0)
    torso = (0, 0)
    # Neck and Head (above torso)
    neck = (0, -0.3)
    head = (neck[0], neck[1] - 0.25)
    
    # Shoulders relative to neck
    left_shoulder = (-0.2, -0.3)
    right_shoulder = (0.2, -0.3)
    
    # Hips relative to torso
    left_hip = (-0.15, 0.2)
    right_hip = (0.15, 0.2)
    
    # Determine leg swing angles (symmetric, opposite phase)
    # When t=0, legs are neutral (standing) with angle 0 (vertical downward).
    left_leg_angle = AMP_LEG * math.sin(t)
    right_leg_angle = -AMP_LEG * math.sin(t)
    
    # Kinematic chain for legs:
    def compute_leg(hip, angle):
        knee_x = hip[0] + LEG_UPPER * math.sin(angle)
        knee_y = hip[1] + LEG_UPPER * math.cos(angle)
        knee = (knee_x, knee_y)
        foot_x = knee[0] + LEG_LOWER * math.sin(angle)
        foot_y = knee[1] + LEG_LOWER * math.cos(angle)
        foot = (foot_x, foot_y)
        return knee, foot

    left_knee, left_foot = compute_leg(left_hip, left_leg_angle)
    right_knee, right_foot = compute_leg(right_hip, right_leg_angle)
    
    # Determine arm swing angles.
    # Arms swing opposite to the contralateral legs.
    left_arm_angle = -AMP_ARM * math.sin(t)  # swings opposite to right leg
    right_arm_angle = AMP_ARM * math.sin(t)    # swings opposite to left leg

    # Kinematic chain for arms:
    def compute_arm(shoulder, angle):
        elbow_x = shoulder[0] + ARM_UPPER * math.sin(angle)
        elbow_y = shoulder[1] + ARM_UPPER * math.cos(angle)
        elbow = (elbow_x, elbow_y)
        hand_x = elbow[0] + ARM_LOWER * math.sin(angle)
        hand_y = elbow[1] + ARM_LOWER * math.cos(angle)
        hand = (hand_x, hand_y)
        return elbow, hand

    left_elbow, left_hand = compute_arm(left_shoulder, left_arm_angle)
    right_elbow, right_hand = compute_arm(right_shoulder, right_arm_angle)
    
    # Collect joint positions in body coordinate units.
    joints = {
        "head": head,
        "neck": neck,
        "left_shoulder": left_shoulder,
        "right_shoulder": right_shoulder,
        "torso": torso,
        "left_hip": left_hip,
        "right_hip": right_hip,
        "left_knee": left_knee,
        "right_knee": right_knee,
        "left_foot": left_foot,
        "right_foot": right_foot,
        "left_elbow": left_elbow,
        "right_elbow": right_elbow,
        "left_hand": left_hand,
        "right_hand": right_hand,
    }
    
    # Convert from body units to screen pixels.
    joint_pixels = {}
    for key, (x, y) in joints.items():
        pix_x = int(x * SCALE + global_dx + WIDTH // 2)
        pix_y = int(y * SCALE + global_dy)
        joint_pixels[key] = (pix_x, pix_y)
    
    return joint_pixels

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion Animation")
    clock = pygame.time.Clock()
    
    start_ticks = pygame.time.get_ticks()
    
    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Calculate elapsed time in seconds.
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Get joint positions.
        joints = get_joint_positions(t)
        
        # Clear screen.
        screen.fill((0, 0, 0))
        
        # Draw each joint as a white circle.
        for pos in joints.values():
            pygame.draw.circle(screen, (255, 255, 255), pos, 5)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()