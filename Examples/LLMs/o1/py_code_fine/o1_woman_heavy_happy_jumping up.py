import pygame
import sys
import math

# --------------------------------------------------------------------------------
# This program displays a biologically inspired point-light animation of a
# "happy woman with heavy weight" performing a jump. It uses 15 white
# circles (point-lights) on a black background. The motion is an approximation
# intended to look coherent and biomechanically plausible.
#
# To run:
#   1) Install pygame via pip if necessary: pip install pygame
#   2) Save this script as, e.g., point_light_jump.py
#   3) Execute: python point_light_jump.py
# --------------------------------------------------------------------------------

# Global configuration for Pygame window
WIDTH = 800
HEIGHT = 600
FPS = 30
NUM_FRAMES = 60  # total frames in the jump animation

# Radius (in pixels) of each point-light
POINT_RADIUS = 5

# Number of point-lights we must display
NUM_POINTS = 15

# Background color (black) and point color (white)
BG_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# --------------------------------------------------------------------------------
# We map the 15 point-lights as follows (indices in parentheses):
#   0)  Head
#   1)  Left Shoulder
#   2)  Right Shoulder
#   3)  Left Elbow
#   4)  Right Elbow
#   5)  Left Wrist
#   6)  Right Wrist
#   7)  Left Hip
#   8)  Right Hip
#   9)  Left Knee
#   10) Right Knee
#   11) Left Ankle
#   12) Right Ankle
#   13) Torso (top center)
#   14) Pelvis (center)
#
# We will define a function that, for each frame index, returns a list of
# (x,y) coordinates for these 15 points, showing a single jump and
# trying to simulate a heavier body shape and a happy jump movement.
# --------------------------------------------------------------------------------

