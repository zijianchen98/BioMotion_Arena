
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Man")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Point Definitions ---
# The 15 points representing a human figure.
# These names define the order in which coordinates are stored in poses.
POINT_NAMES = [
    "HEAD", "NECK",
    "L_SHOULDER", "R_SHOULDER",
    "L_ELBOW", "R_ELBOW",
    "L_WRIST", "R_WRIST",
    "TORSO",  # Mid-spine/pelvis center
    "L_HIP", "R_HIP",
    "L_KNEE", "R_KNEE",
    "L_ANKLE", "R_ANKLE"
]

# Relative coordinates for key poses.
# The origin (0,0) for these relative coordinates is set at the center of the hips/pelvis
# when the person is in the standing pose. Y increases upwards in this system.
# Unit scale: These values are in 'body units', which will be scaled to pixels later.
# Example: -50 for ankle Y means it's 50 units below the hip center.
# Example: 75 for head Y means it's 75 units above the hip center.

# Keyframe 0: Stand (reference pose)
k0_stand = {
    "L_ANKLE": (-20, -50), "R_ANKLE": ( 20, -50),
    "L_KNEE":  (-20, -10), "R_KNEE":  ( 20, -10),
    "L_HIP":   (-15, 0),   "R_HIP":   ( 15, 0),
    "TORSO":   (0,   20),
    "L_SHOULDER":(-20, 50), "R_SHOULDER":(20, 50),
    "NECK":    (0,   60),
    "HEAD":    (0,   75),
    "L_ELBOW": (-30, 30),  "R_ELBOW": ( 30, 30),
    "L_WRIST": (-25, 0),   "R_WRIST": ( 25, 0),
}

# Keyframe 1: Crouch (deep squat preparation for jump)
k1_crouch = {
    "L_ANKLE": (-20, -50), "R_ANKLE": ( 20, -50), # Ankles largely fixed
    "L_KNEE":  (-20, -35), "R_KNEE":  ( 20, -35), # Knees bent significantly
    "L_HIP":   (-15, -25), "R_HIP":   ( 15, -25), # Hips lowered
    "TORSO":   (0,   -5),
    "L_SHOULDER":(-25, 20), "R_SHOULDER":(25, 20), # Shoulders dropped, arms swung back
    "NECK":    (0,   30),
    "HEAD":    (0,   45),
    "L_ELBOW": (-40, 0),   "R_ELBOW": ( 40, 0),
    "L_WRIST": (-35, -20), "R_WRIST": ( 35, -20),
}

# Keyframe 2: Launch (push-off phase, body extending upwards)
k2_launch = {
    "L_ANKLE": (-20, -40), "R_ANKLE": ( 20, -40), # Heels lifting, feet pointing
    "L_KNEE":  (-20, -5),  "R_KNEE":  ( 20, -5),  # Knees extending
    "L_HIP":   (-15, 10),  "R_HIP":   ( 15, 10),  # Hips moving up
    "TORSO":   (0,   35),
    "L_SHOULDER":(-15, 60), "R_SHOULDER":(15, 60), # Arms swinging forward and up
    "NECK":    (0,   70),
    "HEAD":    (0,   85),
    "L_ELBOW": (-20, 50),  "R_ELBOW": ( 20, 50),
    "L_WRIST": (-10, 40),  "R_WRIST": ( 10, 40),
}

# Keyframe 3: Airborne Peak (highest point of the jump)
k3_peak = {
    "L_ANKLE": (-15, -10), "R_ANKLE": ( 15, -10), # Feet tucked slightly
    "L_KNEE":  (-15, 10),  "R_KNEE":  ( 15, 10),
    "L_HIP":   (-15, 25),  "R_HIP":   ( 15, 25),  # Hips highest relative to own base
    "TORSO":   (0,   45),
    "L_SHOULDER":(-10, 70), "R_SHOULDER":(10, 70), # Arms fully up
    "NECK":    (0,   80),
    "HEAD":    (0,   95),
    "L_ELBOW": (-10, 60),  "R_ELBOW": ( 10, 60),
    "L_WRIST": (-5, 50),   "R_WRIST": ( 5, 50),
}

# Keyframe 4: Descent (body falling, preparing for landing)
k4_descent = {
    "L_ANKLE": (-20, -40), "R_ANKLE": ( 20, -40),
    "L_KNEE":  (-20, -15), "R_KNEE":  ( 20, -15),
    "L_HIP":   (-15, 5),   "R_HIP":   ( 15, 5),
    "TORSO":   (0,   25),
    "L_SHOULDER":(-20, 55), "R_SHOULDER":(20, 55), # Arms lowering
    "NECK":    (0,   65),
    "HEAD":    (0,   80),
    "L_ELBOW": (-30, 35),  "R_ELBOW": ( 30, 35),
    "L_WRIST": (-25, 10),  "R_WRIST": ( 25, 10),
}

# Keyframe 5: Landing (impact absorption, body returning to crouch-like state)
k5_landing = {
    "L_ANKLE": (-20, -50), "R_ANKLE": ( 20, -50),
    "L_KNEE":  (-20, -35), "R_KNEE":  ( 20, -35),
    "L_HIP":   (-15, -25), "R_HIP":   ( 15, -25),
    "TORSO":   (0,   -5),
    "L_SHOULDER":(-25, 20), "R_SHOULDER":(25, 20),
    "NECK":    (0,   30),
    "HEAD":    (0,   45),
    "L_ELBOW": (-35, 5),   "R_ELBOW": ( 35, 5),
    "L_WRIST": (-30, -15), "R_WRIST": ( 30, -15),
}

