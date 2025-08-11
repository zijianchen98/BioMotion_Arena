
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 4

# Humanoid model (15 points) key poses
# Points order: Head, Neck, R_Shoulder, L_Shoulder, R_Elbow, L_Elbow, R_Wrist, L_Wrist, Torso, R_Hip, L_Hip, R_Knee, L_Knee, R_Ankle, L_Ankle

# Define key poses as lists of (x, y) coordinates
# These coordinates are absolute pixel positions on the screen
# The overall 'scale' factor helps adjust the size of the figure.
scale = 1.8 

# --- STANDING POSE (slightly slumped, representing a 'sadman with heavy weight') ---
# The origin for this pose is set so the feet are near the bottom of the screen.
x_offset_stand = SCREEN_WIDTH // 2
y_offset_stand = SCREEN_HEIGHT - 100 

standing_slumped_pose = [
    # Head (0)
    (x_offset_stand, y_offset_stand - 200 * scale),
    # Neck (1)
    (x_offset_stand, y_offset_stand - 170 * scale),
    # R_Shoulder (2)
    (x_offset_stand + 35 * scale, y_offset_stand - 140 * scale),
    # L_Shoulder (3)
    (x_offset_stand - 35 * scale, y_offset_stand - 140 * scale),
    # R_Elbow (4) - slightly bent arm, resting
    (x_offset_stand + 45 * scale, y_offset_stand - 80 * scale),
    # L_Elbow (5)
    (x_offset_stand - 45 * scale, y_offset_stand - 80 * scale),
    # R_Wrist (6) - hand near hip
    (x_offset_stand + 35 * scale, y_offset_stand - 20 * scale),
    # L_Wrist (7)
    (x_offset_stand - 35 * scale, y_offset_stand - 20 * scale),
    # Torso (8) - approximate center mass of upper body
    (x_offset_stand, y_offset_stand - 100 * scale),
    # R_Hip (9)
    (x_offset_stand + 15 * scale, y_offset_stand - 0 * scale),
    # L_Hip (10)
    (x_offset_stand - 15 * scale, y_offset_stand - 0 * scale),
    # R_Knee (11)
    (x_offset_stand + 15 * scale, y_offset_stand + 60 * scale),
    # L_Knee (12)
    (x_offset_stand - 15 * scale, y_offset_stand + 60 * scale),
    # R_Ankle (13)
    (x_offset_stand + 15 * scale, y_offset_stand + 120 * scale),
    # L_Ankle (14)
    (x_offset_stand - 15 * scale, y_offset_stand + 120 * scale),
]

# Adjustments for slumped posture to convey "sadman with heavy weight"
# Head and neck are lower, shoulders are slightly inward and lower, torso slightly compressed.
standing_slumped_pose[0] = (standing_slumped_pose[0][0], standing_slumped_pose[0][1] + 15)
standing_slumped_pose[1] = (standing_slumped_pose[1][0], standing_slumped_pose[1][1] + 10)
standing_slumped_pose[2] = (standing_slumped_pose[2][0] - 5, standing_slumped_pose[2][1] + 5)
standing_slumped_pose[3] = (standing_slumped_pose[3][0] + 5, standing_slumped_pose[3][1] + 5)
standing_slumped_pose[8] = (standing_slumped_pose[8][0], standing_slumped_pose[8][1] + 5)


# --- SITTING POSE (on the ground, legs bent, body slightly hunched) ---
# The origin for this pose is set so the hips are near the bottom of the screen.
x_offset_sit = SCREEN_WIDTH // 2
y_offset_sit = SCREEN_HEIGHT - 100 

sitting_pose = [
    # Head (0)
    (x_offset_sit, y_offset_sit - 100 * scale),
    # Neck (1)
    (x_offset_sit, y_offset_sit - 70 * scale),
    # R_Shoulder (2)
    (x_offset_sit + 30 * scale, y_offset_sit - 40 * scale),
    # L_Shoulder (3)
    (x_offset_sit - 30 * scale, y_offset_sit - 40 * scale),
    # R_Elbow (4) - arms resting on knees or slightly out
    (x_offset_sit + 40 * scale, y_offset_sit + 0 * scale),
    # L_Elbow (5)
    (x_offset_sit - 40 * scale, y_offset_sit + 0 * scale),
    # R_Wrist (6)
    (x_offset_sit + 30 * scale, y_offset_sit + 40 * scale),
    # L_Wrist (7)
    (x_offset_sit - 30 * scale, y_offset_sit + 40 * scale),
    # Torso (8)
    (x_offset_sit, y_offset_sit - 20 * scale),
    # R_Hip (9)
    (x_offset_sit + 15 * scale, y_offset_sit + 0 * scale),
    # L_Hip (10)
    (x_offset_sit - 15 * scale, y_offset_sit + 0 * scale),
    # R_Knee (11) - bent forward
    (x_offset_sit + 50 * scale, y_offset_sit + 40 * scale),
    # L_Knee (12)
    (x_offset_sit - 50 * scale, y_offset_sit + 40 * scale),
    # R_Ankle (13) - feet flat on ground
    (x_offset_sit + 50 * scale, y_offset_sit + 80 * scale),
    # L_Ankle (14)
    (x_offset_sit - 50 * scale, y_offset_sit + 80 * scale),
]

# --- LYING POSE (supine, head to the left, feet to the right) ---
# The figure is rotated and translated to be horizontal on the screen.
# The origin for this pose is set to the center of the screen.
x_offset_lie = SCREEN_WIDTH // 2
y_offset_lie = SCREEN_HEIGHT // 2 

