
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------
# Helper routines
# ---------------

def make_pose(alpha, arm_alpha):
    """
    Returns the 15 joint coordinates (x, y) of the skeleton in a LOCAL
    coordinate system with the hip–centre at (0, 0).

    alpha      : 0 (fully crouched)  ->  1 (fully extended legs)
    arm_alpha  : 0 (arms down)       ->  1 (arms up)
    """
    # --- Torso & head (do not change with alpha) ---
    head      = np.array([0.0,  1.9])
    neck      = np.array([0.0,  1.6])
    r_sho     = np.array([0.35, 1.55])
    l_sho     = np.array([-0.35,1.55])
    hip_centre= np.array([0.0,  0.0])
    r_hip     = np.array([0.25, 0.0])
    l_hip     = np.array([-0.25,0.0])

    # --- Legs (interpolated between crouched & extended) ---
    # Extended (alpha=1)
    r_knee_ext = np.array([0.25, -0.9])
    l_knee_ext = np.array([-0.25,-0.9])
    r_ank_ext  = np.array([0.25,-1.8])
    l_ank_ext  = np.array([-0.25,-1.8])

    # Crouched (alpha=0)
    r_knee_cr  = np.array([0.4, -0.4])
    l_knee_cr  = np.array([-0.4,-0.4])
    r_ank_cr   = np.array([0.55,-0.8])
    l_ank_cr   = np.array([-0.55,-0.8])

    r_knee = (1-alpha)*r_knee_cr + alpha*r_knee_ext
    l_knee = (1-alpha)*l_knee_cr + alpha*l_knee_ext
    r_ank  = (1-alpha)*r_ank_cr  + alpha*r_ank_ext
    l_ank  = (1-alpha)*l_ank_cr  + alpha*l_ank_ext

    # --- Arms (swing upward with arm_alpha) ---
    # Arms-down
    r_elb_down = np.array([0.55,1.0])
    l_elb_down = np.array([-0.55,1.0])
    r_wri_down = np.array([0.65,0.4])
    l_wri_down = np.array([-0.65,0.4])

    # Arms-up (above head)
    r_elb_up = np.array([0.25, 2.1])
    l_elb_up = np.array([-0.25,2.1])
    r_wri_up = np.array([0.0 , 2.7])
    l_wri_up = np.array([ 0.0, 2.7])

    r_elb = (1-arm_alpha)*r_elb_down + arm_alpha*r_elb_up
    l_elb = (1-arm_alpha)*l_elb_down + arm_alpha*l_elb_up
    r_wri = (1-arm_alpha)*r_wri_down + arm_alpha*r_wri_up
    l_wri = (1-arm_alpha)*l_wri_down + arm_alpha*l_wri_up

    # Pack joints in the requested order (15 points)
    joints = np.vstack([head, neck,
                        r_sho, l_sho,
                        r_elb, l_elb,
                        r_wri, l_wri,
                        hip_centre, r_hip, l_hip,
                        r_knee, l_knee,
                        r_ank, l_ank])
    return joints


def skeleton_at_global_t(t):
    """
    Build the global (x,y) coordinates of all joints
    for a given absolute time t (seconds).
    A single forward-jump cycle lasts JUMP_PERIOD seconds and the motion
    is tiled in time.
    """
    # Parameters that describe the forward jump
    JUMP_PERIOD = 1.2        # s  (complete take-off, flight, landing)
    H           = 1.2        # m  (jump height)
    D           = 1.5        # m  (horizontal distance)

    cycle_t = t % JUMP_PERIOD
    phase   = cycle_t / JUMP_PERIOD            # 0 … 1

    # Smooth vertical profile (sine) so that dy/dt = 0 at takeoff & landing
    y_cm = H * np.sin(np.pi*phase)             # 0 at ground, H at peak
    x_cm = D * phase                           # constant forward speed

    # Leg extension (crouch -> stretch -> crouch)
    alpha = np.clip(np.sin(np.pi*phase)*1.5, 0.0, 1.0) # 0 at start/end, ~1 airborne

    # Arm swing: start down, swing up during take-off, land down
    arm_alpha = np.clip(np.sin(np.pi*phase)*1.2, 0.0, 1.0)

    local_joints = make_pose(alpha, arm_alpha)

    # Shift by CM
    global_joints = local_joints + np.array([x_cm, y_cm])
    return global_joints


# -----------------
# Matplotlib set-up
# -----------------
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-0.5, 3.0)
ax.set_ylim(-2.2, 2.8)
ax.axis('off')    # no axes for a pure stimulus

# Create a single PathCollection (scatter) that we will update
pts = ax.scatter([], [], s=50, c='white')

# -------------
# Animation loop
# -------------
FPS   = 60
INTER = 1000 // FPS   # ms between frames

def init():
    pts.set_offsets(np.zeros((15, 2)))
    return (pts,)

def update(frame):
    t = frame / FPS                # time in seconds
    joints = skeleton_at_global_t(t)
    pts.set_offsets(joints)
    return (pts,)

anim = FuncAnimation(fig, update,
                     frames=600, interval=INTER,
                     init_func=init, blit=True, repeat=True)

# -----------
# Show window
# -----------
if __name__ == "__main__":
    plt.show()
