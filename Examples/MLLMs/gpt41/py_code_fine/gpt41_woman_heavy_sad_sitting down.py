
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- CONFIGURATIONS ---
FPS = 30
DURATION = 3  # seconds
N_FRAMES = FPS * DURATION
BG_COLOR = 'black'
DOT_COLOR = 'white'
DOT_SIZE = 70

# Body joint indices (convention, 15 dots)
# 0: head, 1: neck, 2: R shoulder, 3: L shoulder,
# 4: R elbow, 5: L elbow, 6: R wrist, 7: L wrist,
# 8: pelvis, 9: R hip, 10: L hip, 11: R knee, 12: L knee, 13: R ankle, 14: L ankle

# Define the mean pose for a sitting-down, heavy, sad woman in normalized coordinates
# Place the subject centered horizontally, upright at x=0.5
# Units: normalized 0-1

# Initial standing pose (start of sitting)
pose_standing = np.array([
    [0.5, 0.93],    # head
    [0.5, 0.87],    # neck
    [0.44, 0.87],   # R shoulder
    [0.56, 0.87],   # L shoulder
    [0.39, 0.80],   # R elbow
    [0.61, 0.80],   # L elbow
    [0.38, 0.74],   # R wrist
    [0.62, 0.74],   # L wrist
    [0.5, 0.73],    # pelvis
    [0.47, 0.73],   # R hip
    [0.53, 0.73],   # L hip
    [0.45, 0.56],   # R knee
    [0.55, 0.56],   # L knee
    [0.44, 0.36],   # R ankle
    [0.56, 0.36],   # L ankle
])

# Sitting down pose, slumped chest (sad posture), heavy person: knees more forward, lower center of mass, arms resting on knees
pose_sitting_sad = np.array([
    [0.5, 0.87],     # head (lower due to slump)
    [0.5, 0.82],     # neck
    [0.46, 0.82],    # R shoulder
    [0.54, 0.82],    # L shoulder
    [0.43, 0.75],    # R elbow (inwards, forward)
    [0.57, 0.75],    # L elbow
    [0.465, 0.63],   # R wrist (rest on knee)
    [0.535, 0.63],   # L wrist
    [0.5, 0.66],     # pelvis (lower)
    [0.47, 0.66],    # R hip
    [0.53, 0.66],    # L hip
    [0.45, 0.52],    # R knee (forward)
    [0.55, 0.52],    # L knee
    [0.46, 0.36],    # R ankle (forward)
    [0.54, 0.36],    # L ankle
])

# For heaviness, we keep proportions wide, and dot vertical distances smaller.
# For sadness, slump the head/chest forward and down, inward arms.

# Animation parameters: smooth in & out (ease)
def ease(t):
    # Ease in-out: smooth transition 0->1 as t goes 0->1
    return 0.5 - 0.5 * np.cos(np.pi * t)

# Add small random variation to simulate biological small fluctuations ("jitter") in each frame
def random_jitter(shape, scale=0.002):
    return (np.random.rand(*shape) - 0.5) * scale

# Create frames for animation
all_frames = []
for f in range(N_FRAMES):
    t = f / (N_FRAMES - 1)
    # Sitting down: interpolate from pose_standing to pose_sitting_sad
    # For heaviness, sitting takes a little longer and slower at the end (use non-linear easing)
    interp = ease(t)
    pose = (1 - interp) * pose_standing + interp * pose_sitting_sad
    # Add micro-jitter for realism
    jitter = random_jitter(pose.shape, 0.003 if interp > 0.2 else 0.001)
    pose += jitter
    all_frames.append(pose)

# -- PLOTTING / ANIMATION --

fig, ax = plt.subplots(figsize=(3.5, 7))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor(BG_COLOR)
ax.set_aspect('equal')
ax.axis('off')

# Set display limits to focus on the "woman"
ax.set_xlim(0.3, 0.7)
ax.set_ylim(0.30, 0.96)

# Plot the points for the first frame
scat = ax.scatter(
    all_frames[0][:, 0], all_frames[0][:, 1],
    s=DOT_SIZE, c=DOT_COLOR, edgecolors='none')

# Optionally: Define the "skeleton" connections to show how coherent/biomechanical the points move
body_lines = [
    (0, 1),  # head-neck
    (1, 2), (1, 3),  # neck-shoulders
    (2, 4), (3, 5),  # shoulders-elbows
    (4, 6), (5, 7),  # elbows-wrists
    (1,8),           # neck-pelvis
    (8,9), (8,10),   # pelvis-hips
    (9,11), (10,12), # hips-knees
    (11,13), (12,14) # knees-ankles
]

# We'll plot the lines in invisible color (almost black) for debugging,
# you can uncomment `plot_lines=True` to show them faintly.
plot_lines = False
if plot_lines:
    skel_lines = [
        ax.plot(
            [all_frames[0][i][0], all_frames[0][j][0]],
            [all_frames[0][i][1], all_frames[0][j][1]],
            color='gray', linewidth=1, alpha=0.2)
        for (i, j) in body_lines
    ]
else:
    skel_lines = []

# -- ANIMATION FUNC --
def update(frame_idx):
    pose = all_frames[frame_idx]
    scat.set_offsets(pose)
    # (optional) update skeleton lines
    if plot_lines:
        for line, (i, j) in zip(skel_lines, body_lines):
            line[0].set_data([pose[i][0], pose[j][0]], [pose[i][1], pose[j][1]])
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True, repeat=True)

plt.show()
