
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# If the code is executed in an environment without a display (e.g. automated tester),
# use a non-interactive backend to avoid errors.
matplotlib.use("Agg")

# ----------  CONSTANTS  ----------
N_DOTS       = 15          # number of point-lights
FPS          = 30          # frames per second
N_FRAMES     = 100         # total animation frames
GROUND_Y     = 0.0         # y-coordinate of the ground
JUMP_HEIGHT  = 2.0         # maximum COM (centre of mass) displacement
GRAVITY      = 2 * JUMP_HEIGHT / ((N_FRAMES // 2) / FPS)**2   # pick g so that the
                                                              # parabola finishes in half the frames

# ----------  BASE SKELETON (NEUTRAL STAND POSE) ----------
# Each element: (x, y)
# 0: head, 1-2: shoulders, 3-4: elbows, 5-6: hands,
# 7-8: hips, 9-10: knees, 11-12: ankles, 13-14: feet
pose_stand = np.array([
    [ 0.0, 6.0],   # head
    [-1.0, 5.0],   # L shoulder
    [ 1.0, 5.0],   # R shoulder
    [-1.5, 4.0],   # L elbow
    [ 1.5, 4.0],   # R elbow
    [-1.5, 3.0],   # L hand
    [ 1.5, 3.0],   # R hand
    [-0.8, 3.0],   # L hip
    [ 0.8, 3.0],   # R hip
    [-0.8, 1.5],   # L knee
    [ 0.8, 1.5],   # R knee
    [-0.8, 0.0],   # L ankle
    [ 0.8, 0.0],   # R ankle
    [-1.0,-0.1],   # L foot
    [ 1.0,-0.1]    # R foot
])

# ----------  CROUCH POSE (KNEES & HIPS FLEXED) ----------
pose_crouch = pose_stand.copy()
pose_crouch[:,1] -= 1.0          # lower every joint by 1 unit
pose_crouch[[3,4,5,6],1] -= 0.5  # elbows & hands lower a bit more
pose_crouch[[9,10],1]  -= 0.5    # knees bend (move further down)
pose_crouch[[1,2],1]   -= 0.5    # shoulders a bit more for a "sad" slouch
pose_crouch[0,1]       -= 0.5    # head lowers

# ----------  PARABOLIC TRAJECTORY FOR JUMP ----------
# Frames 0-24: crouch down
# Frames 25-49: push off + upward start of flight
# Frames 50-74: descending flight
# Frames 75-99: landing & crouch
phase_1 = np.arange(0, 25)
phase_2 = np.arange(25, 50)
phase_3 = np.arange(50, 75)
phase_4 = np.arange(75, 100)

# preallocate array [n_frames, n_dots, 2] for all coordinates
frames = np.zeros((N_FRAMES, N_DOTS, 2))

# ----------  BUILD ALL FRAMES ----------
for f in phase_1:  # crouch
    alpha = (f - phase_1[0]) / (len(phase_1)-1)
    frames[f] = (1 - alpha) * pose_stand + alpha * pose_crouch
    # no vertical offset yet (still on the ground)

# Up-thrust parameters
t_push_total = len(np.concatenate((phase_2, phase_3))) / FPS  # actual flight time
v0           = JUMP_HEIGHT * 4.0 / t_push_total               # choose v0 so that apex ≈ JUMP_HEIGHT
g            = 2.0 * JUMP_HEIGHT / (t_push_total / 2.0)**2    # compute fictitious gravity for symmetry

# Helper to obtain vertical centre-of-mass offset for any (delta_t) in flight
def y_offset(dt):
    return v0 * dt - 0.5 * g * dt**2

# Build phase_2 (push + ascent)
for idx, f in enumerate(phase_2):
    # Interpolate from crouch -> stand (legs extend)
    alpha = (idx) / (len(phase_2)-1)
    local_pose = (1 - alpha) * pose_crouch + alpha * pose_stand

    # time since take-off start
    dt = (idx+1) / FPS
    local_pose[:,1] += y_offset(dt)          # translate entire body upward
    frames[f] = local_pose

# Phase 3 (descent)
start_dt = len(phase_2) / FPS
for idx, f in enumerate(phase_3):
    dt = start_dt + (idx+1) / FPS
    local_pose = pose_stand.copy()
    local_pose[:,1] += y_offset(dt)
    frames[f] = local_pose

# Phase 4 (landing & crouch)
landing_frames = len(phase_4)
for idx, f in enumerate(phase_4):
    alpha = (idx) / (landing_frames-1)
    # interpolate stand -> crouch again
    local_pose = (1 - alpha) * pose_stand + alpha * pose_crouch
    dt = start_dt + (len(phase_3)) / FPS + (idx+1) / FPS
    yoff = y_offset(dt)
    # Once yoff becomes negative we clamp to zero (i.e. person hits the ground)
    if yoff < 0:
        yoff = 0
    local_pose[:,1] += yoff
    frames[f] = local_pose

# ----------  SET UP PLOT ----------
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor("black")
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 9)
sc = ax.scatter(frames[0][:,0], frames[0][:,1], c="white", s=30)

def update(frame_idx):
    coords = frames[frame_idx]
    sc.set_offsets(coords)
    return sc,

ani = FuncAnimation(fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True)

# If this script is executed in an interactive environment, show the animation window.
# Otherwise (e.g. during automated tests) simply save a gif so the code runs headless.
try:
    plt.show()
except Exception:
    ani.save("point_light_jump.gif", writer='pillow', fps=FPS)
