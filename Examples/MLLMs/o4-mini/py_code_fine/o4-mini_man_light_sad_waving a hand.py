
import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Waving - Point Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Mapping from normalized coordinates (x in [-1,1], y in [0,2]) to screen pixels
def to_screen(pos):
    x_norm, y_norm = pos
    # scale factors
    scale_x = 200
    scale_y = 200
    # center x
    x_pix = WIDTH  // 2 + int(x_norm * scale_x)
    # invert y-axis: y_norm = 0 -> near bottom; y_norm = 2 -> higher up
    y_pix = HEIGHT - 100 - int(y_norm * scale_y)
    return (x_pix, y_pix)

# Base (static) joint positions in normalized coords
# 15 points: head, neck, L_sho, R_sho, L_elb, R_elb, L_wri, R_wri, pelvis,
#             L_hip, R_hip, L_knee, R_knee, L_ank, R_ank
base_joints = [
    ( 0.00, 1.90),  # 0: head
    ( 0.00, 1.70),  # 1: neck
    (-0.30, 1.50),  # 2: left shoulder
    ( 0.30, 1.50),  # 3: right shoulder
    (-0.50, 1.10),  # 4: left elbow
    ( 0.30, 1.35),  # 5: right elbow  (raised for waving)
    (-0.70, 0.70),  # 6: left wrist
    ( 0.60, 1.35),  # 7: right wrist (will be animated)
    ( 0.00, 1.00),  # 8: pelvis
    (-0.20, 0.80),  # 9: left hip
    ( 0.20, 0.80),  #10: right hip
    (-0.20, 0.40),  #11: left knee
    ( 0.20, 0.40),  #12: right knee
    (-0.20, 0.00),  #13: left ankle
    ( 0.20, 0.00),  #14: right ankle
]

# Waving parameters
wave_radius = 0.30         # length of forearm in normalized units
wave_frequency = 1.0       # Hz
wave_amplitude = math.pi/4 # max angular deviation from horizontal (±45°)

def compute_wrist_position(elbow_pos, t):
    """
    Compute the animated position of the right wrist,
    oscillating horizontally like a wave.
    """
    ex, ey = elbow_pos
    angle = wave_amplitude * math.sin(2 * math.pi * wave_frequency * t)
    wx = ex + wave_radius * math.cos(angle)
    wy = ey + wave_radius * math.sin(angle)
    return (wx, wy)

def main():
    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        window.fill(BLACK)

        # Current time in seconds
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Build joint list for this frame
        joints = list(base_joints)  # copy static positions

        # Animate right wrist (index 7)
        elbow_pos = base_joints[5]
        joints[7] = compute_wrist_position(elbow_pos, t)

        # Draw the 15 point-lights
        for (x_norm, y_norm) in joints:
            x_pix, y_pix = to_screen((x_norm, y_norm))
            pygame.draw.circle(window, WHITE, (x_pix, y_pix), 8)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
