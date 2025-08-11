
import pygame
import numpy as np
import math

# --- Constants ---
WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 7
FPS = 60
ANIMATION_SECONDS = 5  # The duration of one full 360-degree turn
ANIMATION_FRAMES = ANIMATION_SECONDS * FPS

# --- 3D Model Definition ---
# The 15 joints represent a human figure. The coordinates are in a reference
# frame where Y is up, X is right, and Z is forward. The origin is on the
# ground, centered between the feet.
# Structure: 0:Head, 1:Neck, 2:LShoulder, 3:RShoulder, 4:LElbow, 5:RElbow,
# 6:LWrist, 7:RWrist, 8:Pelvis, 9:LHip, 10:RHip, 11:LKnee, 12:RKnee,
# 13:LAnkle, 14:RAnkle
JOINTS_REST_POSE = np.array([
    [0.0, 1.70, 0.0],  # 0: Head
    [0.0, 1.50, 0.0],  # 1: Neck (between shoulders)
    [-0.22, 1.50, 0.0],# 2: Left Shoulder
    [0.22, 1.50, 0.0], # 3: Right Shoulder
    [-0.22, 1.15, 0.0],# 4: Left Elbow
    [0.22, 1.15, 0.0], # 5: Right Elbow
    [-0.22, 0.85, 0.0],# 6: Left Wrist
    [0.22, 0.85, 0.0], # 7: Right Wrist
    [0.0, 0.92, 0.0],  # 8: Pelvis (between hips)
    [-0.17, 0.92, 0.0],# 9: Left Hip
    [0.17, 0.92, 0.0], # 10: Right Hip
    [-0.18, 0.48, 0.0],# 11: Left Knee
    [0.18, 0.48, 0.0], # 12: Right Knee
    [-0.20, 0.05, 0.0],# 13: Left Ankle
    [0.20, 0.05, 0.0]  # 14: Right Ankle
], dtype=float)

def project_3d_to_2d(points_3d):
    """Projects 3D points to 2D screen coordinates using perspective projection."""
    focal_length = 3.0
    camera_distance = 7.0
    scale = 350

    projected_points = []
    for p in points_3d:
        x, y, z = p
        # The z_proj acts as a divisor; larger z means the point is farther
        # away and appears smaller and closer to the center.
        z_proj = z + camera_distance
        if z_proj == 0: z_proj = 0.001 # Avoid division by zero

        px = (x * focal_length) / z_proj
        py = (y * focal_length) / z_proj
        
        # Translate to screen coordinates, inverting the Y-axis for Pygame.
        screen_x = int(WIDTH / 2 + px * scale)
        screen_y = int(HEIGHT / 2 - py * scale)
        projected_points.append((screen_x, screen_y))
    return projected_points

def main():
    """Initializes Pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Turning Around")
    clock = pygame.time.Clock()

    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Motion Calculation for the Current Frame ---
        
        # 1. Calculate normalized time 't' for one full cycle (0.0 to 1.0)
        t = (frame_count % ANIMATION_FRAMES) / ANIMATION_FRAMES
        
        # Start with a fresh copy of the rest pose for modification
        current_joints = JOINTS_REST_POSE.copy()

        # 2. Add secondary motions (bob, steps, swings) before the main rotation.
        # This makes the movements appear more natural and coordinated.

        # Body Bob: A subtle up-and-down motion of the whole body.
        bob_height = 0.025 * math.sin(t * 4 * math.pi)
        current_joints[:, 1] += bob_height

        # Leg Motion: A two-step turn. The right leg steps, then the left leg.
        step_phase = t * 2.0
        
        # Right leg step (first half of the turn, t = 0.0 to 0.5)
        if step_phase <= 1.0:
            lift = 0.08 * math.sin(step_phase * math.pi)
            bend = 0.15 * math.sin(step_phase * math.pi)
            current_joints[[12, 14], 1] += lift  # Lift R Knee and Ankle
            current_joints[12, 2] += bend        # Bend R Knee forward
        # Left leg step (second half of the turn, t = 0.5 to 1.0)
        else:
            phase_2 = step_phase - 1.0
            lift = 0.08 * math.sin(phase_2 * math.pi)
            bend = 0.15 * math.sin(phase_2 * math.pi)
            current_joints[[11, 13], 1] += lift  # Lift L Knee and Ankle
            current_joints[11, 2] += bend        # Bend L Knee forward

        # Arm Swing: Arms swing in opposition for balance.
        # The swing is a rotation around the shoulder's X-axis (left-right).
        arm_swing_angle = 0.5 * math.sin(t * 2 * math.pi + math.pi)
        
        # Left Arm (Elbow, Wrist)
        left_shoulder_pos = current_joints[2].copy()
        for i in [4, 6]:
            p = current_joints[i] - left_shoulder_pos
            c, s = math.cos(-arm_swing_angle), math.sin(-arm_swing_angle)
            y_new, z_new = p[1] * c - p[2] * s, p[1] * s + p[2] * c
            p[1], p[2] = y_new, z_new
            current_joints[i] = p + left_shoulder_pos
            
        # Right Arm (Elbow, Wrist)
        right_shoulder_pos = current_joints[3].copy()
        for i in [5, 7]:
            p = current_joints[i] - right_shoulder_pos
            c, s = math.cos(arm_swing_angle), math.sin(arm_swing_angle)
            y_new, z_new = p[1] * c - p[2] * s, p[1] * s + p[2] * c
            p[1], p[2] = y_new, z_new
            current_joints[i] = p + right_shoulder_pos

        # 3. Apply the main global rotation for the turn.
        # The entire figure rotates 360 degrees around the central Y-axis.
        main_angle = t * 2 * math.pi
        c, s = math.cos(main_angle), math.sin(main_angle)
        rotation_matrix_y = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        final_joints_3d = current_joints @ rotation_matrix_y.T

        # --- Drawing ---
        
        # Project the final 3D coordinates to 2D for display
        projected_points = project_3d_to_2d(final_joints_3d)

        # Draw the scene: black background and white points
        screen.fill(BACKGROUND_COLOR)
        for point in projected_points:
            pygame.draw.circle(screen, POINT_COLOR, point, POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()

if __name__ == '__main__':
    main()
