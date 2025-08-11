
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup figure
fig, ax = plt.subplots(figsize=(5, 8))
ax.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)

# Initialize 15 points for biological motion ('happy person waving')
points, = ax.plot([], [], 'o', color='white', markersize=9)

# Define initial body coordinates (head, shoulders, elbows, wrists, hip-left/right, knee-left/right, ankle-left/right)
def body_coords(t):
    head = [0, 1.8]
    neck = [0, 1.6]
    shoulder_l = [-0.3, 1.5]
    shoulder_r = [0.3, 1.5]
    elbow_l = [-0.45, 1.35]
    elbow_r = [0.45, 1.35 + 0.1*np.sin(3*t)]
    wrist_l = [-0.4, 1.15]
    wrist_r = [0.55, 1.1 + 0.2*np.sin(3*t)]
    hip_l = [-0.2, 1]
    hip_r = [0.2, 1]
    knee_l = [-0.25, 0.6]
    knee_r = [0.25, 0.6]
    ankle_l = [-0.3, 0.2]
    ankle_r = [0.3, 0.2]

    # Chest and abdomen points (static anchor points)
    chest = [0, 1.4]
    abdomen = [0, 1.2]

    # Combine all points
    coords = np.array([head, neck, shoulder_l, shoulder_r, elbow_l, elbow_r, wrist_l, wrist_r,
                       chest, abdomen, hip_l, hip_r, knee_l, knee_r, ankle_l])
    return coords

# initialize points for animation
def init():
    points.set_data([], [])
    return points,

# animation function called sequentially
def animate(frame):
    t = frame / 10.0
    coords = body_coords(t)
    points.set_data(coords[:, 0], coords[:, 1])
    return points,

# Set black background
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=200, interval=50, blit=True)

plt.show()
