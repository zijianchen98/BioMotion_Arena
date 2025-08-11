
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------
# Parameters that define body proportions
# -----------------------------------------------
HEAD_HEIGHT       = 6.0     # Head centre above hip
SHOULDER_HEIGHT   = 5.0
ELBOW_HEIGHT      = 4.0
WRIST_HEIGHT      = 3.5
HIP_HEIGHT        = 0.0
KNEE_HEIGHT       = -3.0
ANKLE_HEIGHT      = -6.0
FOOT_HEIGHT       = -6.5

SHOULDER_HALF_W   = 1.0
ELBOW_HALF_W      = 1.6
WRIST_HALF_W      = 1.9
HIP_HALF_W        = 0.8
KNEE_HALF_W       = 0.6
ANKLE_HALF_W      = 0.4
FOOT_HALF_W       = 0.8

# Indices of our 15 point–lights
(
    HEAD,
    L_SHOULDER, R_SHOULDER,
    L_ELBOW,    R_ELBOW,
    L_WRIST,    R_WRIST,
    SPINE,      # midpoint between hips
    L_HIP,      R_HIP,
    L_KNEE,     R_KNEE,
    L_ANKLE,    R_ANKLE
) = range(15)

# Animation parameters
FPS            = 60          # frames per second
CYCLE_FRAMES   = 180         # frames in one jump cycle
JUMP_HEIGHT    = 3.0         # peak hip elevation

# Pre-compute a list of phases (0→1) for each frame
phases = np.linspace(0, 1, CYCLE_FRAMES, endpoint=False)


def build_skeleton(phase):
    """
    Construct and return the 15 (x, y) coordinates for a single animation frame.
    `phase` ranges from 0→1 for one complete jump cycle.
    """
    coords = np.zeros((15, 2), dtype=float)   # (N, (x,y))

    # -------------------------------------------------------
    # 1. Decide how far into each ‘sub-phase’ we are
    #    0.00–0.20  : crouch (prepare)
    #    0.20–0.80  : flight
    #    0.80–1.00  : landing crouch
    # -------------------------------------------------------
    crouch_amt = 0.0
    flight     = 0.0
    if phase < 0.20:                       # preparing – bend knees
        crouch_amt = (0.20 - phase) / 0.20           # 1→0
    elif phase > 0.80:                     # landing – bend again
        crouch_amt = (phase - 0.80) / 0.20           # 0→1
    else:                                   # airborne
        flight_phase = (phase - 0.20) / 0.60         # 0→1
        flight = np.sin(np.pi * flight_phase)        # smooth up/down 0→1→0

    # -------------------------------------------------------
    # 2. Determine hip vertical position (base of skeleton)
    # -------------------------------------------------------
    hip_y = HIP_HEIGHT + JUMP_HEIGHT * flight - 2.0 * crouch_amt

    # -------------------------------------------------------
    # 3. Leg compression during crouch
    #    Shorten the effective length of upper/lower leg.
    # -------------------------------------------------------
    leg_scale = 1.0 - 0.35 * crouch_amt
    knee_y   = hip_y + KNEE_HEIGHT   * leg_scale
    ankle_y  = hip_y + ANKLE_HEIGHT  * leg_scale
    foot_y   = hip_y + FOOT_HEIGHT   * leg_scale

    # -------------------------------------------------------
    # 4. Upper-body vertical adjustment (torso compresses slightly)
    # -------------------------------------------------------
    torso_compress = 0.15 * crouch_amt
    shoulder_y = hip_y + SHOULDER_HEIGHT - torso_compress
    elbow_y    = hip_y + ELBOW_HEIGHT    - torso_compress
    wrist_y    = hip_y + WRIST_HEIGHT    - torso_compress
    head_y     = hip_y + HEAD_HEIGHT     - torso_compress

    # -------------------------------------------------------
    # 5. Arm animation – raise arms during flight
    # -------------------------------------------------------
    arm_raise = flight                     # 0 on ground, 1 at apex
    raise_amt = 3.0 * arm_raise            # additional upward shift
    elbow_y  += 0.6 * raise_amt
    wrist_y  += 1.2 * raise_amt

    # -------------------------------------------------------
    # 6. Populate coordinates (x, y) in anatomical order
    # -------------------------------------------------------
    # Head
    coords[HEAD] = (0.0, head_y)

    # Shoulders
    coords[L_SHOULDER] = (-SHOULDER_HALF_W, shoulder_y)
    coords[R_SHOULDER] = ( SHOULDER_HALF_W, shoulder_y)

    # Elbows
    coords[L_ELBOW] = (-ELBOW_HALF_W, elbow_y)
    coords[R_ELBOW] = ( ELBOW_HALF_W, elbow_y)

    # Wrists
    coords[L_WRIST] = (-WRIST_HALF_W, wrist_y)
    coords[R_WRIST] = ( WRIST_HALF_W, wrist_y)

    # Spine (hip centre)
    coords[SPINE] = (0.0, hip_y)

    # Hips
    coords[L_HIP] = (-HIP_HALF_W, hip_y)
    coords[R_HIP] = ( HIP_HALF_W, hip_y)

    # Knees
    coords[L_KNEE] = (-KNEE_HALF_W, knee_y)
    coords[R_KNEE] = ( KNEE_HALF_W, knee_y)

    # Ankles
    coords[L_ANKLE] = (-ANKLE_HALF_W, ankle_y)
    coords[R_ANKLE] = ( ANKLE_HALF_W, ankle_y)

    return coords


# -----------------------------------------------------------
# matplotlib animation
# -----------------------------------------------------------
plt.style.use('dark_background')                      # black bg, white points
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter for 15 points
initial_coords = build_skeleton(0.0)
scat = ax.scatter(initial_coords[:, 0],
                  initial_coords[:, 1],
                  s=60, c='white')

def update(frame):
    phase = phases[frame % CYCLE_FRAMES]
    coords = build_skeleton(phase)
    scat.set_offsets(coords)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=CYCLE_FRAMES,
                    interval=1000 / FPS,
                    blit=True)

plt.show()