# Sequence of relative poses for interpolation
KEY_POSES_RELATIVE = [k0_stand, k1_crouch, k2_launch, k3_peak, k4_descent, k5_landing, k0_stand]

# Overall Y-offset for the person's 'pelvis base' from its standing position.
# These values are in 'body units'. A positive value means the entire person
# moves upwards (lower Y pixel value), and negative means downwards (higher Y pixel value).
KEY_PELVIS_Y_OFFSETS_REL = [0, -25, 10, 100, 20, -25, 0]

# Durations for each animation segment (in frames)
SEGMENT_DURATIONS = [
    20, # Stand to Crouch
    15, # Crouch to Launch (fast acceleration)
    15, # Launch to Peak (fast ascent)
    20, # Peak to Descent (gravity effect)
    15, # Descent to Landing (fast impact)
    20  # Landing to Recover (return to stand)
]
TOTAL_ANIMATION_FRAMES = sum(SEGMENT_DURATIONS)

# --- Animation Parameters ---
PERSON_SCALE = 2.0  # Scale factor for the person's size on screen (e.g., 1 unit = 2 pixels)
POINT_RADIUS = 3    # Radius of each point-light in pixels

# Screen coordinates for the base of the person.
# GROUND_Y_PX is the pixel Y where the feet (ankles) of the standing person should be.
GROUND_Y_PX = SCREEN_HEIGHT - 100
# Calculate the Y-pixel coordinate for the pelvis (Y=0 in relative coords) when standing.
# Ankle is at relative Y=-50, so pelvis is 50 units (scaled) above the ground.
PELVIS_Y_OFFSET_FROM_GROUND_FOR_STANDING = abs(k0_stand["L_ANKLE"][1])
PELVIS_Y_PX_FOR_STANDING = GROUND_Y_PX - (PELVIS_Y_OFFSET_FROM_GROUND_FOR_STANDING * PERSON_SCALE)

# X-coordinate for the horizontal center of the person on screen.
CENTER_X_PX = SCREEN_WIDTH // 2

# Easing function for smoother transitions (Quadratic ease-in-out)
def ease_in_out_quad(t):
    # t ranges from 0 to 1
    t *= 2
    if t < 1:
        return 0.5 * t * t
    t -= 1
    return -0.5 * (t * (t - 2) - 1)

# Linear interpolation function
def lerp(a, b, t):
    return a * (1 - t) + b

# Function to get the current pose (pixel coordinates for all points) based on the animation frame
def get_current_pose(frame_num):
    current_frame = frame_num % TOTAL_ANIMATION_FRAMES
    
    segment_start_frame = 0
    
    for i in range(len(SEGMENT_DURATIONS)):
        segment_end_frame = segment_start_frame + SEGMENT_DURATIONS[i]
        
        if current_frame >= segment_start_frame and current_frame < segment_end_frame:
            # Calculate progress within the current segment (0.0 to 1.0)
            progress_in_segment = (current_frame - segment_start_frame) / SEGMENT_DURATIONS[i]
            
            # Apply easing function for smooth acceleration/deceleration
            t_eased = ease_in_out_quad(progress_in_segment)
            
            # Get the start and end poses for this segment
            start_pose_relative = KEY_POSES_RELATIVE[i]
            end_pose_relative = KEY_POSES_RELATIVE[i+1]
            
            # Get the start and end global Y-offsets for the pelvis
            start_pelvis_y_offset_rel = KEY_PELVIS_Y_OFFSETS_REL[i]
            end_pelvis_y_offset_rel = KEY_PELVIS_Y_OFFSETS_REL[i+1]
            
            # Interpolate the current global Y-offset for the pelvis
            current_pelvis_y_offset_rel = lerp(start_pelvis_y_offset_rel, end_pelvis_y_offset_rel, t_eased)
            
            display_points = []
            for point_name in POINT_NAMES:
                # Interpolate each point's relative (x, y) coordinates
                start_x, start_y = start_pose_relative[point_name]
                end_x, end_y = end_pose_relative[point_name]
                
                interp_x = lerp(start_x, end_x, t_eased)
                interp_y = lerp(start_y, end_y, t_eased)
                
                # Convert relative coordinates to absolute screen coordinates
                # Scale relative coordinates by PERSON_SCALE
                scaled_x = interp_x * PERSON_SCALE
                scaled_y = interp_y * PERSON_SCALE
                
                # Calculate the global Y-coordinate for the current pose's pelvis.
                # Pygame Y increases downwards, our relative Y increases upwards.
                # So, a positive `current_pelvis_y_offset_rel` (moving up) means a smaller Pygame Y.
                global_pelvis_y_px = PELVIS_Y_PX_FOR_STANDING - (current_pelvis_y_offset_rel * PERSON_SCALE)
                
                # Apply the global pelvis position and invert Y-axis for Pygame
                screen_x = CENTER_X_PX + scaled_x
                screen_y = global_pelvis_y_px - scaled_y 
                
                display_points.append((int(screen_x), int(screen_y)))
            
            return display_points
            
        segment_start_frame = segment_end_frame
        
    return [] # Should not be reached if total frames calculation is correct

# --- Main animation loop ---
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Draw solid black background

    # Get the current position of all 15 points
    current_display_points = get_current_pose(frame_count)

    # Draw each point as a white circle
    for point_coord in current_display_points:
        pygame.draw.circle(screen, WHITE, point_coord, POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    frame_count += 1
    clock.tick(FPS) # Control the animation speed

pygame.quit()
