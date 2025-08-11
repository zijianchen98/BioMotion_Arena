
import pygame
import math

# This program creates a point-light animation of a sad man with a heavy weight jumping.
# The animation is designed to be biomechanically plausible and convey the emotion and effort.

# --- Core Animation Parameters ---
WIDTH, HEIGHT = 800, 900  # Window dimensions
FPS = 60                  # Frames per second for smooth animation
POINT_RADIUS = 7          # Size of the white dots
GROUND_Y = 750            # Vertical position of the ground

# --- Color Definitions ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Keyframe Pose Definitions ---
# Each pose is a list of 15 (x, y) tuples representing the joints.
# The coordinates are absolute screen positions.
# Point Order: Head, Sternum, Pelvis, LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist, LHip, RHip, LKnee, RKnee, LAnkle, RAnkle
# Left/Right is from the figure's perspective. On screen, left parts have smaller x-coordinates.
CENTER_X = WIDTH // 2

# Initial Pose: Standing, but slumped to convey sadness. Shoulders are rounded, head is low.
slumped_stand = [
    (CENTER_X, 350),      # 0 Head (low)
    (CENTER_X, 430),      # 1 Sternum (slumped)
    (CENTER_X, 530),      # 2 Pelvis
    (CENTER_X - 40, 435), # 3 L Shoulder (rounded forward)
    (CENTER_X + 40, 435), # 4 R Shoulder
    (CENTER_X - 50, 510), # 5 L Elbow
    (CENTER_X + 50, 510), # 6 R Elbow
    (CENTER_X - 55, 580), # 7 L Wrist
    (CENTER_X + 55, 580), # 8 R Wrist
    (CENTER_X - 20, 530), # 9 L Hip
    (CENTER_X + 20, 530), # 10 R Hip
    (CENTER_X - 25, 640), # 11 L Knee (slightly bent)
    (CENTER_X + 25, 640), # 12 R Knee
    (CENTER_X - 30, GROUND_Y), # 13 L Ankle
    (CENTER_X + 30, GROUND_Y), # 14 R Ankle
]

# Crouch Pose: Bending down slowly, gathering energy under strain.
deep_crouch = [
    (CENTER_X, 450),      # 0 Head
    (CENTER_X, 530),      # 1 Sternum
    (CENTER_X, 630),      # 2 Pelvis
    (CENTER_X - 35, 535), # 3 L Shoulder
    (CENTER_X + 35, 535), # 4 R Shoulder
    (CENTER_X - 60, 590), # 5 L Elbow (back for balance)
    (CENTER_X + 60, 590), # 6 R Elbow
    (CENTER_X - 70, 640), # 7 L Wrist
    (CENTER_X + 70, 640), # 8 R Wrist
    (CENTER_X - 25, 630), # 9 L Hip
    (CENTER_X + 25, 630), # 10 R Hip
    (CENTER_X - 35, 700), # 11 L Knee
    (CENTER_X + 35, 700), # 12 R Knee
    (CENTER_X - 30, GROUND_Y), # 13 L Ankle
    (CENTER_X + 30, GROUND_Y), # 14 R Ankle
]

# Takeoff Pose: A strained extension. The body is pushing off the ground.
takeoff = [
    (CENTER_X, 330),      # 0 Head
    (CENTER_X, 410),      # 1 Sternum
    (CENTER_X, 510),      # 2 Pelvis
    (CENTER_X - 40, 415), # 3 L Shoulder
    (CENTER_X + 40, 415), # 4 R Shoulder
    (CENTER_X - 45, 490), # 5 L Elbow (swinging slightly forward)
    (CENTER_X + 45, 490), # 6 R Elbow
    (CENTER_X - 50, 560), # 7 L Wrist
    (CENTER_X + 50, 560), # 8 R Wrist
    (CENTER_X - 20, 510), # 9 L Hip
    (CENTER_X + 20, 510), # 10 R Hip
    (CENTER_X - 25, 630), # 11 L Knee (extending)
    (CENTER_X + 25, 630), # 12 R Knee
    (CENTER_X - 30, GROUND_Y - 5), # 13 L Ankle (on toes)
    (CENTER_X + 30, GROUND_Y - 5), # 14 R Ankle
]

# Peak Air Pose: The highest point of the jump, which is low to show weakness/weight.
JUMP_APEX_Y_OFFSET = -90
peak_air = [
    (p[0], p[1] + JUMP_APEX_Y_OFFSET) for p in [
        (CENTER_X, 330), (CENTER_X, 410), (CENTER_X, 510),
        (CENTER_X - 40, 415), (CENTER_X + 40, 415),
        (CENTER_X - 45, 480), (CENTER_X + 45, 480),
        (CENTER_X - 50, 530), (CENTER_X + 50, 530),
        (CENTER_X - 20, 510), (CENTER_X + 20, 510),
        (CENTER_X - 25, 610), (CENTER_X + 25, 610),
        (CENTER_X - 30, 700), (CENTER_X + 30, 700),
    ]
]

