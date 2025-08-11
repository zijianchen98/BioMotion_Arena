
import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point‐Light Biological Motion: Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for frame rate
CLOCK = pygame.time.Clock()
FPS = 60

# Body segment lengths (in pixels)
TRUNK_HEIGHT   = 80
NECK_LENGTH    = 20
HIP_WIDTH      = 20
SHOULDER_WIDTH = 30
THIGH_LEN      = 60
SHIN_LEN       = 60
UPPERARM_LEN   = 40
FOREARM_LEN    = 40
FOOT_LEN       = 15

# Motion parameters
RUN_PERIOD     = 1.2                # seconds per full run cycle
VERT_BOB_AMP   = 10                 # vertical bob amplitude
THIGH_AMP      = 0.6                # radians (≈35°)
SHIN_AMP       = 0.5                # radians
ARM_AMP        = 0.7                # radians
FOREARM_AMP    = 0.5                # radians

def get_joint_positions(t):
    """
    Compute 15 joint positions for a single running frame at time t.
    Returns a list of (x, y) tuples.
    """
    # Phase of the running cycle [0..2π)
    phi = (2 * math.pi * (t % RUN_PERIOD)) / RUN_PERIOD

    # Vertical "bob" of the hips for bounce
    bob = VERT_BOB_AMP * math.sin(2 * phi)

    # Hip center
    hip_cx = WIDTH  / 2
    hip_cy = HEIGHT / 2 + bob
    hip_center = (hip_cx, hip_cy)

    # Trunk top (shoulder center)
    shoulder_cx = hip_cx
    shoulder_cy = hip_cy - TRUNK_HEIGHT

    # Head marker
    head_x = shoulder_cx
    head_y = shoulder_cy - NECK_LENGTH
    head = (head_x, head_y)

    # Left and right shoulders
    left_sh  = (shoulder_cx - SHOULDER_WIDTH, shoulder_cy)
    right_sh = (shoulder_cx + SHOULDER_WIDTH, shoulder_cy)

    # Left and right hips
    left_hp  = (hip_cx - HIP_WIDTH, hip_cy)
    right_hp = (hip_cx + HIP_WIDTH, hip_cy)

    # Leg angles relative to vertical down
    thigh_ang_L =  THIGH_AMP * math.sin(phi)
    thigh_ang_R =  THIGH_AMP * math.sin(phi + math.pi)
    shin_ang_L  =  SHIN_AMP  * math.sin(phi + math.pi/2)
    shin_ang_R  =  SHIN_AMP  * math.sin(phi + math.pi + math.pi/2)

    # Knee positions
    def compute_limb_rooted(origin, angle, length):
        """
        Given origin, absolute angle from vertical down, and length,
        returns the end point.
        """
        vx = math.sin(angle)
        vy = math.cos(angle)
        return (origin[0] + length * vx,
                origin[1] + length * vy)

    left_knee  = compute_limb_rooted(left_hp,  thigh_ang_L, THIGH_LEN)
    right_knee = compute_limb_rooted(right_hp, thigh_ang_R, THIGH_LEN)

    # Ankle positions
    left_ankle  = compute_limb_rooted(left_knee,  shin_ang_L, SHIN_LEN)
    right_ankle = compute_limb_rooted(right_knee, shin_ang_R, SHIN_LEN)

    # Toe (foot) markers -- extending same direction as shin
    left_toe  = compute_limb_rooted(left_ankle,  shin_ang_L, FOOT_LEN)
    right_toe = compute_limb_rooted(right_ankle, shin_ang_R, FOOT_LEN)

    # Arm angles relative to vertical up (y axis negative)
    # vertical up vector is (0, -1), so end = origin + length*(sin(a), -cos(a))
    def compute_arm_rooted(origin, angle, length):
        vx = math.sin(angle)
        vy = -math.cos(angle)
        return (origin[0] + length * vx,
                origin[1] + length * vy)

    upperarm_ang_L  =  ARM_AMP     * math.sin(phi + math.pi)
    upperarm_ang_R  =  ARM_AMP     * math.sin(phi)
    forearm_ang_L   =  FOREARM_AMP * math.sin(phi + math.pi + math.pi/2)
    forearm_ang_R   =  FOREARM_AMP * math.sin(phi + math.pi/2)

    # Elbows
    left_elbow  = compute_arm_rooted(left_sh,  upperarm_ang_L, UPPERARM_LEN)
    right_elbow = compute_arm_rooted(right_sh, upperarm_ang_R, UPPERARM_LEN)

    # Wrists
    left_wrist  = compute_arm_rooted(left_elbow,  forearm_ang_L, FOREARM_LEN)
    right_wrist = compute_arm_rooted(right_elbow, forearm_ang_R, FOREARM_LEN)

    # Collect all 15 markers
    points = [
        head,           #  1
        left_sh,        #  2
        right_sh,       #  3
        left_elbow,     #  4
        right_elbow,    #  5
        left_wrist,     #  6
        right_wrist,    #  7
        left_hp,        #  8
        right_hp,       #  9
        left_knee,      # 10
        right_knee,     # 11
        left_ankle,     # 12
        right_ankle,    # 13
        left_toe,       # 14
        right_toe       # 15
    ]

    return points

def main():
    start_time = pygame.time.get_ticks() / 1000.0

    running = True
    while running:
        # Event handling
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Clear screen
        SCREEN.fill(BLACK)

        # Current time
        now = pygame.time.get_ticks() / 1000.0
        t = now - start_time

        # Compute joint positions
        pts = get_joint_positions(t)

        # Draw each as a small white circle
        for (x, y) in pts:
            pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), 5)

        # Flip display
        pygame.display.flip()

        # Cap the frame rate
        CLOCK.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