def get_biomotion_points(frame_index):
    """
    Return a list of (x, y) tuples for the 15 major joints at the specified
    animation frame. The motion is an approximation of a heavier woman
    jumping happily in place.
    """
    # Convert frame_index into a parameter t from 0 to 1
    t = frame_index / float(NUM_FRAMES - 1)
    
    # Overall horizontal center
    center_x = WIDTH // 2
    
    # Baseline vertical position for the pelvis (lowest point in stance)
    baseline_y = HEIGHT // 2 + 100
    
    # We'll shape the jump so that from t=0 to t=0.3 the subject dips slightly,
    # from t=0.3 to t=0.7 they jump upward to a peak, and from t=0.7 to t=1.0
    # they return back to standing.
    
    # Helper function to clamp t between 0 and 1
    def clamp(v):
        return max(0.0, min(1.0, v))
    
    # We'll define a sub-interval for the jump from 0.3 to 0.7
    # and use a simple parabolic shape for the vertical displacement.
    jump_start = 0.3
    jump_end = 0.7
    jump_duration = jump_end - jump_start
    
    # We also define a slight "dip" before the jump
    dip_start = 0.0
    dip_end = 0.15
    
    # Vertical displacement relative to baseline
    # Start with no displacement
    y_offset = 0.0
    
    # Dip down slightly at the beginning (frames [0..dip_end])
    if dip_start <= t <= dip_end:
        dip_t = (t - dip_start) / (dip_end - dip_start)
        # Dip downward up to 20 pixels
        y_offset -= 20.0 * dip_t
    
    # Jump from t=0.3 to t=0.7 using a parabolic arc
    if jump_start <= t <= jump_end:
        jump_t = (t - jump_start) / jump_duration
        # Parabola for jump, up to 120 px high
        # We'll use a simple inverted parabola: 4 * jump_t * (1 - jump_t)
        jump_height = 120.0 * 4.0 * jump_t * (1.0 - jump_t)
        y_offset -= jump_height
    
    # After peak, land and maybe a small bounce
    if jump_end < t <= 1.0:
        # No extra offset, but we could add a small bounce or overshoot.
        pass
    
    # Pelvis Y position
    pelvis_y = baseline_y + y_offset
    
    # We'll define the torso top (index 13) about 60 px above pelvis
    torso_y = pelvis_y - 60
    
    # Head is about 30 px above torso
    head_y = torso_y - 30
    
    # Let's define some horizontal offsets for a heavier silhouette:
    # shoulders are slightly wider, hips are slightly wider, etc.
    # We'll place:
    #   - shoulders about +/- 20 px from center
    #   - hips about +/- 25 px from center
    #   - arms, knees, ankles with offsets from shoulders/hips
    # We'll also incorporate some slight arm swing with t.
    
    # We'll define a small wave function for arms based on t to show happiness
    arm_swing = 15.0 * math.sin(2 * math.pi * (2.0 * t))  # fast swing
    
    # Shoulders
    left_shoulder_x = center_x - 20.0
    right_shoulder_x = center_x + 20.0
    
    # Hips
    left_hip_x = center_x - 25.0
    right_hip_x = center_x + 25.0
    
    # We'll specify distances between joint points (vertical distances).
    # For arms:
    #   Shoulder to elbow: 30 px
    #   Elbow to wrist: 25 px
    # For legs:
    #   Hip to knee: 40 px
    #   Knee to ankle: 40 px
    
    # The arms will raise when the subject jumps. So from t=0.3 to t=0.7
    # the arms move upward. We'll set an angle offset for the arms from -20 deg
    # (down) up to +60 deg (above horizontal) at the jump apex, then back.
    
    arm_angle = -20.0  # default angle (down)
    if jump_start <= t <= jump_end:
        # fraction of the jump
        jump_t = (t - jump_start) / jump_duration
        # arms go from -20 deg to +60 deg
        arm_angle = -20 + 80.0 * jump_t
    elif t > jump_end:
        # arms descend back
        post_land_t = (t - jump_end) / (1.0 - jump_end)
        arm_angle = 60.0 - 80.0 * post_land_t
    
    # Convert angles to radians
    arm_angle_rad = math.radians(arm_angle)
    
    # Left arm
    # position of left elbow
    left_elbow_x = left_shoulder_x + 30.0 * math.cos(arm_angle_rad)
    left_elbow_y = torso_y + 30.0 * math.sin(arm_angle_rad)
    # position of left wrist
    left_wrist_x = left_elbow_x + 25.0 * math.cos(arm_angle_rad)
    left_wrist_y = left_elbow_y + 25.0 * math.sin(arm_angle_rad)
    
    # Right arm (mirror horizontally, same angles, but we invert direction if we want symmetrical)
    right_elbow_x = right_shoulder_x + 30.0 * math.cos(arm_angle_rad)
    right_elbow_y = torso_y + 30.0 * math.sin(arm_angle_rad)
    right_wrist_x = right_elbow_x + 25.0 * math.cos(arm_angle_rad)
    right_wrist_y = right_elbow_y + 25.0 * math.sin(arm_angle_rad)
    
    # Legs: We'll define a small knee bend as we prepare to jump and land.
    # We'll pivot from about 0° bend to ~40° bend. We'll link it to the vertical
    # displacement. The deeper the dip, the bigger the bend.
    
    # We'll measure how high the subject is relative to baseline. If y_offset < 0,
    # then we are above baseline, so we can define a knee extension. If y_offset > 0,
    # we are below baseline, so deeper knee flexion.
    
    # We'll define a knee angle from 0 deg (straight) to 40 deg (bend).
    # We'll say that if y_offset ~ -120 (peak jump) => knee angle ~ 0 deg
    # If y_offset ~ +20 (dip) => knee angle = 40 deg
    # We'll clamp these extremes:
    
    knee_angle_deg = 20.0 + 20.0 * (y_offset / 120.0)  # roughly from +40 to near 0
    knee_angle_deg = max(0.0, min(40.0, knee_angle_deg))
    knee_angle_rad = math.radians(knee_angle_deg)
    
    # We'll keep the upper thighs mostly vertical. We consider hip to knee as 40 px,
    # so the knee is basically 40 px below the hip in y. Then we'll pivot the lower leg
    # by knee_angle_deg.
    
    left_knee_x = left_hip_x
    right_knee_x = right_hip_x
    
    left_knee_y = pelvis_y + 40.0  # simplified
    right_knee_y = pelvis_y + 40.0
    
    # For the ankles, pivot lower leg by knee_angle
    # We'll pivot around the knee downward in the negative direction
    lower_leg_len = 40.0
    # We'll define that the leg extends mostly downward. We'll define negative angle
    # so it angles backward a bit. Let's keep it simple: ankles are 40 px below the knee.
    # We just shift them a bit forward/back depending on knee_angle.
    # We'll define the ankles going "down" at an angle = knee_angle if heavy/landed
    # or near zero if fully extended. We'll interpret that angle from the vertical.
    
    # Convert:
    #   If knee_angle_deg = 0 => straight leg => ankles = knee + (0, +40)
    #   If knee_angle_deg = 40 => ankles forward
    angle_from_vertical = knee_angle_rad
    left_ankle_x = left_knee_x + lower_leg_len * math.sin(angle_from_vertical)
    left_ankle_y = left_knee_y + lower_leg_len * math.cos(angle_from_vertical)
    
    right_ankle_x = right_knee_x - lower_leg_len * math.sin(angle_from_vertical)
    right_ankle_y = right_knee_y + lower_leg_len * math.cos(angle_from_vertical)
    
    # Now gather all points into a list, matching the index specification:
    points = [None] * NUM_POINTS
    
    # 0) Head
    points[0] = (center_x, head_y)
    # 1) Left Shoulder
    points[1] = (left_shoulder_x, torso_y)
    # 2) Right Shoulder
    points[2] = (right_shoulder_x, torso_y)
    # 3) Left Elbow
    points[3] = (left_elbow_x, left_elbow_y)
    # 4) Right Elbow
    points[4] = (right_elbow_x, right_elbow_y)
    # 5) Left Wrist
    points[5] = (left_wrist_x, left_wrist_y)
    # 6) Right Wrist
    points[6] = (right_wrist_x, right_wrist_y)
    # 7) Left Hip
    points[7] = (left_hip_x, pelvis_y)
    # 8) Right Hip
    points[8] = (right_hip_x, pelvis_y)
    # 9) Left Knee
    points[9] = (left_knee_x, left_knee_y)
    # 10) Right Knee
    points[10] = (right_knee_x, right_knee_y)
    # 11) Left Ankle
    points[11] = (left_ankle_x, left_ankle_y)
    # 12) Right Ankle
    points[12] = (right_ankle_x, right_ankle_y)
    # 13) Torso (top center)
    points[13] = (center_x, torso_y)
    # 14) Pelvis (center)
    points[14] = (center_x, pelvis_y)
    
    return points


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion - Happy Heavy Woman Jump")
    clock = pygame.time.Clock()
    
    # Precompute the entire animation frames to loop through
    animation_frames = []
    for i in range(NUM_FRAMES):
        pts = get_biomotion_points(i)
        animation_frames.append(pts)
    
    # Loop variables
    running = True
    frame_index = 0
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw background
        screen.fill(BG_COLOR)
        
        # Get the current frame's points
        points = animation_frames[frame_index]
        
        # Draw each point
        for (x, y) in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)
        
        pygame.display.flip()
        
        frame_index += 1
        if frame_index >= NUM_FRAMES:
            # If you prefer a repeating animation, reset to 0:
            frame_index = 0
            # If you prefer to end after a single jump, uncomment:
            # running = False
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()