
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------
# Helper ­functions
# ---------------------------------------------
def rot(dx, dy, theta):
    """
    Rotate vector (dx, dy) by theta (rad) counter-clock-wise
    and return the rotated vector.
    """
    ct, st = np.cos(theta), np.sin(theta)
    return np.array([ct * dx - st * dy, st * dx + ct * dy])


def compute_skeleton(t):
    """
    Produce 15 joint coordinates (x, y) for the figure at time t.
    Returns an (15, 2) ndarray.
    Naming / indices
        0 : head
        1 : neck / shoulder-centre
        2 : L-shoulder
        3 : L-elbow
        4 : L-wrist
        5 : R-shoulder
        6 : R-elbow
        7 : R-wrist
        8 : hip-centre / pelvis
        9 : L-hip
        10: L-knee
        11: L-ankle
        12: R-hip
        13: R-knee
        14: R-ankle
    """
    # -- anthropometric lengths (arbitrary units) ---------------------------
    neck_len   = 0.28
    head_len   = 0.20
    torso_len  = 0.50
    shoulder_w = 0.35
    hip_w      = 0.30
    upper_arm  = 0.38
    fore_arm   = 0.34
    thigh_len  = 0.45
    shank_len  = 0.45

    # -- global, slow vertical bob (sad, heavy movement -> tiny amplitude) --
    bob_amp = 0.03
    bob = bob_amp * np.sin(2*np.pi*0.6*t)   # slow bob

    # ----------------------------------------------------------------------
    # Basic, static reference frame (pelvis at origin, x right, y up)
    # ----------------------------------------------------------------------
    hip_c = np.array([0.0, bob])                         # index 8
    l_hip = hip_c + np.array([-hip_w/2, 0.0])            # 9
    r_hip = hip_c + np.array([ hip_w/2, 0.0])            # 12

    neck  = hip_c + np.array([0.0, torso_len])           # 1
    head  = neck + np.array([0.0, neck_len + head_len])  # 0

    l_sho = neck + np.array([-shoulder_w/2, 0.0])        # 2
    r_sho = neck + np.array([ shoulder_w/2, 0.0])        # 5

    # ----------------------------------------------------------------------
    # LEFT ARM  (static, hanging down)
    # ----------------------------------------------------------------------
    l_elb = l_sho + np.array([0.0, -upper_arm])          # 3
    l_wri = l_elb + np.array([0.0, -fore_arm])           # 4

    # ----------------------------------------------------------------------
    # RIGHT ARM  (animated – waving)
    # ----------------------------------------------------------------------
    # Shoulder elevation + elbow flex make a hand-wave
    omega = 2*np.pi*0.5          # ~ 0.5 Hz -> slow wave
    the_sho = np.deg2rad(20) * np.sin(omega*t) + np.deg2rad(-25)   # base -25° (down-wards), swings upwards ±20°
    the_elb = np.deg2rad(40) * np.sin(omega*t*2)  + np.deg2rad(70) # elbow flexes around 70°, ±40°

    # Upper-arm vector (angle measured from negative y-axis)
    # Base vector (pointing straight down) is (0, -upper_arm)
    upper_vec = rot(0.0, -upper_arm, the_sho)

    r_elb = r_sho + upper_vec                                 # 6

    # Fore-arm vector rotated by additional the_elb relative to upper-arm
    fore_vec = rot(*np.array([*upper_vec]), the_elb)          # rotate by elbow flex
    fore_vec = fore_vec / np.linalg.norm(fore_vec) * fore_arm # ensure correct length

    r_wri = r_elb + fore_vec                                  # 7

    # ----------------------------------------------------------------------
    # LEGS  (static posture with a slight sway)
    # ----------------------------------------------------------------------
    sway_amp = 0.05
    sway = sway_amp * np.sin(2*np.pi*0.4*t)

    l_knee = l_hip + np.array([sway, -thigh_len])             # 10
    l_ank  = l_knee + np.array([0.0, -shank_len])             # 11

    r_knee = r_hip + np.array([sway, -thigh_len])             # 13
    r_ank  = r_knee + np.array([0.0, -shank_len])             # 14

    skeleton = np.vstack([head, neck,
                          l_sho, l_elb, l_wri,
                          r_sho, r_elb, r_wri,
                          hip_c,
                          l_hip, l_knee, l_ank,
                          r_hip, r_knee, r_ank])
    return skeleton


# ---------------------------------------------
# Matplotlib animation setup
# ---------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.4, 2.3)
ax.axis('off')

# Initialise scatter with 15 points
pts = ax.scatter([], [], s=70, c='white')

def init():
    pts.set_offsets(np.zeros((15, 2)))
    return pts,

def animate(frame):
    t = frame / 30.0      # 30 fps
    joints = compute_skeleton(t)
    pts.set_offsets(joints)
    return pts,

ani = FuncAnimation(fig,
                    animate,
                    frames=300,      # 10 seconds @30 fps
                    interval=33,
                    init_func=init,
                    blit=True)

if __name__ == "__main__":
    plt.show()
