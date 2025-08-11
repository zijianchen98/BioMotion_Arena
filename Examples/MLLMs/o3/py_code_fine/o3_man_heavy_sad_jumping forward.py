
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------- skeleton constants ----------------- #
# All lengths are in arbitrary, self-consistent units
TORSO_LEN      = 0.60          # neck → pelvis (mid-hip)
HEAD_LEN       = 0.18          # neck → top of head
SHOULDER_W     = 0.42          # full shoulder span
UPPER_ARM_LEN  = 0.32
LOWER_ARM_LEN  = 0.30
THIGH_LEN      = 0.60
SHIN_LEN       = 0.60
HIP_OFFSET_X   = 0.14          # half width of pelvis/hips

BASE_PELVIS_Y  = THIGH_LEN + SHIN_LEN * 0.95   # height when standing ~1.17
GROUND_Y       = 0.0

# names kept only for readability / reference
(
    ID_HEAD,
    ID_NECK,
    ID_R_SHOULDER,
    ID_R_ELBOW,
    ID_R_WRIST,
    ID_L_SHOULDER,
    ID_L_ELBOW,
    ID_L_WRIST,
    ID_PELVIS,
    ID_R_HIP,
    ID_R_KNEE,
    ID_R_ANKLE,
    ID_L_HIP,
    ID_L_KNEE,
    ID_L_ANKLE
) = range(15)

# ----------------- helper utilities ----------------- #
def knee_position(hip, ankle, thigh_len, shin_len, side_sign):
    """
    2-D (x,y) inverse kinematics for a planar leg.
    side_sign = +1 for right leg / -1 for left leg => picks "forward" knee.
    """
    hx, hy = hip
    ax, ay = ankle
    dx, dy = ax - hx, ay - hy
    d = np.hypot(dx, dy)
    # clamp distance (helps during flight frames)
    d = np.clip(d, 1e-6, thigh_len + shin_len - 1e-6)

    # angle between thigh and the line hip→ankle
    cos_a = (thigh_len**2 + d**2 - shin_len**2) / (2 * thigh_len * d)
    cos_a = np.clip(cos_a, -1.0, 1.0)
    a = np.arccos(cos_a)

    # unit vector hip→ankle
    ux, uy = dx / d, dy / d
    # perpendicular
    px, py = -uy * side_sign, ux * side_sign

    # knee position by tri-angulation
    kx = hx + ux * (thigh_len * np.cos(a)) + px * (thigh_len * np.sin(a))
    ky = hy + uy * (thigh_len * np.cos(a)) + py * (thigh_len * np.sin(a))
    return kx, ky

def arm_chain(shoulder, down_amount):
    """
    Very simple ‘sad / heavy’ arm that mostly hangs down,
    slight bend at the elbow. down_amount ranges 0…1, where 1 = fully down
    """
    sx, sy = shoulder
    elbow_y = sy - UPPER_ARM_LEN * (0.3 + 0.7 * down_amount)
    wrist_y = elbow_y - LOWER_ARM_LEN * (0.7 + 0.3 * down_amount)
    return (sx, elbow_y), (sx, wrist_y)

# ----------------- motion parameterisation ----------------- #
def traj_pelvis(t_norm):
    """
    Pelvis (mid-hip) translation through the jump.
    Returns (x, y, ground_contact_bool)
    """
    # phases (sec proportion): stand 0-.2 | crouch .2-.4 | push-off .4-.45
    # flight .45-.70 | landing .70-.85 | stand-again .85-1.00
    if t_norm < 0.20:                         # quiet standing
        return 0.00, BASE_PELVIS_Y, True
    elif t_norm < 0.40:                      # crouching down
        p = (t_norm - 0.20) / 0.20
        y = BASE_PELVIS_Y - 0.35 * p
        return 0.00, y, True
    elif t_norm < 0.45:                      # explosive push-off
        p = (t_norm - 0.40) / 0.05
        x = 0.00 + 0.25 * p
        y = BASE_PELVIS_Y - 0.35 * (1.0 - p) + 0.10 * p
        return x, y, True
    elif t_norm < 0.70:                      # flight phase (parabolic arc)
        p = (t_norm - 0.45) / 0.25           # 0→1 within flight
        x = 0.25 + 1.10 * p
        # simple parabolic vertical displacement (peak at p=.5)
        y = (BASE_PELVIS_Y + 0.42) - 1.68 * (p - 0.5)**2
        return x, y, False
    elif t_norm < 0.85:                      # absorbing landing
        p = (t_norm - 0.70) / 0.15
        x = 1.35 + 0.25 * p
        y = (BASE_PELVIS_Y + 0.07) - 0.30 * p
        return x, y, True
    else:                                    # return to stance
        p = (t_norm - 0.85) / 0.15
        x = 1.60 + 0.20 * p
        y = (BASE_PELVIS_Y - 0.28) + 0.28 * p
        return x, y, True

