
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------
#  Helper functions
# -------------------------------------------------
def forward_kinematics(shoulder, lu, ll, shoulder_angle, elbow_angle):
    """
    2-D forward kinematics for a single arm.
      shoulder        : (x, y) tuple
      lu, ll          : upper–arm and lower–arm lengths
      shoulder_angle  : 0° points straight down, +CCW
      elbow_angle     : inner angle at elbow (180° = straight)
    Returns elbow, wrist 2-D coordinates.
    """
    # Shoulder angle wrt downward vertical
    a = np.deg2rad(shoulder_angle)
    # Elbow flexion (convert to the absolute orientation of the lower arm)
    b = np.deg2rad(elbow_angle)
    # Upper-arm vector
    ex = shoulder[0] + lu * np.sin(a)
    ey = shoulder[1] - lu * np.cos(a)
    # Lower-arm orientation
    lower_dir = a + np.pi - b
    wx = ex + ll * np.sin(lower_dir)
    wy = ey - ll * np.cos(lower_dir)
    return (ex, ey), (wx, wy)


# -------------------------------------------------
#  Static body landmarks (15 points)
# -------------------------------------------------
# Basic proportions (metres purely for relative positioning)
head            = (0.0, 1.80)
torso           = (0.0, 1.45)     # sternum
pelvis          = (0.0, 1.10)

l_shoulder      = (-0.25, 1.60)
r_shoulder      = ( 0.25, 1.60)

l_hip           = (-0.20, 1.10)
r_hip           = ( 0.20, 1.10)

l_knee          = (-0.20, 0.60)
r_knee          = ( 0.20, 0.60)

l_ankle         = (-0.20, 0.00)
r_ankle         = ( 0.20, 0.00)

# Left arm is kept still
l_elbow         = (-0.35, 1.30)
l_wrist         = (-0.45, 1.00)

# Arm segment lengths for the right (waving) arm
UPPER_ARM = 0.35
LOWER_ARM = 0.30

# -------------------------------------------------
#  Animation
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-0.2, 2.1)
ax.axis('off')

# Create a scatter plot with 15 points
scatter = ax.scatter([0]*15, [0]*15, s=50, c='white')

# Frame count & timing
FPS     = 30
DUR_SEC = 4           # total duration of loop
N       = FPS * DUR_SEC
t_vals  = np.linspace(0, 1, N)  # normalized time

def update(frame):
    t = t_vals[frame]

    # Right-arm kinematics (simple waving)
    # Shoulder performs a wide arc; elbow flexes slightly out of phase
    shoulder_angle = 70 + 40 * np.sin(2*np.pi * 1.5 * t)     # 70° ±40°
    elbow_angle    = 150 - 20 * np.sin(2*np.pi * 1.5 * t + np.pi/3)

    r_elbow, r_wrist = forward_kinematics(r_shoulder,
                                          UPPER_ARM, LOWER_ARM,
                                          shoulder_angle, elbow_angle)

    # Assemble the 15 marker positions
    points = np.array([
        head,
        l_shoulder, r_shoulder,
        l_elbow, r_elbow,
        l_wrist, r_wrist,
        torso,
        pelvis,
        l_hip, r_hip,
        l_knee, r_knee,
        l_ankle, r_ankle
    ])

    scatter.set_offsets(points)
    return scatter,

ani = FuncAnimation(fig, update, frames=N, interval=1000/FPS, blit=True)
plt.show()
