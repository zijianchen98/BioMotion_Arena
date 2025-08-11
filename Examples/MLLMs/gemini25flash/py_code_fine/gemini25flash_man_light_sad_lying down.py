
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Lying Sadman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# --- Biomechanical Model (15 points) ---
# Each point represents a key joint or body part.

# Joint names, mapping to a simplified human skeleton for a point-light display.
JOINT_NAMES = [
    "Head", "Neck",
    "R_Shoulder", "L_Shoulder",
    "R_Elbow", "L_Elbow",
    "R_Wrist", "L_Wrist",
    "R_Hip", "L_Hip",
    "R_Knee", "L_Knee",
    "R_Ankle", "L_Ankle",
    "Spine_Mid" # Represents the sternum/upper torso center
]

# Initial positions for a person lying supine (on their back), viewed from above.
# The body will be oriented vertically on the screen (head at the top, feet at the bottom).
# Coordinates are normalized (e.g., from -1 to 1) relative to the figure's approximate center.
# These values are adjusted to represent a "sadman lying down" base pose:
# Arms are slightly closer to the body, legs are subtly more bent/relaxed, and the head is slightly slumped.
initial_positions_normalized = {
    "Head":             (0.0, -0.82),   # Slightly lower/slumped head
    "Neck":             (0.0, -0.67),
    "R_Shoulder":       (-0.18, -0.55), # Right shoulder (person's right), appears on left of screen center
    "L_Shoulder":       (0.18, -0.55),  # Left shoulder (person's left), appears on right of screen center
    "Spine_Mid":        (0.0, -0.30),   # Roughly sternum/upper torso center
    "R_Elbow":          (-0.20, -0.15), # Right elbow, arms bent slightly inwards, resting near torso
    "L_Elbow":          (0.20, -0.15),  # Left elbow
    "R_Wrist":          (-0.15, 0.05),  # Right wrist, hands resting near hips/pelvis
    "L_Wrist":          (0.15, 0.05),   # Left wrist
    "R_Hip":            (-0.10, 0.10),  # Right hip
    "L_Hip":            (0.10, 0.10),   # Left hip
    "R_Knee":           (-0.12, 0.45),  # Right knee, legs slightly bent/curled
    "L_Knee":           (0.12, 0.45),   # Left knee
    "R_Ankle":          (-0.08, 0.65),  # Right ankle, feet relaxed
    "L_Ankle":          (0.08, 0.65),   # Left ankle
}

# Scale factor to map normalized coordinates to screen pixels
BODY_SCALE = 200 # Adjust this to make the figure larger/smaller on screen
BODY_OFFSET_X = SCREEN_WIDTH // 2  # Center the figure horizontally
BODY_OFFSET_Y = SCREEN_HEIGHT // 2.5 # Shift slightly up from vertical center to ensure full body is visible

# --- Animation parameters ---
frame_count = 0
FPS = 60 # Frames per second for animation smoothness

# 1. Subtle breathing motion (vertical movement, mostly torso/chest)
BREATH_AMPLITUDE = 3 # pixels: maximum vertical displacement for breathing
BREATH_SPEED = 0.05 # radians per frame: controls the speed of the breathing cycle

# 2. Subtle restless movements (small, independent wiggles of limb ends/head)
RESTLESS_AMPLITUDE_HEAD = 2 # pixels: max displacement for head wiggles
RESTLESS_SPEED_HEAD = 0.08 # speed for head wiggles

RESTLESS_AMPLITUDE_LIMB = 1.5 # pixels: max displacement for wrist/ankle wiggles
RESTLESS_SPEED_LIMB = 0.06 # speed for limb wiggles

# 3. Very slow, long-period 'sad slump' or 'uncurl' movement
# This mimics a subtle, almost imperceptible shifting of body posture over a long time,
# fitting the "sadman lying down" context (e.g., adjusting for comfort or subtle restlessness).
SAD_SLUMP_AMPLITUDE_KNEE_Y = 5 # max pixel shift for knee Y position (making legs more bent/straight)
SAD_SLUMP_SPEED_KNEE = 0.005 # very slow speed for knee bend/straighten cycle

SAD_SLUMP_AMPLITUDE_ELBOW_X = 3 # max pixel shift for elbow X position (making arms splay/fold)
SAD_SLUMP_SPEED_ELBOW = 0.003 # very slow speed for arm splay/fold cycle


