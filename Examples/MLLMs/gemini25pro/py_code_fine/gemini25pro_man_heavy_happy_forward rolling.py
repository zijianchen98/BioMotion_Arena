
import pygame
import numpy as np

def generate_motion_data():
    """
    Generates the point-light motion data for a happyman with heavy weight
    performing a forward roll.

    The motion is defined by a series of keyframes, which are then interpolated
    using a Catmull-Rom spline for smooth, natural movement.

    The 15 points are ordered as follows for kinematic sense:
    0: Head, 1: Neck, 2: Pelvis, 3: L_Shoulder, 4: R_Shoulder,
    5: L_Elbow, 6: R_Elbow, 7: L_Wrist, 8: R_Wrist, 9: L_Hip, 10: R_Hip,
    11: L_Knee, 12: R_Knee, 13: L_Ankle, 14: R_Ankle.

    Returns:
        A list of frames. Each frame is a list of 15 (x, y) tuples
        representing the coordinates of the point-lights.
    """

    # --- Keyframe Definitions ---
    # Each keyframe has a time (t), a set of relative joint positions (points),
    # and a central position on the screen (pos).
    # The 'points' define the body's posture, centered around a local origin.
    # The 'pos' defines where the center of that posture is on the screen.
    # The coordinate system for points has Y increasing upwards.
    # The coordinate system for pos matches the screen (Y increasing downwards).
    # The final conversion handles this transformation.

    keyframes = []
    scale = 1.3  # Scale of the figure
    
    # Keyframe 1: (t=0.0) Initial crouch on the left
    # Posture: Deep crouch, arms bent holding a "weight"
    kf1_points = [np.array(p) for p in [
        [-5, 95],    # 0 Head
        [0, 75],     # 1 Neck
        [0, 0],      # 2 Pelvis
        [-20, 70],   # 3 L_Shoulder
        [20, 70],    # 4 R_Shoulder
        [0, 50],     # 5 L_Elbow (bent, holding weight)
        [40, 50],    # 6 R_Elbow
        [-5, 25],    # 7 L_Wrist (near pelvis)
        [35, 25],    # 8 R_Wrist
        [-15, 0],    # 9 L_Hip
        [15, 0],     # 10 R_Hip
        [15, -50],   # 11 L_Knee
        [45, -50],   # 12 R_Knee
        [5, -90],    # 13 L_Ankle
        [35, -90],   # 14 R_Ankle
    ]]
    keyframes.append({'t': 0.0, 'points': kf1_points, 'pos': np.array([150, 480])})

    # Keyframe 2: (t=0.25) Tucking and leaning forward
    # Posture: Body rotates forward, head tucks, legs prepare to push
    kf2_points = [np.array(p) for p in [
        [40, 60],    # 0 Head (tucked)
        [30, 40],    # 1 Neck
        [0, 0],      # 2 Pelvis
        [25, 50],    # 3 L_Shoulder
        [55, 40],    # 4 R_Shoulder
        [45, 15],    # 5 L_Elbow
        [75, 5],     # 6 R_Elbow
        [30, 0],     # 7 L_Wrist
        [60, -10],   # 8 R_Wrist
        [-10, 10],   # 9 L_Hip
        [10, -10],   # 10 R_Hip
        [-30, -40],  # 11 L_Knee
        [-10, -60],  # 12 R_Knee
        [-60, -60],  # 13 L_Ankle
        [-40, -80],  # 14 R_Ankle
    ]]
    keyframes.append({'t': 0.25, 'points': kf2_points, 'pos': np.array([250, 450])})

    # Keyframe 3: (t=0.5) Mid-roll, upside down on back/shoulders
    # Posture: Tightly tucked ball, rotated
    kf3_points = [np.array(p) for p in [
        [60, -30],    # 0 Head
        [50, 0],      # 1 Neck
        [0, 0],       # 2 Pelvis
        [45, 15],     # 3 L_Shoulder
        [65, 15],     # 4 R_Shoulder
        [25, 20],     # 5 L_Elbow
        [45, 20],     # 6 R_Elbow
        [10, 10],     # 7 L_Wrist
        [30, 10],     # 8 R_Wrist
        [-5, -15],    # 9 L_Hip
        [-5, 15],     # 10 R_Hip
        [-40, -25],   # 11 L_Knee
        [-40, 25],    # 12 R_Knee
        [-60, -15],   # 13 L_Ankle
        [-60, 35],    # 14 R_Ankle
    ]]
    keyframes.append({'t': 0.5, 'points': kf3_points, 'pos': np.array([400, 350])})

    # Keyframe 4: (t=0.75) Finishing roll, sitting up, feet landing
    # Posture: Untucking, torso coming up
    kf4_points = [np.array(p) for p in [
        [-20, 95],   # 0 Head
        [-10, 75],   # 1 Neck
        [0, 0],      # 2 Pelvis
        [-30, 70],   # 3 L_Shoulder
        [10, 70],    # 4 R_Shoulder
        [-10, 50],   # 5 L_Elbow
        [30, 50],    # 6 R_Elbow
        [-15, 25],   # 7 L_Wrist
        [25, 25],    # 8 R_Wrist
        [-15, 0],    # 9 L_Hip
        [15, 0],     # 10 R_Hip
        [-50, -40],  # 11 L_Knee
        [-20, -40],  # 12 R_Knee
        [-80, -80],  # 13 L_Ankle
        [-50, -80],  # 14 R_Ankle
    ]]
    keyframes.append({'t': 0.75, 'points': kf4_points, 'pos': np.array([550, 480])})

    # Keyframe 5: (t=1.0) Final crouch on the right
    # Posture: Same as start, allows for a smooth loop
    keyframes.append({'t': 1.0, 'points': kf1_points, 'pos': np.array([650, 480])})

    # --- Interpolation ---
    def catmull_rom_spline(P0, P1, P2, P3, t):
        """ Interpolates between P1 and P2 using a Catmull-Rom spline. """
        return 0.5 * ((2 * P1) +
                      (-P0 + P2) * t +
                      (2 * P0 - 5 * P1 + 4 * P2 - P3) * t**2 +
                      (-P0 + 3 * P1 - 3 * P2 + P3) * t**3)

    motion_data = []
    num_total_frames = 180  # Total frames for the entire animation loop

    # Pad keyframes to handle endpoints of the spline
    padded_keyframes = [keyframes[0]] + keyframes + [keyframes[-1]]

    for i in range(1, len(padded_keyframes) - 2):
        p0_data, p1_data, p2_data, p3_data = padded_keyframes[i-1:i+3]

        t_start, t_end = p1_data['t'], p2_data['t']
        num_segment_frames = int((t_end - t_start) * num_total_frames)

        P0_pos, P1_pos, P2_pos, P3_pos = (d['pos'] for d in (p0_data, p1_data, p2_data, p3_data))
        P0_pts, P1_pts, P2_pts, P3_pts = (np.array(d['points']) for d in (p0_data, p1_data, p2_data, p3_data))

        for j in range(num_segment_frames):
            if num_segment_frames == 0: continue
            t = j / num_segment_frames

            current_pos = catmull_rom_spline(P0_pos, P1_pos, P2_pos, P3_pos, t)
            current_points_relative = catmull_rom_spline(P0_pts, P1_pts, P2_pts, P3_pts, t)

            frame_points = []
            for p in current_points_relative:
                # Combine relative point with central position, scale, and flip Y-axis
                x = current_pos[0] + p[0] * scale
                y = current_pos[1] - p[1] * scale # Y is flipped for screen coordinates
                frame_points.append((x, y))

            motion_data.append(frame_points)

    return motion_data


def main():
    """
    Main function to initialize Pygame and run the animation loop.
    """
    pygame.init()

    # Screen and animation settings
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    BG_COLOR = (0, 0, 0)
    DOT_COLOR = (255, 255, 255)
    DOT_RADIUS = 6

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Forward Roll")
    clock = pygame.time.Clock()

    # Generate the motion data
    motion_frames = generate_motion_data()
    if not motion_frames:
        print("Error: Motion data could not be generated.")
        return
        
    num_frames = len(motion_frames)
    current_frame_index = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill(BG_COLOR)

        # Get current frame's points
        points_to_draw = motion_frames[current_frame_index]

        # Draw the points
        for point in points_to_draw:
            pygame.draw.circle(screen, DOT_COLOR, (int(point[0]), int(point[1])), DOT_RADIUS)

        # Update the display
        pygame.display.flip()

        # Advance to the next frame
        current_frame_index = (current_frame_index + 1) % num_frames

        # Control the frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
