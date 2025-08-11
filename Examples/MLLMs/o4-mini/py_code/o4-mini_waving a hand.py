
import sys
import math
import pygame

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion: Waving Man")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Skeleton segment lengths (pixels)
TORSO_LEN     = 120
NECK_LEN      = 30
HEAD_LEN      = 30
SHOULDER_W    = 50
HIP_W         = 40
UPPER_ARM_LEN = 80
FOREARM_LEN   = 70
THIGH_LEN     = 100
SHIN_LEN      = 100

# Waving motion parameters
WAVE_FREQ         = 1.0      # 1 Hz
SHOULDER_AMP_DEG  = 10.0     # +/- 10° shoulder sway
FOREARM_AMP_DEG   = 60.0     # +/- 60° forearm swing

# Base angles (degrees)
RIGHT_SHOULDER_BASE_DEG = -30.0   # -30° from horizontal
RIGHT_FOREARM_BASE_DEG  = 90.0    # forearm initial relative to upper arm
LEFT_SHOULDER_DEG       = 210.0   # resting down-left
LEFT_FOREARM_REL_DEG    =   0.0   # forearm aligned with upper arm

# Convert degrees to radians
def deg2rad(deg):
    return deg * math.pi / 180.0

# Vector from angle and length
def vec_from(angle_rad, length):
    return (math.cos(angle_rad) * length, math.sin(angle_rad) * length)

# Main loop
def main():
    # Center of the skeleton's pelvis
    pelvis_x = screen_width // 2
    pelvis_y = screen_height // 2 + 50

    # Convert static angles to radians
    left_sh_base = deg2rad(LEFT_SHOULDER_DEG)
    left_fr_rel = deg2rad(LEFT_FOREARM_REL_DEG)
    right_sh_base = deg2rad(RIGHT_SHOULDER_BASE_DEG)
    right_fr_base  = deg2rad(RIGHT_FOREARM_BASE_DEG)
    shoulder_amp = deg2rad(SHOULDER_AMP_DEG)
    forearm_amp  = deg2rad(FOREARM_AMP_DEG)

    t = 0.0
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        t += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute current shoulder and forearm angles for right arm
        wave_phase = 2 * math.pi * WAVE_FREQ * t
        right_sh_angle = right_sh_base + shoulder_amp * math.sin(wave_phase)
        right_fr_rel_angle = right_fr_base + forearm_amp * math.sin(wave_phase)

        # Clear screen
        screen.fill(BLACK)

        # Build skeleton joint positions
        joints = []

        # 1) Pelvis
        pelvis = (pelvis_x, pelvis_y)
        joints.append(pelvis)

        # 2) Spine / Neck
        neck = (pelvis[0], pelvis[1] - TORSO_LEN)
        joints.append(neck)

        # 3) Head
        head = (neck[0], neck[1] - HEAD_LEN)
        joints.append(head)

        # Shoulders
        l_sh = (neck[0] - SHOULDER_W, neck[1])
        r_sh = (neck[0] + SHOULDER_W, neck[1])
        joints.append(l_sh)
        joints.append(r_sh)

        # Elbows
        # Left arm static
        l_el = (l_sh[0] + vec_from(left_sh_base, UPPER_ARM_LEN)[0],
                l_sh[1] + vec_from(left_sh_base, UPPER_ARM_LEN)[1])
        joints.append(l_el)

        # Right upper arm moves a bit with shoulder sway
        r_el = (r_sh[0] + vec_from(right_sh_angle, UPPER_ARM_LEN)[0],
                r_sh[1] + vec_from(right_sh_angle, UPPER_ARM_LEN)[1])
        joints.append(r_el)

        # Wrists
        # Left forearm static
        l_wr = (l_el[0] + vec_from(left_sh_base + left_fr_rel, FOREARM_LEN)[0],
                l_el[1] + vec_from(left_sh_base + left_fr_rel, FOREARM_LEN)[1])
        joints.append(l_wr)

        # Right forearm waving
        r_wr = (r_el[0] + vec_from(right_sh_angle + right_fr_rel_angle, FOREARM_LEN)[0],
                r_el[1] + vec_from(right_sh_angle + right_fr_rel_angle, FOREARM_LEN)[1])
        joints.append(r_wr)

        # Hips
        l_hip = (pelvis[0] - HIP_W, pelvis[1])
        r_hip = (pelvis[0] + HIP_W, pelvis[1])
        joints.append(l_hip)
        joints.append(r_hip)

        # Knees
        down = deg2rad(90.0)
        l_kn = (l_hip[0] + vec_from(down, THIGH_LEN)[0],
                l_hip[1] + vec_from(down, THIGH_LEN)[1])
        r_kn = (r_hip[0] + vec_from(down, THIGH_LEN)[0],
                r_hip[1] + vec_from(down, THIGH_LEN)[1])
        joints.append(l_kn)
        joints.append(r_kn)

        # Ankles
        l_an = (l_kn[0] + vec_from(down, SHIN_LEN)[0],
                l_kn[1] + vec_from(down, SHIN_LEN)[1])
        r_an = (r_kn[0] + vec_from(down, SHIN_LEN)[0],
                r_kn[1] + vec_from(down, SHIN_LEN)[1])
        joints.append(l_an)
        joints.append(r_an)

        # Draw the 15 point-lights
        for (x, y) in joints:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
