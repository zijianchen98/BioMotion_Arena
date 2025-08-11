
"""
Point–light biological–motion stimulus
15 white dots (a human jumper) on a black background
----------------------------------------------------

The script shows a simplified, yet biomechanically-plausible, side-view
animation of a man that repeatedly jumps forward.  The motion is completely
procedural – no external data files are required.

Exactly 15 point-lights – corresponding to common motion-capture marker
locations – are rendered:

    0  head
    1  chest (sternum)
    2  shoulder L     3  shoulder R
    4  elbow L        5  elbow R
    6  wrist L        7  wrist R
    8  hip L          9  hip R
   10  knee L        11  knee R
   12  ankle L       13  ankle R
   14  pelvis (root of the kinematic tree)

The code uses only the standard scientific-Python stack (NumPy and
Matplotlib) so it will run in any typical Python environment without extra
dependencies.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------- basic constants -----------------------------
FPS               = 60          # animation framerate
CYCLE_DURATION_S  = 2.0         # one jump = 2 s
N_FRAMES          = int(FPS * CYCLE_DURATION_S)
DT                = 1.0 / FPS

# anthropometric segment lengths (metres, arbitrarily chosen)
TORSO     = 0.60        # hip → shoulder-centre
NECK      = 0.10        # shoulder-centre → head-centre
HEAD      = 0.12        # head-centre → top of head
UPPER_ARM = 0.30
LOWER_ARM = 0.25
UPPER_LEG = 0.45
LOWER_LEG = 0.45

HIP_OFFSET      = 0.12  # half pelvis width
SHOULDER_OFFSET = 0.18  # half shoulder width

STAND_HIP_HEIGHT  = 0.95
CROUCH_HIP_HEIGHT = 0.70
PEAK_HIP_HEIGHT   = 1.20
STEP_LENGTH       = 1.60     # forward distance covered per jump

# helper for degree→radian conversion
def d2r(deg):
    return np.deg2rad(deg)

# -------------------------- motion-parameter curves -------------------------
# All parameters are C¹-smooth (cosine ease-in/ease-out) to avoid jerks.

def smoothstep(a, b, t):
    """0-1 cosine ease between times a and b."""
    if t < a:
        return 0.0
    if t > b:
        return 1.0
    x = (t - a) / (b - a)
    return 0.5 - 0.5 * np.cos(np.pi * x)


def hip_height(phase):
    """Vertical trajectory of the pelvis (root)."""
    # crouch, take-off, flight, landing
    h = (STAND_HIP_HEIGHT
         - (STAND_HIP_HEIGHT - CROUCH_HIP_HEIGHT) * smoothstep(0.00, 0.15, phase)   # crouch down
         + (PEAK_HIP_HEIGHT  - STAND_HIP_HEIGHT) * smoothstep(0.30, 0.50, phase)   # rise to peak
         - (PEAK_HIP_HEIGHT  - STAND_HIP_HEIGHT) * smoothstep(0.50, 0.70, phase)   # descent
         + (STAND_HIP_HEIGHT - CROUCH_HIP_HEIGHT) * smoothstep(0.70, 0.85, phase)) # landing crouch
    return h


def torso_pitch(phase):
    """Forward/backward lean of the torso (0 = straight up, +ve = leaning forward)."""
    return d2r(15) * np.sin(np.pi * phase)  # mild sinusoidal forward lean


def arm_angle(phase):
    """Shoulder flexion (0 = arms hanging, positive = arms forward/up)."""
    # swing arms back during crouch, then swing up in take-off, forward in flight, back again for landing
    return d2r(-30) * smoothstep(0.00, 0.15, phase)             + \
           d2r(110) * smoothstep(0.15, 0.45, phase)             + \
           d2r(-80) * smoothstep(0.65, 0.95, phase)


def knee_angle(phase):
    """Knee flexion (0 = straight, +ve = bend)."""
    bend = d2r(85)  # maximum flexion
    # bend for crouch, extend in flight, bend for landing, return to straight
    return bend * smoothstep(0.00, 0.15, phase)                          + \
           -bend * smoothstep(0.30, 0.50, phase)                         + \
            bend * smoothstep(0.70, 0.85, phase)


def forward_progress(phase):
    """Pelvis (root) X position – linear translation with each cycle."""
    return STEP_LENGTH * phase


# -------------------------- forward kinematics ------------------------------
def rotate(v, theta):
    """Rotate 2-vector v by angle theta (radians)."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])


