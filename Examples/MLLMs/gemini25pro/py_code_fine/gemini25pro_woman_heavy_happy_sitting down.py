
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 6

# --- Animation Timing ---
# Duration in frames (at 60 FPS). The movement is slow to imply heavy weight.
DURATION_SIT = 180  # 3.0 seconds for a controlled sit-down action
DURATION_STAND = 180 # 3.0 seconds to stand up
DURATION_PAUSE = 60 # 1.0 second pause in standing and seated positions

TOTAL_CYCLE_FRAMES = DURATION_SIT + DURATION_PAUSE + DURATION_STAND + DURATION_PAUSE

# --- Keyframe Data for 15-point skeleton ---
# The skeleton consists of: head, spine_chest, spine_pelvis,
# l_shoulder, r_shoulder, l_elbow, r_elbow, l_wrist, r_wrist,
# l_hip, r_hip, l_knee, r_knee, l_ankle, r_ankle.
# Coordinates are defined for 3 key poses: Standing, Mid-squat, and Seated.
poses = [
    # Pose 0: Standing
    {
        "head": (350, 220), "spine_chest": (350, 275), "spine_pelvis": (350, 380),
        "l_shoulder": (320, 270), "r_shoulder": (380, 270),
        "l_elbow": (310, 325), "r_elbow": (390, 325),
        "l_wrist": (300, 380), "r_wrist": (400, 380),
        "l_hip": (330, 380), "r_hip": (370, 380),
        "l_knee": (330, 470), "r_knee": (370, 470),
        "l_ankle": (330, 550), "r_ankle": (370, 550),
    },
    # Pose 1: Mid-squat (maximum forward lean for counterbalance)
    {
        "head": (380, 270), "spine_chest": (380, 325), "spine_pelvis": (400, 425),
        "l_shoulder": (350, 320), "r_shoulder": (410, 320),
        "l_elbow": (320, 350), "r_elbow": (440, 350),
        "l_wrist": (290, 380), "r_wrist": (470, 380),
        "l_hip": (380, 425), "r_hip": (420, 425),
        "l_knee": (335, 480), "r_knee": (375, 480),
        "l_ankle": (330, 550), "r_ankle": (370, 550),
    },
    # Pose 2: Seated
    {
        "head": (450, 310), "spine_chest": (450, 365), "spine_pelvis": (450, 470),
        "l_shoulder": (420, 360), "r_shoulder": (480, 360),
        "l_elbow": (400, 410), "r_elbow": (500, 410),
        "l_wrist": (370, 460), "r_wrist": (530, 460),
        "l_hip": (430, 470), "r_hip": (470, 470),
        "l_knee": (340, 490), "r_knee": (380, 490),
        "l_ankle": (330, 550), "r_ankle": (370, 550),
    }
]

# --- Helper Functions ---
def ease_in_out(t):
    """A smooth easing function for natural motion (cosine)."""
    return 0.5 * (1 - math.cos(math.pi * t))

def lerp(p1, p2, t):
    """Linear interpolation for a single value."""
    return p1 * (1 - t) + p2 * t

def interpolate_point(p1, p2, t):
    """Linear interpolation for a 2D point."""
    x = lerp(p1[0], p2[0], t)
    y = lerp(p1[1], p2[1], t)
    return (x, y)

def get_current_pose(frame_count, poses_data):
    """Calculates the current pose by interpolating between keyframes based on the animation cycle."""
    
    current_frame_in_cycle = frame_count % TOTAL_CYCLE_FRAMES
    
    # Phase 1: Sitting down (Pose 0 -> Pose 1 -> Pose 2)
    if current_frame_in_cycle < DURATION_SIT:
        progress = current_frame_in_cycle / DURATION_SIT
        if progress < 0.5:
            # First half: Standing to Mid-squat
            t = progress * 2
            eased_t = ease_in_out(t)
            start_pose, end_pose = poses_data[0], poses_data[1]
        else:
            # Second half: Mid-squat to Seated
            t = (progress - 0.5) * 2
            eased_t = ease_in_out(t)
            start_pose, end_pose = poses_data[1], poses_data[2]
            
    # Phase 2: Paused while seated
    elif current_frame_in_cycle < DURATION_SIT + DURATION_PAUSE:
        return poses_data[2]
        
    # Phase 3: Standing up (Pose 2 -> Pose 1 -> Pose 0)
    elif current_frame_in_cycle < DURATION_SIT + DURATION_PAUSE + DURATION_STAND:
        progress = (current_frame_in_cycle - (DURATION_SIT + DURATION_PAUSE)) / DURATION_STAND
        if progress < 0.5:
            # First half: Seated to Mid-squat
            t = progress * 2
            eased_t = ease_in_out(t)
            start_pose, end_pose = poses_data[2], poses_data[1]
        else:
            # Second half: Mid-squat to Standing
            t = (progress - 0.5) * 2
            eased_t = ease_in_out(t)
            start_pose, end_pose = poses_data[1], poses_data[0]
            
    # Phase 4: Paused while standing
    else:
        return poses_data[0]
        
    # Calculate the interpolated pose for the current frame
    current_pose = {}
    for joint in poses_data[0].keys():
        p1 = start_pose[joint]
        p2 = end_pose[joint]
        current_pose[joint] = interpolate_point(p1, p2, eased_t)
        
    return current_pose

# --- Main Program ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: A happywoman with heavy weight is sitting down")
clock = pygame.time.Clock()

frame_count = 0
running = True

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- Update ---
    # Calculate the coordinates for all 15 points for the current frame
    current_points = get_current_pose(frame_count, poses)

    # --- Drawing ---
    screen.fill(BACKGROUND_COLOR)
    
    # Draw each point of the current pose
    for joint, pos in current_points.items():
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)
        
    pygame.display.flip()
    
    # --- Tick ---
    frame_count += 1
    clock.tick(FPS)

pygame.quit()
