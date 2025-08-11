
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of frames in the animation
FRAMES = 120

# Scale factor to map the body model to screen coordinates
SCALE = 0.20
BASE_Y = 0.05  # baseline vertical offset so the "roll" stays near the bottom

# Local (model) coordinates for 15 point‐light markers in a side‐view skeleton:
# head, neck, chest, left shoulder, right shoulder, left elbow, right elbow,
# left wrist, right wrist, left hip, right hip, left knee, right knee, left ankle, right ankle
markers = np.array([
    [ 0.00, 1.50],  # head
    [ 0.00, 1.30],  # neck
    [ 0.00, 1.10],  # chest
    [ 0.20, 1.20],  # left shoulder
    [-0.20, 1.20],  # right shoulder
    [ 0.30, 0.90],  # left elbow
    [-0.30, 0.90],  # right elbow
    [ 0.40, 0.60],  # left wrist
    [-0.40, 0.60],  # right wrist
    [ 0.10, 0.80],  # left hip
    [-0.10, 0.80],  # right hip
    [ 0.15, 0.50],  # left knee
    [-0.15, 0.50],  # right knee
    [ 0.15, 0.10],  # left ankle
    [-0.15, 0.10],  # right ankle
])

# Center of rotation (hip center)
center = np.array([0.0, 0.80])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot of the 15 points
scatter = ax.scatter(
    np.zeros(15),
    np.zeros(15),
    c='white',
    s=50
)

# Animation update function
def update(frame):
    theta = 2 * np.pi * frame / FRAMES
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s],
                  [s,  c]])
    # Rotate each marker around the hip center
    rotated = (markers - center) @ R.T + center

    # Compute a left‐to‐right translation to simulate forward rolling
    tx = 0.10 + 0.80 * (frame / FRAMES)

    # Map to screen coordinates
    xs = rotated[:, 0] * SCALE + tx
    ys = rotated[:, 1] * SCALE + BASE_Y

    scatter.set_offsets(np.c_[xs, ys])
    return scatter,

# Create the animation
anim = animation.FuncAnimation(
    fig, update, frames=FRAMES, interval=40, blit=True
)

plt.show()