# --- Animation loop ---
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Calculate current positions based on initial pose and applying animation effects.
    # A fresh set of positions is created each frame to prevent accumulation of offsets and ensure periodic motion.
    current_positions = {name: [pos[0] * BODY_SCALE + BODY_OFFSET_X,
                                pos[1] * BODY_SCALE + BODY_OFFSET_Y]
                         for name, pos in initial_positions_normalized.items()}

    # --- Apply Animation Effects ---

    # 1. Breathing motion
    # Applies a vertical oscillation to the torso and connected upper body parts.
    breath_offset_y = BREATH_AMPLITUDE * math.sin(frame_count * BREATH_SPEED)
    current_positions["Spine_Mid"][1] += breath_offset_y
    current_positions["R_Shoulder"][1] += breath_offset_y * 0.8 # Shoulders move slightly less
    current_positions["L_Shoulder"][1] += breath_offset_y * 0.8
    current_positions["Neck"][1] += breath_offset_y * 0.5 # Neck moves even less
    current_positions["Head"][1] += breath_offset_y * 0.3 # Head moves least

    # 2. Subtle restless shifts
    # Small, localized oscillations to simulate minor fidgeting or adjustments.
    # Head subtle movement (x and y)
    current_positions["Head"][0] += RESTLESS_AMPLITUDE_HEAD * math.sin(frame_count * RESTLESS_SPEED_HEAD * 1.0 + 10) * 0.5
    current_positions["Head"][1] += RESTLESS_AMPLITUDE_HEAD * math.cos(frame_count * RESTLESS_SPEED_HEAD * 1.1 + 11) * 0.5
    current_positions["Neck"][0] += RESTLESS_AMPLITUDE_HEAD * math.sin(frame_count * RESTLESS_SPEED_HEAD * 1.0 + 10) * 0.1

    # Wrist subtle movement
    current_positions["R_Wrist"][0] += RESTLESS_AMPLITUDE_LIMB * math.sin(frame_count * RESTLESS_SPEED_LIMB * 1.2 + 20) * 0.8
    current_positions["R_Wrist"][1] += RESTLESS_AMPLITUDE_LIMB * math.cos(frame_count * RESTLESS_SPEED_LIMB * 1.3 + 21) * 0.8
    current_positions["L_Wrist"][0] += RESTLESS_AMPLITUDE_LIMB * math.sin(frame_count * RESTLESS_SPEED_LIMB * 1.1 + 22) * 0.8
    current_positions["L_Wrist"][1] += RESTLESS_AMPLITUDE_LIMB * math.cos(frame_count * RESTLESS_SPEED_LIMB * 1.0 + 23) * 0.8

    # Ankle subtle movement
    current_positions["R_Ankle"][0] += RESTLESS_AMPLITUDE_LIMB * math.sin(frame_count * RESTLESS_SPEED_LIMB * 0.9 + 30) * 0.6
    current_positions["R_Ankle"][1] += RESTLESS_AMPLITUDE_LIMB * math.cos(frame_count * RESTLESS_SPEED_LIMB * 0.8 + 31) * 0.6
    current_positions["L_Ankle"][0] += RESTLESS_AMPLITUDE_LIMB * math.sin(frame_count * RESTLESS_SPEED_LIMB * 0.7 + 32) * 0.6
    current_positions["L_Ankle"][1] += RESTLESS_AMPLITUDE_LIMB * math.cos(frame_count * RESTLESS_SPEED_LIMB * 0.6 + 33) * 0.6

    # 3. Very slow 'sad slump' or 'uncurl'
    # This creates a long, gradual transition in the posture, like slowly adjusting limbs.
    # The (1 + sin) / 2 formula ensures the movement cycles smoothly between 0 and 1.
    slump_factor_knee = (1 + math.sin(frame_count * SAD_SLUMP_SPEED_KNEE)) / 2
    # Adjust knees (and dependent ankles) to subtly bend/straighten
    current_positions["R_Knee"][1] += SAD_SLUMP_AMPLITUDE_KNEE_Y * slump_factor_knee
    current_positions["L_Knee"][1] += SAD_SLUMP_AMPLITUDE_KNEE_Y * slump_factor_knee
    current_positions["R_Ankle"][1] += SAD_SLUMP_AMPLITUDE_KNEE_Y * slump_factor_knee * 0.5
    current_positions["L_Ankle"][1] += SAD_SLUMP_AMPLITUDE_KNEE_Y * slump_factor_knee * 0.5

    slump_factor_elbow = (1 + math.sin(frame_count * SAD_SLUMP_SPEED_ELBOW)) / 2
    # Adjust elbows (and dependent wrists) to subtly splay/fold arms
    # Right elbow moves right on screen (away from spine); Left elbow moves left.
    current_positions["R_Elbow"][0] += SAD_SLUMP_AMPLITUDE_ELBOW_X * slump_factor_elbow
    current_positions["L_Elbow"][0] -= SAD_SLUMP_AMPLITUDE_ELBOW_X * slump_factor_elbow
    current_positions["R_Wrist"][0] += SAD_SLUMP_AMPLITUDE_ELBOW_X * slump_factor_elbow * 0.5
    current_positions["L_Wrist"][0] -= SAD_SLUMP_AMPLITUDE_ELBOW_X * slump_factor_elbow * 0.5

    # --- Draw points ---
    for name in JOINT_NAMES:
        x, y = current_positions[name]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap frame rate and increment frame count
    clock.tick(FPS)
    frame_count += 1

pygame.quit()
sys.exit()
