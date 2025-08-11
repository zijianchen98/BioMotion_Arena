import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
FRAMES = 60

# Define the 15 joints in a standing pose (x, y)
# (Approximate 2D coordinates for a "happy" heavy-set woman standing)
standing_pose = np.array([
    [0.0, 1.6],   # 1. Head
    [0.0, 1.45],  # 2. Neck
    [-0.15, 1.4], # 3. Left Shoulder
    [ 0.15, 1.4], # 4. Right Shoulder
    [-0.25, 1.2], # 5. Left Elbow
    [ 0.25, 1.2], # 6. Right Elbow
    [-0.3, 1.0],  # 7. Left Wrist
    [ 0.3, 1.0],  # 8. Right Wrist
    [-0.1, 1.0],  # 9. Left Hip
    [ 0.1, 1.0],  # 10. Right Hip
    [-0.1, 0.6],  # 11. Left Knee
    [ 0.1, 0.6],  # 12. Right Knee
    [-0.1, 0.2],  # 13. Left Ankle
    [ 0.1, 0.2],  # 14. Right Ankle
    [ 0.0, 1.2],  # 15. Torso center
])

# Define the same 15 joints in a sitting pose (x, y)
# (Approximate 2D coordinates for a "happy" heavy-set woman sitting down)
sitting_pose = np.array([
    [0.0, 1.4],
    [0.0, 1.3],
    [-0.15, 1.25],
    [ 0.15, 1.25],
    [-0.3, 1.0],
    [ 0.3, 1.0],
    [-0.4, 0.8],
    [ 0.4, 0.8],
    [-0.1, 0.8],
    [ 0.1, 0.8],
    [-0.1, 0.5],
    [ 0.1, 0.5],
    [-0.1, 0.2],
    [ 0.1, 0.2],
    [0.0, 1.0],
])

# Interpolation function between standing and sitting
def get_positions(t):
    # t in [0,1], 0 -> standing, 1 -> sitting
    return (1 - t) * standing_pose + t * sitting_pose

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor("black")
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect("equal")
ax.axis("off")

# Initial scatter
scatter = ax.scatter([], [], c="white", s=50)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Frame goes from 0 to FRAMES-1
    # We'll interpolate t from 0 to 1 over the duration
    t = frame / (FRAMES - 1)
    positions = get_positions(t)
    scatter.set_offsets(positions)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=FRAMES, init_func=init, blit=True, interval=50)

plt.show()