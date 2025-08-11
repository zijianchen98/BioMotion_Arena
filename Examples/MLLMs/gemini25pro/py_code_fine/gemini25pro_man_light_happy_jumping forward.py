
import pygame
import math

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Biological Motion: Jumping Forward"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation Parameters
POINT_RADIUS = 4
TOTAL_FRAMES = 120  # Total frames for one loop (2 seconds at 60 FPS)

# --- Keyframe Data ---

# Global path of the figure's center (x, y_from_bottom_of_screen)
KEYFRAME_GLOBALS = [
    (150, 100),  # Frame 0: Initial Crouch
    (250, 200),  # Frame 30: Takeoff
    (400, 350),  # Frame 60: Apex of Jump
    (550, 200),  # Frame 90: Landing Preparation
    (650, 100)   # Frame 120: Landed Crouch
]

# Time mapping for the keyframes
KEYFRAME_TIMES = [0, 30, 60, 90, TOTAL_FRAMES]

# Local poses: coordinates for each of the 15 points relative to the global center.
# The Y-axis is defined as UP (+y) for easier biomechanical definition.
# Point Order: Head, Neck, Pelvis, L_Shoulder, R_Shoulder, L_Elbow, R_Elbow, 
# L_Wrist, R_Wrist, L_Hip, R_Hip, L_Knee, R_Knee, L_Ankle, R_Ankle

# Keyframe 0: Initial Crouch Pose
kf0_local = [
    (20, 90), (15, 60), (5, 5),      # Head, Neck, Pelvis
    (-20, 55), (25, 55),            # Shoulders L/R
    (-40, 20), (10, 20),            # Elbows L/R (arms swung back)
    (-50, -10), (5, -10),           # Wrists L/R
    (-15, 0), (15, 0),              # Hips L/R
    (-20, -50), (20, -50),            # Knees L/R
    (-5, -80), (35, -80)            # Ankles L/R
]

# Keyframe 1: Takeoff Pose (Explosive Extension)
kf1_local = [
    (0, 110), (0, 80), (0, 5),       # Head, Neck, Pelvis
    (-25, 75), (25, 75),             # Shoulders
    (-10, 30), (60, 30),             # Elbows (arms swinging forward)
    (-5, 0), (70, 0),                # Wrists
    (-15, 0), (15, 0),             # Hips
    (-20, -70), (20, -70),           # Knees (extending)
    (-25, -140), (25, -140)          # Ankles (fully extended)
]

# Keyframe 2: Apex Pose (Tucked, for a "light weight" feel)
kf2_local = [
    (20, 90), (15, 60), (5, 5),       # Head, Neck, Pelvis
    (-15, 55), (25, 55),             # Shoulders
    (10, 30), (50, 30),              # Elbows (arms forward)
    (25, 10), (65, 10),              # Wrists
    (-15, 0), (15, 0),             # Hips
    (-25, 20), (35, 20),             # Knees (tucked up)
    (-10, 0), (50, 0)               # Ankles (tucked up)
]

# Keyframe 3: Landing Preparation Pose (Legs extend down)
kf3_local = [
    (0, 110), (0, 80), (0, 5),       # Head, Neck, Pelvis
    (-25, 75), (25, 75),             # Shoulders
    (-40, 50), (40, 50),             # Elbows (arms out for balance)
    (-60, 30), (60, 30),             # Wrists
    (-15, 0), (15, 0),             # Hips
    (-20, -70), (20, -70),           # Knees (extending down)
    (-25, -140), (25, -140)          # Ankles (reaching for ground)
]

# Keyframe 4: Landed Crouch Pose (Same as initial crouch)
kf4_local = kf0_local

KEYFRAME_POSES = [kf0_local, kf1_local, kf2_local, kf3_local, kf4_local]


# --- Easing and Interpolation Functions ---

def lerp(a, b, t):
    """Linear interpolation between a and b."""
    return a + (b - a) * t

def ease_in_out_sine(t):
    """Sine easing function for smooth start and end."""
    return -(math.cos(math.pi * t) - 1) / 2

def ease_out_quad(t):
    """Quadratic easing, decelerating to zero. Used for upward jump motion."""
    return 1 - (1 - t) * (1 - t)

def ease_in_quad(t):
    """Quadratic easing, accelerating from zero. Used for downward jump motion."""
    return t * t


# --- Core Animation Logic ---

def get_current_pose(frame_num):
    """Calculates the screen coordinates of all 15 points for a given frame."""
    
    # Ensure the frame number loops correctly
    if frame_num < KEYFRAME_TIMES[0] or frame_num >= KEYFRAME_TIMES[-1]:
        frame_num %= KEYFRAME_TIMES[-1]

    # Find the current keyframe segment the animation is in
    start_kf_idx = -1
    for i in range(len(KEYFRAME_TIMES) - 1):
        if frame_num >= KEYFRAME_TIMES[i] and frame_num < KEYFRAME_TIMES[i+1]:
            start_kf_idx = i
            break
    
    end_kf_idx = start_kf_idx + 1

    # Calculate interpolation factor 't' (0.0 to 1.0) for the current segment
    start_time = KEYFRAME_TIMES[start_kf_idx]
    end_time = KEYFRAME_TIMES[end_kf_idx]
    t = (frame_num - start_time) / (end_time - start_time)
    
    # --- Interpolate Global Position ---
    gx1, gy1 = KEYFRAME_GLOBALS[start_kf_idx]
    gx2, gy2 = KEYFRAME_GLOBALS[end_kf_idx]

    # Use custom easing for the jump arc to create a more realistic parabolic feel
    if start_kf_idx == 1:  # Takeoff -> Apex (going up)
        t_eased_global = ease_out_quad(t)
    elif start_kf_idx == 2: # Apex -> Landing Prep (going down)
        t_eased_global = ease_in_quad(t)
    else: # Crouch/Land segments use smooth start/end
        t_eased_global = ease_in_out_sine(t)
    
    # Horizontal motion is linear for constant forward velocity, vertical is eased
    global_x = lerp(gx1, gx2, t)
    global_y = lerp(gy1, gy2, t_eased_global)

    # --- Interpolate Local Pose for each point ---
    t_eased_local = ease_in_out_sine(t)
    start_pose_local = KEYFRAME_POSES[start_kf_idx]
    end_pose_local = KEYFRAME_POSES[end_kf_idx]

    final_pose = []
    for i in range(len(start_pose_local)):
        lx1, ly1 = start_pose_local[i]
        lx2, ly2 = end_pose_local[i]
        local_x = lerp(lx1, lx2, t_eased_local)
        local_y = lerp(ly1, ly2, t_eased_local)

        # Combine global and local positions, then convert to Pygame screen coordinates
        final_x = global_x + local_x
        final_y = HEIGHT - (global_y + local_y)  # Invert Y-axis for screen display
        final_pose.append((int(final_x), int(final_y)))

    return final_pose

# --- Main Program Loop ---

def main():
    """Initializes Pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    frame_num = 0
    running = True

    while running:
        # Event handling to quit the animation
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Clear the screen with a black background
        screen.fill(BLACK)
        
        # Calculate and draw the points for the current frame
        pose = get_current_pose(frame_num)
        for point in pose:
            pygame.draw.circle(screen, WHITE, point, POINT_RADIUS)

        # Update the full display
        pygame.display.flip()

        # Advance to the next frame, looping at the end
        frame_num = (frame_num + 1) % TOTAL_FRAMES
        
        # Maintain the desired frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
