
"""
A Python program that displays an animation of a running "happyman" using a point‐light 
display with 15 white dots on a black background. This program uses Pygame.

The 15 markers represent (in order):
 1. Head 
 2. Left Shoulder 
 3. Right Shoulder 
 4. Left Elbow 
 5. Right Elbow 
 6. Left Wrist 
 7. Right Wrist 
 8. Spine 
 9. Left Hip 
10. Right Hip 
11. Left Knee 
12. Right Knee 
13. Left Ankle 
14. Right Ankle 
15. Pelvis

The body segments are computed from simple biomechanical assumptions. The limbs swing in a 
smooth, periodic fashion to simulate realistic running. The skeleton’s pelvis translates 
horizontally simulating running.
"""

import pygame, sys, math

# ---------- Parameters and helper functions ------------
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Time parameters
RUN_CYCLE = 0.8  # seconds for one full cycle of running
v = 200          # horizontal speed in pixels per second

# Body segment lengths (in pixels)
spine_offset = 20   # distance from pelvis to spine marker
head_offset  = 20   # distance from spine to head marker
shoulder_offset = 10  # horizontal offset from spine for shoulders

arm_upper = 20     # from shoulder to elbow
arm_lower = 20     # from elbow to wrist
leg_thigh = 30     # from hip to knee
leg_shank = 30     # from knee to ankle

hip_offset = 10    # horizontal offset from pelvis for hips

# Swing amplitudes (in radians)
A_arm = math.radians(30)    # arm swing amplitude
A_leg = math.radians(30)    # leg swing amplitude
# Knee flexion: additional swing of shank relative to thigh
A_knee = math.radians(20)

# Helper: vector addition
def vec_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

# Helper: create vector from magnitude and angle (angle in radians)
# Note: In screen coordinates, x increases right, y increases down.
def from_angle(mag, angle):
    return (mag * math.cos(angle), mag * math.sin(angle))

# ---------- Main Animation Function ------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Running Point-Light Biological Motion")
    clock = pygame.time.Clock()
    
    start_ticks = pygame.time.get_ticks()
    
    # Initial horizontal starting position for the pelvis
    start_x = 100
    base_pelvis_y = HEIGHT - 100  # vertical position of pelvis
    
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Compute time in seconds
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0
        
        # Horizontal position of pelvis
        pelvis_x = start_x + v * t
        # Slight vertical oscillation of the pelvis (a subtle bounce)
        pelvis_y = base_pelvis_y - 5 * math.sin(2 * math.pi * t / RUN_CYCLE)
        
        # ---------------- Compute Marker Positions ---------------------
        points = {}  # dictionary to store computed marker positions
        
        # 15th marker: Pelvis (we want to include this point)
        points["Pelvis"] = (pelvis_x, pelvis_y)
        
        # 8. Spine: located above pelvis by a fixed offset.
        spine = (pelvis_x, pelvis_y - spine_offset)
        points["Spine"] = spine
        
        # 1. Head: above spine by head_offset.
        head = (spine[0], spine[1] - head_offset)
        points["Head"] = head
        
        # 2 & 3. Left Shoulder and Right Shoulder:
        left_shoulder = (spine[0] - shoulder_offset, spine[1])
        right_shoulder = (spine[0] + shoulder_offset, spine[1])
        points["Left Shoulder"] = left_shoulder
        points["Right Shoulder"] = right_shoulder
        
        # --- Arms: Compute left and right arms with swing ---
        # The arms swing in counterphase.
        # Base angle of a hanging arm is straight down (90° from x-axis = math.pi/2).
        base_arm_angle = math.pi/2
        # Left arm swing: using sine; Right arm is shifted by pi (counterphase)
        left_arm_angle = base_arm_angle + A_arm * math.sin(2*math.pi*t/ RUN_CYCLE)
        right_arm_angle = base_arm_angle + A_arm * math.sin(2*math.pi*t/ RUN_CYCLE + math.pi)
        # 4 & 5. Left Elbow and Right Elbow:
        left_elbow = vec_add(left_shoulder, from_angle(arm_upper, left_arm_angle))
        right_elbow = vec_add(right_shoulder, from_angle(arm_upper, right_arm_angle))
        points["Left Elbow"] = left_elbow
        points["Right Elbow"] = right_elbow
        # 6 & 7. Left Wrist and Right Wrist:
        left_wrist = vec_add(left_elbow, from_angle(arm_lower, left_arm_angle))
        right_wrist = vec_add(right_elbow, from_angle(arm_lower, right_arm_angle))
        points["Left Wrist"] = left_wrist
        points["Right Wrist"] = right_wrist
        
        # --- Lower body: hips, legs ---
        # 9 & 10. Left Hip and Right Hip:
        left_hip = (pelvis_x - hip_offset, pelvis_y)
        right_hip = (pelvis_x + hip_offset, pelvis_y)
        points["Left Hip"] = left_hip
        points["Right Hip"] = right_hip
        
        # Legs: For each leg, compute thigh and shank based on swing angles.
        # The thigh base angle is vertical downward (pi/2) with a sinusoid adjustment.
        left_thigh_angle = math.pi/2 + A_leg * math.sin(2*math.pi*t/ RUN_CYCLE)
        right_thigh_angle = math.pi/2 + A_leg * math.sin(2*math.pi*t/ RUN_CYCLE + math.pi)
        
        # 11 & 12. Left Knee and Right Knee:
        left_knee = vec_add(left_hip, from_angle(leg_thigh, left_thigh_angle))
        right_knee = vec_add(right_hip, from_angle(leg_thigh, right_thigh_angle))
        points["Left Knee"] = left_knee
        points["Right Knee"] = right_knee
        
        # Knee flexion: the shank swings further relative to the thigh.
        # A simple model: the shank angle is thigh angle minus a sinusoid (with a bit of delay)
        left_shank_angle = left_thigh_angle - A_knee * math.sin(2*math.pi*t/ RUN_CYCLE)
        right_shank_angle = right_thigh_angle - A_knee * math.sin(2*math.pi*t/ RUN_CYCLE + math.pi)
        
        # 13 & 14. Left Ankle and Right Ankle:
        left_ankle = vec_add(left_knee, from_angle(leg_shank, left_shank_angle))
        right_ankle = vec_add(right_knee, from_angle(leg_shank, right_shank_angle))
        points["Left Ankle"] = left_ankle
        points["Right Ankle"] = right_ankle
        
        # (Markers are now: Head, LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist, Spine,
        # LHip, RHip, LKnee, RKnee, LAnkle, RAnkle, Pelvis) -> 15 points
        
        # ---------------- Drawing ---------------------
        screen.fill(BLACK)
        # Draw each marker as a white circle (radius 4)
        for pt in points.values():
            # Convert coordinates (assume they are already in pixel space)
            pygame.draw.circle(screen, WHITE, (int(pt[0]), int(pt[1])), 4)
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()