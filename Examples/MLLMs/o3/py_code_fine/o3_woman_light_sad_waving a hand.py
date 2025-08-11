
"""
Point-light stimulus: “sad woman (light weight) waving a hand”

The script creates a biological–motion style animation that consists of
exactly 15 white dots on a solid black background.  The dots correspond to
the main joints of a (female) human body.  To convey ‘sadness’ the figure
is slightly slumped and its head tilts forward; at the same time the right
hand executes a gentle waving gesture.

The animation is rendered with matplotlib.  When the script is executed it
opens a window that plays the stimulus in a continuous loop.  The same code
can be used non-interactively (e.g. inside Jupyter) – set SAVE_AS_GIF = True
to save the animation to *point_light_woman_waving.gif* instead.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# --------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------
FPS           = 30          # animation frames per second
DURATION      = 6           # seconds per cycle
N_FRAMES      = FPS*DURATION
FIGSIZE       = (4, 8)      # inches
DOT_SIZE      = 60          # scatter marker size
SAVE_AS_GIF   = False       # set True to export a GIF instead of showing

# --------------------------------------------------------------------
# Simple articulated model (2-D, side view)
# --------------------------------------------------------------------
# All lengths are relative to shoulder width == 1.0
LENGTH = {
    "neck"   : 0.18,
    "spine"  : 0.45,
    "hip"    : 0.2,
    "upper_arm" : 0.33,
    "fore_arm"  : 0.28,
    "thigh"     : 0.48,
    "shin"      : 0.46,
}

# Index map – exactly 15 labels
LABELS = [
    "head", "neck",
    "r_shoulder", "l_shoulder",
    "r_elbow", "l_elbow",
    "r_wrist", "l_wrist",
    "pelvis", "r_hip", "l_hip",
    "r_knee", "l_knee",
    "r_ankle", "l_ankle",
]

# --------------------------------------------------------------------
# Forward kinematics helpers
# --------------------------------------------------------------------
def rot(theta):
    """2-D rotation matrix (counter-clock-wise)."""
    s, c = np.sin(theta), np.cos(theta)
    return np.array([[c, -s],
                     [s,  c]])

def limb(start, length, angle):
    """Compute endpoint of a limb given start, length and world angle."""
    return start + rot(angle) @ np.array([0.0, -length])

# --------------------------------------------------------------------
# Animation key-frame generator
# --------------------------------------------------------------------
def skeleton_at_phase(phi):
    """
    Returns 15×2 array with the joint coordinates for
    the given phase 0…1 of the animation.
    """
    # Basic posture (slightly slumped – conveys sadness)
    shoulder_ctr = np.array([0.0, 0.0])            # origin of model

    # Head & torso ----------------------------------------------------
    neck  = shoulder_ctr + np.array([0.0, -LENGTH["neck"]*0.2])  # slight forward lean
    head  = neck + np.array([0.0, LENGTH["neck"]])               # small upward offset
    pelvis = shoulder_ctr + np.array([0.0, LENGTH["spine"]])

    # Hip joints
    r_hip = pelvis + np.array([ 0.15, 0.0])
    l_hip = pelvis + np.array([-0.15, 0.0])

    # Sad posture: head tilts forward 6°
    head = neck + rot(np.deg2rad(6)) @ np.array([0.0, LENGTH["neck"]])

    # Lower body (static – small sway could be added) -----------------
    r_knee  = limb(r_hip, LENGTH["thigh"], np.deg2rad(92))
    l_knee  = limb(l_hip, LENGTH["thigh"], np.deg2rad(88))
    r_ankle = limb(r_knee, LENGTH["shin"],  np.deg2rad(88))
    l_ankle = limb(l_knee, LENGTH["shin"],  np.deg2rad(92))

    # Upper body & waving arm -----------------------------------------
    # Shoulders
    r_shoulder = shoulder_ctr + np.array([ 0.25, 0.0])
    l_shoulder = shoulder_ctr + np.array([-0.25, 0.0])

    # LEFT arm (inactive, hangs down)
    l_elbow = limb(l_shoulder, LENGTH["upper_arm"], np.deg2rad(105))
    l_wrist = limb(l_elbow,    LENGTH["fore_arm"],  np.deg2rad(100))

    # RIGHT arm (waving) – motion driven by phase “phi”
    #   The elbow keeps a ~90° bend while the shoulder oscillates.
    shoulder_sweep = 25 * np.sin(2*np.pi*phi)   # ±25° front/back swing
    elbow_bend     = 90 + 10*np.sin(4*np.pi*phi + np.pi/3)  # small bend variation

    r_elbow_angle_world = np.deg2rad(70 - shoulder_sweep)   # downward-front
    r_elbow = limb(r_shoulder, LENGTH["upper_arm"], r_elbow_angle_world)

    # Fore-arm angle relative to elbow (outward wave)
    wrist_angle_world = r_elbow_angle_world - np.deg2rad(elbow_bend)

    # Add lateral waving of the wrist (~hand)
    wrist_side = 0.12 * np.sin(4*np.pi*phi)    # left/right offset
    r_wrist = limb(r_elbow, LENGTH["fore_arm"], wrist_angle_world) + np.array([wrist_side, 0])

    # Package all positions in order ---------------------------------
    data = np.vstack([
        head, neck,
        r_shoulder, l_shoulder,
        r_elbow, l_elbow,
        r_wrist, l_wrist,
        pelvis, r_hip, l_hip,
        r_knee, l_knee,
        r_ankle, l_ankle
    ])
    return data


# --------------------------------------------------------------------
# Matplotlib animation setup
# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=FIGSIZE)
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.axis('off')

# Prepare scatter plot (15 dots)
scat = ax.scatter([], [], s=DOT_SIZE, c="white")

# Pre-compute limits so the figure stays still
demo = skeleton_at_phase(0.0)
max_range = 1.6
ax.set_xlim(-max_range,  max_range)
ax.set_ylim( 1.6, -2.2)     # Y inverted to make upward positive for head

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def update(frame):
    phi = (frame % N_FRAMES) / N_FRAMES   # 0…1
    pts = skeleton_at_phase(phi)
    scat.set_offsets(pts)
    return scat,

ani = anim.FuncAnimation(fig, update,
                         frames=N_FRAMES,
                         init_func=init,
                         interval=1000/FPS,
                         blit=True,
                         repeat=True)

# --------------------------------------------------------------------
# Display or save
# --------------------------------------------------------------------
if SAVE_AS_GIF:
    print("Saving GIF … this may take a few seconds.")
    ani.save("point_light_woman_waving.gif",
             writer=anim.PillowWriter(fps=FPS))
else:
    plt.show()