lying_pose = [
    # Head (0)
    (x_offset_lie - 200 * scale, y_offset_lie),
    # Neck (1)
    (x_offset_lie - 150 * scale, y_offset_lie),
    # R_Shoulder (2) - viewer's right shoulder (top in this orientation)
    (x_offset_lie - 100 * scale, y_offset_lie - 30 * scale),
    # L_Shoulder (3) - viewer's left shoulder (bottom in this orientation)
    (x_offset_lie - 100 * scale, y_offset_lie + 30 * scale),
    # R_Elbow (4) - arm by side, slightly bent
    (x_offset_lie - 50 * scale, y_offset_lie - 25 * scale),
    # L_Elbow (5)
    (x_offset_lie - 50 * scale, y_offset_lie + 25 * scale),
    # R_Wrist (6)
    (x_offset_lie + 0 * scale, y_offset_lie - 20 * scale),
    # L_Wrist (7)
    (x_offset_lie + 0 * scale, y_offset_lie + 20 * scale),
    # Torso (8) - approximate mid-spine
    (x_offset_lie - 70 * scale, y_offset_lie),
    # R_Hip (9)
    (x_offset_lie + 50 * scale, y_offset_lie - 15 * scale),
    # L_Hip (10)
    (x_offset_lie + 50 * scale, y_offset_lie + 15 * scale),
    # R_Knee (11) - legs slightly bent
    (x_offset_lie + 120 * scale, y_offset_lie - 20 * scale),
    # L_Knee (12)
    (x_offset_lie + 120 * scale, y_offset_lie + 20 * scale),
    # R_Ankle (13)
    (x_offset_lie + 180 * scale, y_offset_lie - 15 * scale),
    # L_Ankle (14)
    (x_offset_lie + 180 * scale, y_offset_lie + 15 * scale),
]


# Animation parameters
FPS = 30
clock = pygame.time.Clock()

# Total animation loop duration (frames)
# A slower, more deliberate motion for "sadman with heavy weight"
# The total duration of 16 seconds ensures the motion is perceived as labored.
ANIM_TOTAL_FRAMES = 480 # 16 seconds at 30 FPS for a full cycle (down and up)

# Define animation segments (start_frame, end_frame, start_pose, end_pose)
# The animation cycles from standing, to sitting, to lying, holds, then reverses.
segments = [
    # Phase 1: Slumped Stand to Sit (duration: 4 seconds = 120 frames)
    # This slow descent shows effort.
    {"start_frame": 0, "end_frame": 120, "start_pose": standing_slumped_pose, "end_pose": sitting_pose},
    # Phase 2: Sit to Lie (duration: 6 seconds = 180 frames)
    # The primary action of "lying down", again slow and deliberate.
    {"start_frame": 120, "end_frame": 300, "start_pose": sitting_pose, "end_pose": lying_pose},
    # Phase 3: Hold Lie (duration: 3 seconds = 90 frames)
    # A period where the person remains lying down.
    {"start_frame": 300, "end_frame": 390, "start_pose": lying_pose, "end_pose": lying_pose},
    # Phase 4: Lie to Sit (duration: 2 seconds = 60 frames)
    # The start of getting up.
    {"start_frame": 390, "end_frame": 450, "start_pose": lying_pose, "end_pose": sitting_pose},
    # Phase 5: Sit to Slumped Stand (duration: 1 second = 30 frames)
    # Completing the cycle to return to the initial slumped standing pose.
    {"start_frame": 450, "end_frame": ANIM_TOTAL_FRAMES, "start_pose": sitting_pose, "end_pose": standing_slumped_pose},
]

current_frame_counter = 0
running = True

def lerp_point(p1, p2, t):
    """Linear interpolation between two 2D points."""
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))

# Main animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen with black background

    current_pose_points = []
    
    # Find the current animation segment based on the frame counter
    current_segment = None
    for segment in segments:
        if segment["start_frame"] <= current_frame_counter < segment["end_frame"]:
            current_segment = segment
            break
    
    if current_segment:
        frame_in_segment = current_frame_counter - current_segment["start_frame"]
        segment_duration = current_segment["end_frame"] - current_segment["start_frame"]
        
        # Calculate interpolation factor 't' (0 to 1)
        if segment_duration > 0:
            t = frame_in_segment / segment_duration
            # Apply ease-in/ease-out for smoother motion (cosine interpolation)
            # This makes the movement start and end softly, mimicking natural joint movement.
            t_eased = 0.5 - 0.5 * math.cos(t * math.pi)
        else: # For segments with zero duration (e.g., pure holds, though handled by start_pose==end_pose)
            t_eased = 0 

        # Interpolate each of the 15 points
        for i in range(15):
            interpolated_point = lerp_point(current_segment["start_pose"][i], current_segment["end_pose"][i], t_eased)
            current_pose_points.append(interpolated_point)
    else:
        # Fallback: if outside defined segments (should not happen with modulo on counter),
        # default to the starting (slumped standing) pose.
        current_pose_points = list(standing_slumped_pose)

    # Draw the points on the screen
    for point in current_pose_points:
        # Ensure points are within screen bounds and convert to int for drawing
        draw_x = int(max(0, min(SCREEN_WIDTH - 1, point[0])))
        draw_y = int(max(0, min(SCREEN_HEIGHT - 1, point[1])))
        pygame.draw.circle(screen, WHITE, (draw_x, draw_y), POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    # Update frame counter and control the frame rate
    current_frame_counter = (current_frame_counter + 1) % ANIM_TOTAL_FRAMES
    clock.tick(FPS)

pygame.quit() # Uninitialize Pygame modules
