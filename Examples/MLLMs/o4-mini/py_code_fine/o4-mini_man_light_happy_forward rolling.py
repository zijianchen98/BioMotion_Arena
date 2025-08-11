
import sys
import math
import pygame

def main():
    # Initialize Pygame
    pygame.init()
    screen_width, screen_height = 600, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sad Heavy Woman Turning Around - Point-Light Display")
    clock = pygame.time.Clock()

    # Frame rate and animation settings
    fps = 60
    duration_seconds = 4
    total_frames = fps * duration_seconds

    # 3D joint definitions (x, y, z) in meters for a slumped/sad heavy woman
    # 15 markers: head top, neck, L/R shoulders, L/R elbows, L/R wrists,
    # mid-hip, L/R hips, L/R knees, L/R ankles
    joints3d = [
        (0.00, 1.70,  0.00),   # Head top
        (0.00, 1.50,  0.05),   # Neck (slightly forward)
        (-0.20, 1.50, 0.00),   # Left shoulder
        ( 0.20, 1.50, 0.00),   # Right shoulder
        (-0.40, 1.30, 0.00),   # Left elbow
        ( 0.40, 1.30, 0.00),   # Right elbow
        (-0.50, 1.10, 0.00),   # Left wrist
        ( 0.50, 1.10, 0.00),   # Right wrist
        ( 0.00, 1.00, 0.00),   # Mid-hip
        (-0.15, 1.00, 0.00),   # Left hip
        ( 0.15, 1.00, 0.00),   # Right hip
        (-0.15, 0.60, 0.00),   # Left knee
        ( 0.15, 0.60, 0.00),   # Right knee
        (-0.15, 0.10, 0.00),   # Left ankle
        ( 0.15, 0.10, 0.00),   # Right ankle
    ]

    # Scaling and screen-center for orthographic projection
    scale = 250  # pixels per meter
    center_x = screen_width // 2
    center_y = screen_height // 2

    frame = 0
    running = True
    while running:
        # Handle quit events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        # Clear screen to black
        screen.fill((0, 0, 0))

        # Compute rotation angle for this frame
        t = frame / total_frames
        angle = t * 2 * math.pi  # full 360° over duration
        cosA = math.cos(angle)
        sinA = math.sin(angle)

        # Draw each joint
        for x, y, z in joints3d:
            # Rotate around vertical axis (y)
            xr = x * cosA - z * sinA
            zr = x * sinA + z * cosA
            # Orthographic projection
            px = center_x + xr * scale
            py = center_y - y * scale
            pygame.draw.circle(screen, (255, 255, 255), (int(px), int(py)), 5)

        # Update display
        pygame.display.flip()

        # Advance frame
        frame = (frame + 1) % total_frames
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
