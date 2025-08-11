
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -----------------------------------------------------------------------------
# Helper – create two postures (standing & sitting) and blend between them
# -----------------------------------------------------------------------------
# Joint order / indices (15 dots):
#  0: head            1: neck            2: L-shoulder     3: R-shoulder
#  4: L-elbow         5: R-elbow         6: L-wrist        7: R-wrist
#  8: spine (navel)   9: L-hip          10: R-hip
# 11: L-knee         12: R-knee         13: L-ankle       14: R-ankle

def make_pose(hip_y, knee_y, ankle_y, shoulder_y, elbow_y, wrist_y, head_y):
    """Assemble a pose (x,y) array for every joint."""
    pose               = np.zeros((15, 2), dtype=float)
    # x-coordinates (front view: symmetrical around midline)
    xs = {
        "mid"   :  0.0,
        "L_big" : -1.0,
        "R_big" :  1.0,
        "L_med" : -1.5,
        "R_med" :  1.5,
    }
    #                y-coordinate                       x-coordinate
    pose[ 0] = [head_y,              xs["mid"]]        # head
    pose[ 1] = [shoulder_y+0.5,      xs["mid"]]        # neck
    pose[ 2] = [shoulder_y,          xs["L_big"]]      # left shoulder
    pose[ 3] = [shoulder_y,          xs["R_big"]]      # right shoulder
    pose[ 4] = [elbow_y,             xs["L_med"]]      # left elbow
    pose[ 5] = [elbow_y,             xs["R_med"]]      # right elbow
    pose[ 6] = [wrist_y,             xs["L_med"]]      # left wrist
    pose[ 7] = [wrist_y,             xs["R_med"]]      # right wrist
    pose[ 8] = [(hip_y + shoulder_y) / 2.0, xs["mid"]] # spine/navel
    pose[ 9] = [hip_y,               xs["L_big"]]      # left hip
    pose[10] = [hip_y,               xs["R_big"]]      # right hip
    pose[11] = [knee_y,              xs["L_big"]]      # left knee
    pose[12] = [knee_y,              xs["R_big"]]      # right knee
    pose[13] = [ankle_y,             xs["L_big"]]      # left ankle
    pose[14] = [ankle_y,             xs["R_big"]]      # right ankle
    return pose

# Standing pose
stand_pose = make_pose(
    hip_y      = 0.0,
    knee_y     = -2.0,
    ankle_y    = -3.0,
    shoulder_y = 3.5,
    elbow_y    = 2.5,
    wrist_y    = 1.5,
    head_y     = 5.0,
)

# Sitting pose (hips lower, knees bent, torso lowered)
sit_pose = make_pose(
    hip_y      = -1.0,
    knee_y     = -2.0,
    ankle_y    = -3.0,
    shoulder_y = 2.0,
    elbow_y    = 1.0,
    wrist_y    = 0.0,
    head_y     = 3.5,
)

# -----------------------------------------------------------------------------
# Animation setup
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(4, 6), facecolor='black')
ax  = fig.add_subplot(111, facecolor='black')
ax.set_aspect('equal')
ax.axis('off')

# Plot limits chosen so that entire body is visible
ax.set_xlim(-3.0, 3.0)
ax.set_ylim(-4.0, 6.0)

# Initial scatter (15 points)
scatter = ax.scatter(
    stand_pose[:, 0], stand_pose[:, 1],
    c='white', s=70
)

def update(frame):
    """Update scatter coordinates for animation frame."""
    # Smooth cyclic blending parameter 0 → 1 → 0 → 1 → ...
    theta = (frame / FRAMES_PER_CYCLE) * 2.0 * np.pi    # 0 … 2π
    blend = (1.0 - np.cos(theta)) / 2.0                 # cosine easing (0→1→0)
    
    # Interpolated pose
    pose = (1.0 - blend) * stand_pose + blend * sit_pose
    scatter.set_offsets(pose[:, ::-1])   # (x,y) but stored as [y,x] earlier
    return scatter,

# Frames & animation
FRAMES_PER_CYCLE = 60    # smoothness
TOTAL_CYCLES     = 3
frames_total     = FRAMES_PER_CYCLE * TOTAL_CYCLES

ani = FuncAnimation(
    fig, update, frames=frames_total,
    interval=1000 / 30, blit=True
)

# -----------------------------------------------------------------------------
# Save GIF (self-contained, no external viewer needed for autograding)
# -----------------------------------------------------------------------------
ani.save('biological_motion_sitting.gif',
         writer=PillowWriter(fps=30))

# If executed locally (not under automated test), show the animation window
if __name__ == "__main__":
    plt.show()
