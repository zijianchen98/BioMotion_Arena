
import pygame
import numpy as np

def main():
    """
    Main function to set up and run the biological motion animation.
    """
    # --- Pygame and Display Setup ---
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 30
    POINT_RADIUS = 5
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Jumping Forward with Heavy Weight")
    clock = pygame.time.Clock()

    # --- Keyframe Animation Data ---
    # The animation portrays a sad, heavy jump. This is reflected in:
    # - A slumped starting and ending posture (head down, shoulders rounded).
    # - A deep, slow crouch to gather energy, as if burdened.
    # - A low jump trajectory (low apex).
    # - A heavy landing with deep flexion to absorb the impact.
    # - A slow recovery to the final standing position.
    
    start_x = 150
    end_x = 650
    floor_y = 550

    # Each pose is a NumPy array of 15 (x, y) coordinates for the joints.
    # The order of joints is consistent across all poses.
    # 0:Head, 1:Sternum, 2:Pelvis, 3:L_Shoulder, 4:R_Shoulder, 5:L_Elbow, 6:R_Elbow,
    # 7:L_Wrist, 8:R_Wrist, 9:L_Hip, 10:R_Hip, 11:L_Knee, 12:R_Knee, 13:L_Ankle, 14:R_Ankle

    # Pose 0: Initial slumped stance
    p0 = np.array([
        [start_x + 5, 290], [start_x, 340], [start_x, 430], [start_x - 25, 335],
        [start_x + 25, 335], [start_x - 35, 380], [start_x + 35, 380], [start_x - 40, 430],
        [start_x + 40, 430], [start_x - 15, 430], [start_x + 15, 430], [start_x - 15, 490],
        [start_x + 15, 490], [start_x - 15, floor_y], [start_x + 15, floor_y]
    ])

    # Pose 1: Deep crouch, arms swing back
    cx = start_x + 30
    p1 = np.array([
        [cx + 20, 360], [cx + 10, 400], [cx, 500], [cx - 20, 395],
        [cx + 30, 395], [cx - 40, 410], [cx + 10, 410], [cx - 50, 420],
        [cx, 420], [cx - 15, 500], [cx + 15, 500], [cx - 20, 520],
        [cx + 20, 520], [cx - 25, floor_y], [cx + 25, floor_y]
    ])

    # Pose 2: Takeoff, extension
    tx = start_x + 120
    p2 = np.array([
        [tx + 25, 260], [tx + 20, 310], [tx, 400], [tx - 25, 305],
        [tx + 25, 305], [tx, 350], [tx + 40, 350], [tx + 5, 390],
        [tx + 45, 390], [tx - 15, 400], [tx + 15, 400], [tx - 10, 475],
        [tx + 10, 475], [start_x + 40, floor_y], [start_x + 70, floor_y]
    ])

    # Pose 3: Apex of the jump (low trajectory)
    ax = 400
    p3 = np.array([
        [ax + 5, 260], [ax, 310], [ax, 400], [ax - 25, 305],
        [ax + 25, 305], [ax - 5, 360], [ax + 45, 360], [ax, 400],
        [ax + 50, 400], [ax - 15, 400], [ax + 15, 400], [ax - 10, 460],
        [ax + 20, 460], [ax - 5, 520], [ax + 25, 520]
    ])

    # Pose 4: Landing and impact absorption
    ix = end_x
    p4 = np.array([
        [ix + 20, 360], [ix + 10, 400], [ix, 500], [ix - 20, 395],
        [ix + 30, 395], [ix - 40, 430], [ix + 50, 430], [ix - 50, 450],
        [ix + 60, 450], [ix - 15, 500], [ix + 15, 500], [ix - 20, 520],
        [ix + 20, 520], [ix - 25, floor_y], [ix + 25, floor_y]
    ])

    # Pose 5: Final slumped stance
    p5 = np.array([
        [end_x + 5, 290], [end_x, 340], [end_x, 430], [end_x - 25, 335],
        [end_x + 25, 335], [end_x - 35, 380], [end_x + 35, 380], [end_x - 40, 430],
        [end_x + 40, 430], [end_x - 15, 430], [end_x + 15, 430], [end_x - 15, 490],
        [end_x + 15, 490], [end_x - 15, floor_y], [end_x + 15, floor_y]
    ])

    key_poses = [p0, p0, p1, p2, p3, p4, p5, p5]
    # Number of frames between each key pose
    durations = [15, 25, 10, 20, 15, 30, 20]

    # --- Frame Generation ---
    def interpolate(p1, p2, steps):
        """Linearly interpolates between two poses (p1 and p2) over a number of steps."""
        frames = []
        if steps == 0:
            return frames
        for i in range(steps):
            t = (i + 1) / steps
            # Use ease-in-out for smoother, more natural acceleration and deceleration
            t_eased = t * t * (3.0 - 2.0 * t)
            current_frame = p1 * (1 - t_eased) + p2 * t_eased
            frames.append(current_frame)
        return frames

    all_frames = []
    for i in range(len(key_poses) - 1):
        p1 = key_poses[i]
        p2 = key_poses[i+1]
        steps = durations[i]
        all_frames.extend(interpolate(p1, p2, steps))
    
    num_frames = len(all_frames)
    frame_index = 0

    # --- Main Animation Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Drawing ---
        screen.fill(BLACK)
        
        current_pose = all_frames[frame_index]
        for point in current_pose:
            # Cast coordinates to int for drawing
            pos = (int(point[0]), int(point[1]))
            pygame.draw.circle(screen, WHITE, pos, POINT_RADIUS)

        # --- Update Display ---
        pygame.display.flip()
        
        # --- Advance to Next Frame ---
        frame_index = (frame_index + 1) % num_frames
        
        # --- Control Frame Rate ---
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
