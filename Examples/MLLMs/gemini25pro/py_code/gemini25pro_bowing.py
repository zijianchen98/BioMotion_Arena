
import pygame
import sys
import math

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
DOT_RADIUS = 5

# --- Animation Parameters ---
ANIMATION_CYCLE_S = 4.0
BOW_DURATION_S = 1.5
PAUSE_LOW_S = 0.5
RISE_DURATION_S = 1.5
PAUSE_HIGH_S = ANIMATION_CYCLE_S - (BOW_DURATION_S + PAUSE_LOW_S + RISE_DURATION_S)

# --- Figure Parameters ---
FIGURE_SCALE = 2.2
FIGURE_CENTER_X = SCREEN_WIDTH // 2
FIGURE_CENTER_Y = SCREEN_HEIGHT - 100
BOW_ANGLE_DEG = 80.0

# --- Joint Definitions ---
# (local_x, local_y) with (0,0) at the ground between the ankles. Y-axis points up.
# The body is defined in an upright, standing pose.
KEYFRAME_STAND = [
    (0, 165),    # 0: Head
    (0, 145),    # 1: Neck
    (-25, 140),  # 2: L Shoulder
    (25, 140),   # 3: R Shoulder
    (-28, 100),  # 4: L Elbow
    (28, 100),   # 5: R Elbow
    (-31, 60),   # 6: L Wrist
    (31, 60),    # 7: R Wrist
    (0, 85),     # 8: Pelvis (pivot point)
    (-15, 85),   # 9: L Hip
    (15, 85),    # 10: R Hip
    (-18, 45),   # 11: L Knee
    (18, 45),    # 12: R Knee
    (-20, 0),    # 13: L Ankle
    (20, 0),     # 14: R Ankle
]

def create_bow_keyframe(stand_pose, angle_deg):
    """Creates the bowed keyframe by rotating the upper body around the pelvis."""
    angle_rad = math.radians(angle_deg)
    cos_angle = math.cos(angle_rad)
    
    pivot_point_idx = 8 # Pelvis index
    pivot_x, pivot_y = stand_pose[pivot_point_idx]
    
    bow_pose = []
    for i, (x, y) in enumerate(stand_pose):
        # Lower body (hips and below) remains stationary
        if i >= pivot_point_idx:
            bow_pose.append((x, y))
        else:
            # Upper body points rotate around the pivot.
            # This simulates a 3D forward bend projected onto a 2D plane by
            # foreshortening the vertical distance from the pivot.
            rel_y = y - pivot_y
            new_y = pivot_y + rel_y * cos_angle
            bow_pose.append((x, new_y))
            
    return bow_pose

KEYFRAME_BOW = create_bow_keyframe(KEYFRAME_STAND, BOW_ANGLE_DEG)

def lerp(a, b, t):
    """Linearly interpolates between a and b by a factor of t."""
    return a + (b - a) * t

def ease_in_out(t):
    """Applies an ease-in, ease-out curve to the interpolation factor t."""
    return (1 - math.cos(t * math.pi)) / 2

def transform_to_screen(point):
    """Converts local figure coordinates to screen coordinates."""
    local_x, local_y = point
    screen_x = FIGURE_CENTER_X + local_x * FIGURE_SCALE
    screen_y = FIGURE_CENTER_Y - local_y * FIGURE_SCALE # Invert Y-axis for Pygame
    return int(screen_x), int(screen_y)

def main():
    """Initializes Pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Bowing")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        total_time_s = pygame.time.get_ticks() / 1000.0
        time_in_cycle = total_time_s % ANIMATION_CYCLE_S
        
        interpolation_factor = 0.0
        
        # Determine the current phase of the animation cycle
        if 0 <= time_in_cycle < BOW_DURATION_S:
            # Bowing down
            progress = time_in_cycle / BOW_DURATION_S
            interpolation_factor = ease_in_out(progress)
        elif time_in_cycle < BOW_DURATION_S + PAUSE_LOW_S:
            # Paused at the bottom of the bow
            interpolation_factor = 1.0
        elif time_in_cycle < BOW_DURATION_S + PAUSE_LOW_S + RISE_DURATION_S:
            # Rising up
            progress = (time_in_cycle - (BOW_DURATION_S + PAUSE_LOW_S)) / RISE_DURATION_S
            interpolation_factor = 1.0 - ease_in_out(progress)
        else:
            # Paused standing
            interpolation_factor = 0.0

        screen.fill(BLACK)

        # Calculate and draw each point based on the interpolated position
        for i in range(len(KEYFRAME_STAND)):
            start_pos = KEYFRAME_STAND[i]
            end_pos = KEYFRAME_BOW[i]

            current_x = lerp(start_pos[0], end_pos[0], interpolation_factor)
            current_y = lerp(start_pos[1], end_pos[1], interpolation_factor)
            
            screen_pos = transform_to_screen((current_x, current_y))
            pygame.draw.circle(screen, WHITE, screen_pos, DOT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