def get_joint_positions(phase):
    """
    Return positions (x, y) for the 15 predefined body markers
    for a given phase ∈ [0, 1] of the jump cycle.
    """
    # ---------------- root (pelvis centre) ----------------
    root  = np.array([forward_progress(phase), hip_height(phase)])

    # pelvis (marker 14)
    pelvis_centre = root.copy()

    # hips
    hip_L = root + np.array([-HIP_OFFSET, 0.0])
    hip_R = root + np.array([ HIP_OFFSET, 0.0])

    # ---------------- torso ----------------
    pitch = torso_pitch(phase)
    torso_vec = rotate(np.array([0.0, TORSO]), pitch)
    shoulder_centre = root + torso_vec
    chest_centre    = shoulder_centre  # marker 1

    # shoulders
    shoulder_L = shoulder_centre + np.array([-SHOULDER_OFFSET, 0.0])
    shoulder_R = shoulder_centre + np.array([ SHLDR := SHOULDER_OFFSET, 0.0])  # noqa

    # ---------------- head ----------------
    neck_vec  = rotate(np.array([0.0, NECK + HEAD]), pitch)
    head = shoulder_centre + neck_vec

    # ---------------- arms ----------------
    arm = arm_angle(phase)

    upper_arm_vec    = rotate(np.array([ 0.0, -UPPER_ARM]), pitch + arm)   # downward is ‑Y
    lower_arm_vec    = rotate(np.array([ 0.0, -LOWER_ARM]), pitch + arm)
    elbow_L = shoulder_L + 0.5 * upper_arm_vec
    elbow_R = shoulder_R + 0.5 * upper_arm_vec
    wrist_L = elbow_L     + lower_arm_vec
    wrist_R = elbow_R     + lower_arm_vec

    # ---------------- legs ----------------
    knee_bend = knee_angle(phase)
    # For simplicity legs move in the sagittal plane only; left/right are identical
    upper_leg_vec = rotate(np.array([0.0, -UPPER_LEG]), knee_bend)  # rotate around hip
    lower_leg_vec = rotate(np.array([0.0, -LOWER_LEG]), -0.5 * knee_bend)

    knee_L  = hip_L + upper_leg_vec
    knee_R  = hip_R + upper_leg_vec
    ankle_L = knee_L + lower_leg_vec
    ankle_R = knee_R + lower_leg_vec

    # during ground-contact phases, pin ankles to ground (y = 0)
    if phase < 0.30 or phase > 0.70:
        ankle_L[1] = 0.0
        ankle_R[1] = 0.0
        # move knees vertically so leg length is preserved
        knee_L[1] = (hip_L[1] + ankle_L[1]) / 2.0
        knee_R[1] = (hip_R[1] + ankle_R[1]) / 2.0

    # ---------------- assemble marker list ----------------
    joints = np.vstack([
        head,                 # 0
        chest_centre,         # 1
        shoulder_L,           # 2
        shoulder_R,           # 3
        elbow_L,              # 4
        elbow_R,              # 5
        wrist_L,              # 6
        wrist_R,              # 7
        hip_L,                # 8
        hip_R,                # 9
        knee_L,               #10
        knee_R,               #11
        ankle_L,              #12
        ankle_R,              #13
        pelvis_centre         #14
    ])
    return joints


# -------------------------- Matplotlib animation ----------------------------
fig, ax = plt.subplots(facecolor='black')
fig.canvas.manager.set_window_title('Biological Motion: Jumping Forward')

# main scatter object (15 points) – initial dummy data
scat = ax.scatter(np.zeros(15), np.zeros(15),
                  s=36, c='white', edgecolor='none')

ax.set_aspect('equal')
ax.set_xlim(-0.5, STEP_LENGTH + 0.5)
ax.set_ylim(-0.1, 1.6)
ax.axis('off')               # hide axes, ticks, frame
ax.set_facecolor('black')    # black background


def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,


def update(frame):
    phase = (frame % N_FRAMES) / N_FRAMES  # 0…1
    pts   = get_joint_positions(phase)
    scat.set_offsets(pts)
    return scat,


ani = FuncAnimation(fig, update, init_func=init,
                    frames=N_FRAMES, interval=DT * 1000, blit=True, repeat=True)

plt.show()
