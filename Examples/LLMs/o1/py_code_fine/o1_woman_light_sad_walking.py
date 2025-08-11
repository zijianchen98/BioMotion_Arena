import pygame
import math

# --------------------------
# Point-light biological motion: Sad woman (light weight) walking
# --------------------------
# This program uses Pygame to present 15 white point-lights against a black background.
# The motion is a simplistic approximation of a sad woman walking with minimal amplitude
# (light weight). Although simplified, it demonstrates a plausible biomechanical pattern
# of a basic walking cycle with "sad" posture.

# Number of joints
NUM_JOINTS = 15

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Walking cycle length (in seconds)
CYCLE_DURATION = 2.0

# Frames per second
FPS = 60

# Radius of the point-lights
RADIUS = 4

def get_sad_woman_walking_positions(t):
    """
    Return a list of (x, y) positions for the 15 joints at time t (seconds).
    The parameter t is mapped into the walking cycle [0, CYCLE_DURATION).
    A 'sad' posture is approximated by slightly lowered head,
    minimal arm swing, and a smaller step amplitude.
    """
    # Phase within one full cycle of walking: 0 .. 2*pi
    phase = (t % CYCLE_DURATION) / CYCLE_DURATION * 2.0 * math.pi

    # Base position (center of screen)
    base_x = WIDTH // 2
    base_y = HEIGHT // 2

    # Some basic body measurements and offsets (purely illustrative)
    torso_len = 50
    head_offset = 15
    shoulder_width = 30
    arm_len_upper = 25
    arm_len_lower = 25
    hip_width = 25
    leg_len_upper = 35
    leg_len_lower = 35

    # "Sad" posture: slight bend forward
    # We'll simulate a stoop by offsetting the torso
    sad_stoop = 10  # how much the torso is shifted forward at the top

    # Walking amplitude adjustments for "light weight" + "sad"
    step_amplitude = 15  # forward/back foot translation
    arm_swing_amplitude = 5

    # Leg phase difference: when left foot is forward, right foot is back
    # We'll use a standard ~pi offset for typical walking gait
    leg_phase_offset = math.pi

    # Arm phase difference: arms move out of phase with legs in normal walking
    # reducing amplitude for "sad" style
    arm_phase_offset = math.pi

    # Vertical displacement of the pelvis (very slight for a sad and light walk)
    pelvis_vertical_disp = 3

    # Compute vertical bobbing offset
    pelvis_y_offset = pelvis_vertical_disp * math.sin(2 * phase)

    # Pelvis (waist) - somewhat central
    pelvis_pos = (base_x, base_y + pelvis_y_offset)

    # Torso top (neck) - stooped slightly forward
    neck_x = pelvis_pos[0] - sad_stoop
    neck_y = pelvis_pos[1] - torso_len
    neck_pos = (neck_x, neck_y)

    # Head - a bit above the neck, slightly forward (sad posture)
    head_pos = (neck_x - 5, neck_y - head_offset)

    # Shoulders
    left_shoulder_x = neck_x - shoulder_width / 2
    right_shoulder_x = neck_x + shoulder_width / 2
    shoulders_y = neck_y
    left_shoulder_pos = (left_shoulder_x, shoulders_y)
    right_shoulder_pos = (right_shoulder_x, shoulders_y)

    # Arms (upper + lower)
    # We'll create a small swing based on (phase + arm_phase_offset)
    # but reduced amplitude for sadness
    left_arm_angle = math.sin(phase + arm_phase_offset) * 0.2  # small angle
    right_arm_angle = math.sin(phase) * 0.2

    # Elbows
    left_elbow_x = left_shoulder_x + arm_len_upper * math.sin(left_arm_angle)
    left_elbow_y = shoulders_y + arm_len_upper * math.cos(left_arm_angle)
    right_elbow_x = right_shoulder_x + arm_len_upper * math.sin(right_arm_angle)
    right_elbow_y = shoulders_y + arm_len_upper * math.cos(right_arm_angle)
    left_elbow_pos = (left_elbow_x, left_elbow_y)
    right_elbow_pos = (right_elbow_x, right_elbow_y)

    # Wrists
    # Another small angle for the forearms to swing inward/outward
    # We'll reuse the same angle for simplicity, applying a slight offset
    forearm_offset = 0.3
    left_wrist_x = left_elbow_x + arm_len_lower * math.sin(left_arm_angle + forearm_offset)
    left_wrist_y = left_elbow_y + arm_len_lower * math.cos(left_arm_angle + forearm_offset)
    right_wrist_x = right_elbow_x + arm_len_lower * math.sin(right_arm_angle + forearm_offset)
    right_wrist_y = right_elbow_y + arm_len_lower * math.cos(right_arm_angle + forearm_offset)
    left_wrist_pos = (left_wrist_x, left_wrist_y)
    right_wrist_pos = (right_wrist_x, right_wrist_y)

    # Hips
    left_hip_x = pelvis_pos[0] - hip_width / 2
    right_hip_x = pelvis_pos[0] + hip_width / 2
    hips_y = pelvis_pos[1]
    left_hip_pos = (left_hip_x, hips_y)
    right_hip_pos = (right_hip_x, hips_y)

    # Walking motion for legs
    # We'll have the foot swing forward/back around pelvis with small amplitude
    left_leg_angle = math.sin(phase) * 0.4  # main motion
    right_leg_angle = math.sin(phase + leg_phase_offset) * 0.4

    # Knees
    left_knee_x = left_hip_x + leg_len_upper * math.sin(left_leg_angle)
    left_knee_y = hips_y + leg_len_upper * math.cos(left_leg_angle)
    right_knee_x = right_hip_x + leg_len_upper * math.sin(right_leg_angle)
    right_knee_y = hips_y + leg_len_upper * math.cos(right_leg_angle)
    left_knee_pos = (left_knee_x, left_knee_y)
    right_knee_pos = (right_knee_x, right_knee_y)

    # Ankles/Feet
    # We'll add additional forward/back displacement to simulate step amplitude
    left_foot_forward = step_amplitude * math.sin(phase)
    right_foot_forward = step_amplitude * math.sin(phase + leg_phase_offset)

    left_ankle_x = left_knee_x + leg_len_lower * math.sin(left_leg_angle) + left_foot_forward
    left_ankle_y = left_knee_y + leg_len_lower * math.cos(left_leg_angle)
    right_ankle_x = right_knee_x + leg_len_lower * math.sin(right_leg_angle) + right_foot_forward
    right_ankle_y = right_knee_y + leg_len_lower * math.cos(right_leg_angle)
    left_ankle_pos = (left_ankle_x, left_ankle_y)
    right_ankle_pos = (right_ankle_x, right_ankle_y)

    # Collect all 15 joints in an ordered list
    joints = [
        head_pos,
        neck_pos,
        left_shoulder_pos,
        left_elbow_pos,
        left_wrist_pos,
        right_shoulder_pos,
        right_elbow_pos,
        right_wrist_pos,
        pelvis_pos,
        left_hip_pos,
        left_knee_pos,
        left_ankle_pos,
        right_hip_pos,
        right_knee_pos,
        right_ankle_pos
    ]

    return joints

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sad Woman (Light Weight) Walking - Point-Light Display")
    clock = pygame.time.Clock()

    running = True
    start_ticks = pygame.time.get_ticks()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate time in seconds since start
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        elapsed_sec = elapsed_ms / 1000.0

        # Get joint positions at current time
        joints = get_sad_woman_walking_positions(elapsed_sec)

        # Draw
        screen.fill((0, 0, 0))  # black background
        for (x, y) in joints:
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()