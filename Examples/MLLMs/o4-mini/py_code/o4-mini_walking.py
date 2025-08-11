
import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Walker")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Screen center
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Scale between model units and pixels
SCALE = 200.0

# Walking parameters
FREQ = 1.0                        # steps per second
OMEGA = 2 * math.pi * FREQ       # angular speed
LEG_AMP = math.radians(30)        # max leg swing
LEG_LENGTH = 1.0                  # thigh+shank
FOOT_HEIGHT_AMP = 0.2             # foot clearance
KNEE_OFF_AMP = 0.1                # knee bulge

# Arm parameters
ARM_AMP = math.radians(20)
ARM_LENGTH = 0.7
ARM_LIFT_AMP = 0.1
ELBOW_OFF_AMP = 0.05

# Body segment lengths and widths
SPINE_LEN = 0.5
SHOULDER_W = 0.4
HIP_W = 0.3
NECK_LEN = 0.2
HEAD_LEN = 0.2

# Pelvis vertical oscillation
PELVIS_OSC_AMP = 0.05

def to_screen(pt):
    """Convert model (x,y) to screen coordinates."""
    x, y = pt
    sx = CENTER_X + x * SCALE
    sy = CENTER_Y - y * SCALE
    return int(sx), int(sy)

def run():
    t = 0.0
    running = True
    while running:
        # Handle events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))

        # Phase
        phi = OMEGA * t

        # Pelvis position
        pelvis_x = 0.0
        pelvis_y = PELVIS_OSC_AMP * math.sin(2 * phi)

        # Shoulder and neck and head
        shoulder_center = (pelvis_x, pelvis_y + SPINE_LEN)
        neck = (shoulder_center[0], shoulder_center[1] + NECK_LEN)
        head = (neck[0], neck[1] + HEAD_LEN)

        # Shoulder markers
        left_sh = (shoulder_center[0] - SHOULDER_W/2, shoulder_center[1])
        right_sh = (shoulder_center[0] + SHOULDER_W/2, shoulder_center[1])

        # Pelvis and hips
        pelvis = (pelvis_x, pelvis_y)
        left_hip = (pelvis_x - HIP_W/2, pelvis_y)
        right_hip = (pelvis_x + HIP_W/2, pelvis_y)

        # LEG POSITIONS
        # Leg swing angles
        left_theta = LEG_AMP * math.sin(phi)
        right_theta = LEG_AMP * math.sin(phi + math.pi)
        # Foot clearance
        left_clear = max(0.0, math.sin(phi))
        right_clear = max(0.0, math.sin(phi + math.pi))

        # Ankle marker positions
        def ankle_pos(hip, theta, clear):
            ax = hip[0] + LEG_LENGTH * math.sin(theta)
            ay = hip[1] - LEG_LENGTH * math.cos(theta) + FOOT_HEIGHT_AMP * clear
            return (ax, ay)

        left_an = ankle_pos(left_hip, left_theta, left_clear)
        right_an = ankle_pos(right_hip, right_theta, right_clear)

        # Knee markers as midpoint plus perpendicular bulge
        def knee_pos(hip, ank, clear):
            mx = 0.5 * (hip[0] + ank[0])
            my = 0.5 * (hip[1] + ank[1])
            vx = ank[0] - hip[0]
            vy = ank[1] - hip[1]
            # perpendicular
            norm = math.hypot(vx, vy)
            if norm > 1e-6:
                px = -vy / norm
                py = vx / norm
            else:
                px, py = 0.0, 0.0
            off = KNEE_OFF_AMP * clear
            return (mx + px * off, my + py * off)

        left_kn = knee_pos(left_hip, left_an, left_clear)
        right_kn = knee_pos(right_hip, right_an, right_clear)

        # ARM POSITIONS
        # Swing opposite to legs
        left_arm_phase = phi + math.pi
        right_arm_phase = phi

        left_alpha = ARM_AMP * math.sin(left_arm_phase)
        right_alpha = ARM_AMP * math.sin(right_arm_phase)
        left_lift = max(0.0, math.sin(left_arm_phase))
        right_lift = max(0.0, math.sin(right_arm_phase))

        def wrist_pos(sh, alpha, lift):
            wx = sh[0] + ARM_LENGTH * math.sin(alpha)
            wy = sh[1] - ARM_LENGTH * math.cos(alpha) + ARM_LIFT_AMP * lift
            return (wx, wy)

        left_wr = wrist_pos(left_sh, left_alpha, left_lift)
        right_wr = wrist_pos(right_sh, right_alpha, right_lift)

        def elbow_pos(sh, wr, lift):
            mx = 0.5 * (sh[0] + wr[0])
            my = 0.5 * (sh[1] + wr[1])
            vx = wr[0] - sh[0]
            vy = wr[1] - sh[1]
            norm = math.hypot(vx, vy)
            if norm > 1e-6:
                px = -vy / norm
                py = vx / norm
            else:
                px, py = 0.0, 0.0
            off = ELBOW_OFF_AMP * lift
            return (mx + px * off, my + py * off)

        left_el = elbow_pos(left_sh, left_wr, left_lift)
        right_el = elbow_pos(right_sh, right_wr, right_lift)

        # Collect all 15 markers
        markers = [
            head,
            neck,
            left_sh, right_sh,
            left_el, right_el,
            left_wr, right_wr,
            pelvis,
            left_hip, right_hip,
            left_kn, right_kn,
            left_an, right_an
        ]

        # Draw markers
        for pt in markers:
            sx, sy = to_screen(pt)
            pygame.draw.circle(screen, (255, 255, 255), (sx, sy), 5)

        # Update display
        pygame.display.flip()

        # Tick
        clock.tick(FPS)
        t += 1.0 / FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run()