# Landing Preparation Pose: Legs extend downwards to absorb the coming impact.
pre_land = [
    (p[0], p[1] + JUMP_APEX_Y_OFFSET + 50) for p in [
        (CENTER_X, 330), (CENTER_X, 410), (CENTER_X, 510),
        (CENTER_X - 45, 415), (CENTER_X + 45, 415),
        (CENTER_X - 55, 490), (CENTER_X + 55, 490),
        (CENTER_X - 60, 560), (CENTER_X + 60, 560),
        (CENTER_X - 20, 510), (CENTER_X + 20, 510),
        (CENTER_X - 25, 630), (CENTER_X + 25, 630),
        (CENTER_X - 30, GROUND_Y - 15), (CENTER_X + 30, GROUND_Y - 15),
    ]
]


# Landing Impact Pose: A heavy landing with a deep bend to absorb force.
land_impact = [
    (CENTER_X, 470),      # 0 Head
    (CENTER_X, 550),      # 1 Sternum
    (CENTER_X, 650),      # 2 Pelvis
    (CENTER_X - 45, 555), # 3 L Shoulder
    (CENTER_X + 45, 555), # 4 R Shoulder
    (CENTER_X - 65, 630), # 5 L Elbow (out for balance)
    (CENTER_X + 65, 630), # 6 R Elbow
    (CENTER_X - 75, 690), # 7 L Wrist
    (CENTER_X + 75, 690), # 8 R Wrist
    (CENTER_X - 25, 650), # 9 L Hip
    (CENTER_X + 25, 650), # 10 R Hip
    (CENTER_X - 35, 710), # 11 L Knee (deep bend)
    (CENTER_X + 35, 710), # 12 R Knee
    (CENTER_X - 30, GROUND_Y), # 13 L Ankle
    (CENTER_X + 30, GROUND_Y), # 14 R Ankle
]

# --- Timeline ---
# Associates frame numbers with poses to define the motion sequence and timing.
KEYFRAMES = [
    (0, slumped_stand),
    (35, deep_crouch),    # Slow preparation
    (42, takeoff),        # Quick, strained takeoff
    (55, peak_air),       # Short air time, low peak
    (65, pre_land),       # Preparing for landing
    (72, land_impact),    # Hard impact
    (130, slumped_stand)  # Long, slow recovery
]
TOTAL_FRAMES = KEYFRAMES[-1][0]

# --- Interpolation Functions ---

def lerp(v1, v2, t):
    """Linear interpolation between two values."""
    return v1 + (v2 - v1) * t

def interpolate_points(p1, p2, t):
    """Linear interpolation between two (x, y) points."""
    x = lerp(p1[0], p2[0], t)
    y = lerp(p1[1], p2[1], t)
    return (x, y)

def get_current_pose(frame_num):
    """
    Calculates the current pose by interpolating between the relevant keyframes.
    Applies an easing function for smoother, more natural motion.
    """
    frame_num %= TOTAL_FRAMES

    # Find the two keyframes that bracket the current frame
    start_keyframe = KEYFRAMES[0]
    end_keyframe = KEYFRAMES[1]
    for i in range(len(KEYFRAMES) - 1):
        if KEYFRAMES[i][0] <= frame_num < KEYFRAMES[i+1][0]:
            start_keyframe = KEYFRAMES[i]
            end_keyframe = KEYFRAMES[i+1]
            break

    frame_start, pose_start = start_keyframe
    frame_end, pose_end = end_keyframe

    # Calculate the interpolation factor 't'
    duration = frame_end - frame_start
    if duration == 0:
        t = 0.0
    else:
        t = (frame_num - frame_start) / duration
    
    # Apply a smoothstep (ease-in, ease-out) easing function to 't'
    t = t * t * (3.0 - 2.0 * t)

    # Interpolate each of the 15 points in the pose
    current_points = [
        interpolate_points(pose_start[i], pose_end[i], t)
        for i in range(15)
    ]
    return current_points


# --- Main Application ---

def main():
    """Initializes pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Man Jumping with Heavy Weight")
    clock = pygame.time.Clock()

    frame_counter = 0
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # --- Logic ---
        # Get the interpolated positions of all points for the current frame
        points = get_current_pose(frame_counter)

        # --- Drawing ---
        screen.fill(BLACK)
        for point in points:
            # Cast coordinates to integers for drawing
            pos = (int(point[0]), int(point[1]))
            pygame.draw.circle(screen, WHITE, pos, POINT_RADIUS)
        
        pygame.display.flip()

        # --- Update ---
        frame_counter += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
