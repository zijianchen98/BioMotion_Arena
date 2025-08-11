
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define key frames
key_times = np.array([0,1,2,3,4])
key_frames = [
    np.array([
        [0,1.8], [-0.2,1.6], [0.2,1.6], [-0.3,1.4], [0.3,1.4], [-0.3,1.2], [0.3,1.2], [-0.3,1.1], [0.3,1.1], [-0.1,1.0], [0.1,1.0], [-0.1,0.5], [0.1,0.5], [-0.1,0], [0.1,0]
    ]),
    np.array([
        [0,1.5], [-0.2,1.3], [0.2,1.3], [-0.4,1.2], [0.4,1.2], [-0.5,1.1], [0.5,1.1], [-0.52,1.05], [0.52,1.05], [-0.1,0.7], [0.1,0.7], [-0.2,0.4], [0.2,0.4], [-0.1,0], [0.1,0]
    ]),
    np.array([
        [0.5,2.0], [0.3,1.8], [0.7,1.8], [0.2,1.9], [0.8,1.9], [0.1,2.0], [0.9,2.0], [0.08,2.05], [0.92,2.05], [0.4,1.2], [0.6,1.2], [0.4,0.8], [0.6,0.8], [0.4,0.4], [0.6,0.4]
    ]),
    np.array([
        [1.0,2.0], [0.8,1.8], [1.2,1.8], [0.7,1.9], [1.3,1.9], [0.6,2.0], [1.4,2.0], [0.58,2.05], [1.42,2.05], [0.9,1.2], [1.1,1.2], [0.9,0.8], [1.1,0.8], [0.9,0.4], [1.1,0.4]
    ]),
    np.array([
        [1.5,1.5], [1.3,1.3], [1.7,1.3], [1.2,1.2], [1.8,1.2], [1.2,1.1], [1.8,1.1], [1.2,1.05], [1.8,1.05], [1.4,0.7], [1.6,0.7], [1.3,0.4], [1.7,0.4], [1.4,0], [1.6,0]
    ])
]

# Function to get positions at time t
def get_positions(t, key_times, key_frames):
    if t <= key_times[0]:
        return key_frames[0]
    elif t >= key_times[-1]:
        return key_frames[-1]
    else:
        for k in range(len(key_times)-1):
            if key_times[k] <= t < key_times[k+1]:
                alpha = (t - key_times[k]) / (key_times[k+1] - key_times[k])
                pos_k = key_frames[k]
                pos_k1 = key_frames[k+1]
                pos = (1 - alpha) * pos_k + alpha * pos_k1
                return pos

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 3)
ax.set_ylim(-0.5, 2.5)
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    t = i * 0.05  # dt = 0.05, for example
    pos = get_positions(t, key_times, key_frames)
    points.set_data(pos[:,0], pos[:,1])
    return points,

# Create animation
ani = FuncAnimation(fig, animate, frames=80, init_func=init, blit=True, interval=50)
plt.show()
