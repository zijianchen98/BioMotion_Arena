
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --------------------  configuration  -------------------- #
N_POINTS       = 15            # exactly 15 point-lights
FPS            = 30            # frames per second
DURATION       = 4             # seconds for one full bow–return cycle
AMPLITUDE_DEG  = 50            # peak forward-lean angle (deg)
FIGSIZE        = (4, 6)        # inches
POINT_SIZE     = 60            # scatter point size
# --------------------------------------------------------- #

# Index map for clarity
HEAD, NECK, R_SHOULDER, L_SHOULDER, R_ELBOW, L_ELBOW, \
R_WRIST, L_WRIST, R_HIP, L_HIP, R_KNEE, L_KNEE, \
R_ANKLE, L_ANKLE, PELVIS = range(15)

# -----------------  base (upright) skeleton  -------------- #
#
# Coordinates are given in a 2-D side-view (x = forward/back,
# y = vertical).  Units are arbitrary but internally consistent.
#
base = np.zeros((N_POINTS, 2))
# vertical column (x == 0 when upright)
base[HEAD]        = [ 0.0,  7.0]
base[NECK]        = [ 0.0,  6.0]
base[R_SHOULDER]  = [ 0.0,  6.0]
base[L_SHOULDER]  = [ 0.0,  6.0]
base[R_ELBOW]     = [ 0.0,  5.0]
base[L_ELBOW]     = [ 0.0,  5.0]
base[R_WRIST]     = [ 0.0,  4.0]
base[L_WRIST]     = [ 0.0,  4.0]
base[R_HIP]       = [ 0.0,  4.0]
base[L_HIP]       = [ 0.0,  4.0]
base[R_KNEE]      = [ 0.0,  2.0]
base[L_KNEE]      = [ 0.0,  2.0]
base[R_ANKLE]     = [ 0.0,  0.0]
base[L_ANKLE]     = [ 0.0,  0.0]
base[PELVIS]      = [ 0.0,  4.0]     # mid-point between hips
# ---------------------------------------------------------- #

# joints that rotate as one rigid upper-body segment
upper_body_indices = [HEAD, NECK,
                      R_SHOULDER, L_SHOULDER,
                      R_ELBOW,    L_ELBOW,
                      R_WRIST,    L_WRIST]

pelvis_origin = base[PELVIS].copy()
leg_indices   = [R_HIP, L_HIP, R_KNEE, L_KNEE, R_ANKLE, L_ANKLE]

# ----------  figure & axis styling (black background) ----- #
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor('black')
ax.set_xlim(-4, 8)
ax.set_ylim(-1, 8)
ax.set_aspect('equal')
ax.axis('off')  # no border / ticks

# scatter plot that will be updated every frame
scat = ax.scatter(base[:, 0], base[:, 1],
                  c='white', s=POINT_SIZE)

# ------------------  animation update  -------------------- #
total_frames = int(FPS * DURATION)

def rotate(vec, angle_rad):
    """2-D rotation of a vector by given angle about origin."""
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    x, y = vec.T
    return np.column_stack(( c*x + s*y,
                            -s*x + c*y ))

def frame(step):
    phase   = step / total_frames            # 0 … 1
    angle   = np.deg2rad(AMPLITUDE_DEG) * np.sin(2*np.pi*phase)
    current = base.copy()

    # rotate whole upper body about the pelvis
    vecs = current[upper_body_indices] - pelvis_origin      # shift to origin
    current[upper_body_indices] = rotate(vecs, angle) + pelvis_origin

    # slight knee flex when bowing (more flex when deeper)
    knee_bend = 0.4 * (np.sin(angle) ** 2)                  # 0 … 0.4
    for hip, knee, ankle in [(R_HIP, R_KNEE, R_ANKLE),
                             (L_HIP, L_KNEE, L_ANKLE)]:
        # hip stays put (acts like hinge). Move knee forward,
        # drop ankle a touch to keep leg length plausible.
        current[knee, 0]  +=  1.2 * knee_bend               # forward
        current[knee, 1]  -=  0.3 * knee_bend               # down
        current[ankle, 0] +=  1.8 * knee_bend
        current[ankle, 1] -=  0.3 * knee_bend

    # centre-of-mass dips slightly at deepest point (heavy weight!)
    dip = 0.3 * (np.sin(angle) ** 2)
    current[:, 1] -= dip

    scat.set_offsets(current)
    return scat,

ani = animation.FuncAnimation(fig,
                              frame,
                              frames=total_frames,
                              interval=1000/FPS,
                              blit=True)

plt.show()
