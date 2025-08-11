
import sys
import math
import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("15-Point Biological Motion - Running")

# Motion parameters
FPS = 60
f = 1.5  # cycling frequency in Hz
deg2rad = math.pi / 180.0

# Segment lengths (pixels)
torso_len = 120
thigh_len = 100
shin_len = 100
upper_arm_len = 60
lower_arm_len = 60
foot_len = 20

# Joint angle amplitudes
A_leg = 30 * deg2rad       # thigh swing amplitude
A_knee = 40 * deg2rad      # knee flex amplitude
A_arm = 30 * deg2rad       # upper arm swing amplitude
A_elbow = 40 * deg2rad     # elbow flex amplitude

# Bounce amplitude for pelvis vertical movement
bounce_amp = 15

# Point radius
pt_rad = 6

# Main loop
start_ticks = pygame.time.get_ticks()
running = True
while running:
    # Event handling
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
            running = False

    # Time since start in seconds
    t = (pygame.time.get_ticks() - start_ticks) / 1000.0
    phase = 2 * math.pi * f * t

    # Vertical bounce of pelvis
    bounce = bounce_amp * math.sin(4 * math.pi * f * t)

    # Pelvis (hip center)
    pelvis_x = WIDTH / 2
    pelvis_y = HEIGHT / 2 + bounce

    # Torso: neck position
    neck_x = pelvis_x
    neck_y = pelvis_y - torso_len

    # Head marker
    head_x = neck_x
    head_y = neck_y - 20

    # Shoulders
    shoulder_offset = 30
    ls_x, ls_y = neck_x - shoulder_offset, neck_y
    rs_x, rs_y = neck_x + shoulder_offset, neck_y

    # Hips (left & right)
    hip_offset = 20
    lh_x, lh_y = pelvis_x - hip_offset, pelvis_y
    rh_x, rh_y = pelvis_x + hip_offset, pelvis_y

    # ---- Arms ----
    # Upper-arm angles from vertical
    phi_arm_L = A_arm * math.sin(phase + math.pi)
    phi_arm_R = A_arm * math.sin(phase)

    # Elbow flex activation (only bend when sin(...)>0)
    bend_L = max(0.0, math.sin(phase + math.pi))
    bend_R = max(0.0, math.sin(phase))
    phi_elbow_L = A_elbow * bend_L
    phi_elbow_R = A_elbow * bend_R

    # Left elbow
    le_x = ls_x + upper_arm_len * math.sin(phi_arm_L)
    le_y = ls_y + upper_arm_len * math.cos(phi_arm_L)
    # Left wrist
    forearm_L = phi_arm_L + phi_elbow_L
    lw_x = le_x + lower_arm_len * math.sin(forearm_L)
    lw_y = le_y + lower_arm_len * math.cos(forearm_L)

    # Right elbow
    re_x = rs_x + upper_arm_len * math.sin(phi_arm_R)
    re_y = rs_y + upper_arm_len * math.cos(phi_arm_R)
    # Right wrist
    forearm_R = phi_arm_R + phi_elbow_R
    rw_x = re_x + lower_arm_len * math.sin(forearm_R)
    rw_y = re_y + lower_arm_len * math.cos(forearm_R)

    # ---- Legs ----
    # Thigh angles from vertical
    phi_thigh_L = A_leg * math.sin(phase)
    phi_thigh_R = A_leg * math.sin(phase + math.pi)

    # Knee flex activation
    kflex_L = max(0.0, math.sin(phase))
    kflex_R = max(0.0, math.sin(phase + math.pi))
    phi_knee_L = A_knee * kflex_L
    phi_knee_R = A_knee * kflex_R

    # Left knee
    lk_x = lh_x + thigh_len * math.sin(phi_thigh_L)
    lk_y = lh_y + thigh_len * math.cos(phi_thigh_L)
    # Left ankle
    shin_L = phi_thigh_L - phi_knee_L
    la_x = lk_x + shin_len * math.sin(shin_L)
    la_y = lk_y + shin_len * math.cos(shin_L)

    # Right knee
    rk_x = rh_x + thigh_len * math.sin(phi_thigh_R)
    rk_y = rh_y + thigh_len * math.cos(phi_thigh_R)
    # Right ankle
    shin_R = phi_thigh_R - phi_knee_R
    ra_x = rk_x + shin_len * math.sin(shin_R)
    ra_y = rk_y + shin_len * math.cos(shin_R)

    # Foot/toe markers (simple downward offset)
    lt_x, lt_y = la_x, la_y + foot_len
    rt_x, rt_y = ra_x, ra_y + foot_len

    # Collect all 15 points
    points = [
        (head_x, head_y),
        (ls_x, ls_y),
        (rs_x, rs_y),
        (le_x, le_y),
        (re_x, re_y),
        (lw_x, lw_y),
        (rw_x, rw_y),
        (lh_x, lh_y),
        (rh_x, rh_y),
        (lk_x, lk_y),
        (rk_x, rk_y),
        (la_x, la_y),
        (ra_x, ra_y),
        (lt_x, lt_y),
        (rt_x, rt_y),
    ]

    # Draw
    screen.fill((0, 0, 0))
    for (x, y) in points:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), pt_rad)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
