
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

######################################################################
# 15-point skeleton (indices)
#  0 head            8 root / pelvis
#  1 neck            9 R-hip  12 L-hip
#  2 R-shoulder     10 R-knee 13 L-knee
#  3 R-elbow        11 R-ank  14 L-ank
#  4 R-wrist
#  5 L-shoulder
#  6 L-elbow
#  7 L-wrist
######################################################################

# Basic (front-view) horizontal offsets at rest (metres – arbitrary units)
X_REST = np.array([0.00,  0.00,  0.15,  0.25,  0.35,
                  -0.15, -0.25, -0.35,  0.00,  0.10,
                   0.10,  0.10, -0.10, -0.10, -0.10])

# Basic vertical coordinates (metres) when standing
Y_REST = np.array([1.80, 1.60, 1.55, 1.25, 0.95,
                   1.55, 1.25, 0.95, 1.00, 1.00,
                   0.55, 0.00, 1.00, 0.55, 0.00])

# Animation parameters
FPS          = 30
CYCLE_FRAMES = FPS * 2                 # 2-second jump cycle
TOTAL_FRAMES = CYCLE_FRAMES * 3        # 3 cycles in total
CROUCH_DY    = 0.25                    # crouch depth (m)
JUMP_DY      = 0.60                    # jump apex above stand (m)
FORWARD_DX   = 0.50                    # forward motion per cycle (m)

def easing(x):
    """Smoothstep easing (0–1)."""
    return 3*x**2 - 2*x**3

def skeleton_at_phase(phi):
    """
    Return 15-point (x, y) arrays for cycle phase phi in [0, 1).
    phi = 0   start standing
    0–0.25    crouch
    0.25–0.35 launch
    0.35–0.65 airborne
    0.65–1    landing & recover
    """
    x = X_REST.copy()
    y = Y_REST.copy()

    # Global forward (x) and vertical (y) displacement of the whole body
    global_dy = 0.0
    global_dx = FORWARD_DX * phi

    # Determine which sub-phase we are in
    if phi < 0.25:  # crouching
        k = easing(phi / 0.25)         # 0 → 1
        global_dy -= CROUCH_DY * k
        knee_bend = k
    elif phi < 0.35:  # take-off (rapid extension)
        k = (phi - 0.25) / 0.10        # 0 → 1
        global_dy = -CROUCH_DY * (1 - k)
        knee_bend = 1 - k
    elif phi < 0.65:  # airborne (parabolic arc)
        k = (phi - 0.35) / 0.30        # 0 → 1
        # smooth parabola: sin(pi*k)
        arc = np.sin(np.pi * k)
        global_dy = JUMP_DY * arc
        knee_bend = 0.0
    else:             # landing
        k = (phi - 0.65) / 0.35        # 0 → 1
        global_dy = JUMP_DY * (1 - k) - CROUCH_DY * k
        knee_bend = k

    # Apply global translation
    x += global_dx
    y += global_dy

    # Knee flexion/extension (simple vertical offset relative to hip & ankle)
    # Knees approach hips during crouch/landing
    y[10]  = y[9]  - 0.45 + 0.25 * knee_bend   # R-knee
    y[13]  = y[12] - 0.45 + 0.25 * knee_bend   # L-knee
    # Ankles stay on ground unless airborne
    if phi < 0.25 or phi > 0.65:        # feet on ground
        y[[11, 14]] = 0.0 + global_dy * 0  # keep relative ground contact
    else:                               # airborne: lift ankles with body
        y[[11, 14]] = Y_REST[[11, 14]] + global_dy

    # Shoulder slump & head drop to convey "sad" affect
    slump = 0.06
    y[[2, 5]] -= slump
    y[0]      -= slump * 1.5
    # Slight inward shoulder roll
    x[[2, 5]] *= 0.75

    return x, y

# --------------------------------------------------------------------
# Matplotlib setup
fig = plt.figure(figsize=(4, 6), facecolor='black')
ax  = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.5 + FORWARD_DX * 3)
ax.set_ylim(-0.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

# Scatter for the 15 points
pts, = ax.plot([], [], 'o', color='white', markersize=6)

def init():
    pts.set_data([], [])
    return pts,

def animate(frame):
    # Cycle progress 0–1
    phi = (frame % CYCLE_FRAMES) / CYCLE_FRAMES
    # Whole stimulus progresses forward each completed cycle
    global_phase_shift = (frame // CYCLE_FRAMES) * FORWARD_DX
    x, y = skeleton_at_phase(phi)
    x += global_phase_shift
    pts.set_data(x, y)
    return pts,

ani = FuncAnimation(fig, animate, frames=TOTAL_FRAMES,
                    init_func=init, interval=1000/FPS, blit=True)

plt.show()