def leg_chain(pelvis_x, pelvis_y, contact_ground, side_sign):
    """
    Returns hip, knee, ankle tuples for one leg.
    side_sign = +1 (right)  /  -1 (left)
    """
    hip_x = pelvis_x + HIP_OFFSET_X * side_sign
    hip_y = pelvis_y
    # ----- ankle target ----- #
    if contact_ground:
        ank_x = hip_x
        ank_y = GROUND_Y
    else:  # during flight: leg hangs somewhat back/down
        ank_x = hip_x - 0.10 * side_sign         # slight backward sweep
        ank_y = pelvis_y - 0.90 * (THIGH_LEN + SHIN_LEN)
    # compute knee position
    knee_x, knee_y = knee_position(
        (hip_x, hip_y), (ank_x, ank_y),
        THIGH_LEN, SHIN_LEN,
        side_sign
    )
    return (hip_x, hip_y), (knee_x, knee_y), (ank_x, ank_y)

def frame_coords(t_norm):
    """
    Produce 15 (x,y) coordinates for the current normalised time (0-1).
    Indexing follows the constant IDs declared above.
    """
    coords = np.zeros((15, 2))

    pelvis_x, pelvis_y, ground_contact = traj_pelvis(t_norm)
    coords[ID_PELVIS] = pelvis_x, pelvis_y

    # ------------- legs (left & right) ------------- #
    (lhx, lhy), (lkx, lky), (lax, lay) = leg_chain(pelvis_x, pelvis_y, ground_contact, -1)
    (rhx, rhy), (rkx, rky), (rax, ray) = leg_chain(pelvis_x, pelvis_y, ground_contact, +1)

    coords[ID_L_HIP]   = lhx, lhy
    coords[ID_L_KNEE]  = lkx, lky
    coords[ID_L_ANKLE] = lax, lay
    coords[ID_R_HIP]   = rhx, rhy
    coords[ID_R_KNEE]  = rkx, rky
    coords[ID_R_ANKLE] = rax, ray

    # ------------- torso & head ------------- #
    neck_x, neck_y = pelvis_x, pelvis_y + TORSO_LEN
    coords[ID_NECK] = neck_x, neck_y
    head_x, head_y = neck_x, neck_y + HEAD_LEN
    coords[ID_HEAD] = head_x, head_y

    # ------------- shoulders ------------- #
    lsx, lsy = neck_x - SHOULDER_W / 2.0, neck_y
    rsx, rsy = neck_x + SHOULDER_W / 2.0, neck_y
    coords[ID_L_SHOULDER] = lsx, lsy
    coords[ID_R_SHOULDER] = rsx, rsy

    # ------------- arms ------------- #
    # damped ‘down_amount’: arms hang more in crouch/landing, rise slightly in flight
    down_amount = 0.8
    if not ground_contact:
        down_amount = 0.3     # mild lift during airborne phase

    # left arm
    (lex, ley), (lwx, lwy) = arm_chain((lsx, lsy), down_amount)
    coords[ID_L_ELBOW] = lex, ley
    coords[ID_L_WRIST] = lwx, lwy

    # right arm
    (rex, rey), (rwx, rwy) = arm_chain((rsx, rsy), down_amount)
    coords[ID_R_ELBOW] = rex, rey
    coords[ID_R_WRIST] = rwx, rwy

    return coords

# ----------------- animation setup ----------------- #
FPS          = 30
DURATION_SEC = 4.5
N_FRAMES     = int(FPS * DURATION_SEC)

fig, ax = plt.subplots(figsize=(4, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# limits chosen to keep entire jump on screen
ax.set_xlim(-1.2, 3.0)
ax.set_ylim(-0.2, 2.2)

# initial scatter
scat = ax.scatter([], [], c='white', s=18)

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def animate(frame_idx):
    t_norm = frame_idx / (N_FRAMES - 1)
    pts = frame_coords(t_norm)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig,
                    animate,
                    frames=N_FRAMES,
                    init_func=init,
                    interval=1000 / FPS,
                    blit=True)

plt.show()
