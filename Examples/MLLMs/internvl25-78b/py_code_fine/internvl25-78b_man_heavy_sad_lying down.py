
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of frames
n_frames = 60

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1)

# Create a list of 15 point lights
points = ax.plot([], [], 'o', color='white')[0]

# Joint positions for a sadman lying down
def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / n_frames
    positions = np.array([
        [-0.4, 0.8 * np.sin(2 * np.pi * t)],  # Head
        [-0.35, 0.7 * np.sin(2 * np.pi * t)],  # Upper body 1
        [-0.3, 0.6 * np.sin(2 * np.pi * t)],  # Upper body 2
        [-0.25, 0.5 * np.sin(2 * np.pi * t)],  # Thorax
        [-0.2, 0.4 * np.sin(2 * np.pi * t)],  # Pelvis
        [0.2, 0.4 * np.sin(2 * np.pi * t)],  # Pelvis
        [0.25, 0.5 * np.sin(2 * np.pi * t)],  # Thorax
        [0.3, 0.6 * np.sin(2 * np.pi * t)],  # Upper body 2
        [0.35, 0.7 * np.sin(2 * np.pi * t)],  # Upper body 1
        [0.4, 0.8 * np.sin(2 * np.pi * t)],  # Head
        [-0.5, -0.8 + 0.2 * np.sin(2 * np.pi * t)],  # Left leg 1
        [-0.45, -0.9 + 0.2 * np.sin(2 * np.pi * t)],  # Left leg 2
        [0.5, -0.8 + 0.2 * np.sin(2 * np.pi * t)],  # Right leg 1
        [0.45, -0.9 + 0.2 * np.sin(2 * np.pi * t)],  # Right leg 2
        [0, -1.2 + 0.1 * np.sin(2 * np.pi * t)]  # Weight
    ])
    
    x, y = positions[:, 0], positions[:, 1]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, update, frames=n_frames,
                              init_func=init, blit=True, interval=100)

plt.axis('off')
plt.show()
