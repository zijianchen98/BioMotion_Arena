
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define key times
key_times = [0, 0.25, 0.5, 0.75, 1.0]

# Define key points for each key frame
key_points = [
    np.array([(0,1.6), (-0.2,1.4), (0.2,1.4), (-0.2,1.0), (0.2,1.0), (-0.2,0.6), (0.2,0.6), (-0.2,0.5), (0.2,0.5), (-0.1,0.8), (0.1,0.8), (-0.1,0.4), (0.1,0.4), (-0.1,0), (0.1,0)]),
    np.array([(0,0.8), (-0.15,0.6), (0.15,0.6), (-0.25,0.6), (0.25,0.6), (-0.35,0.6), (0.35,0.6), (-0.4,0.6), (0.4,0.6), (-0.05,0.5), (0.05,0.5), (-0.05,0.2), (0.05,0.2), (-0.1,0), (0.1,0)]),
    np.array([(0.5,0.3), (0.4,0.4), (0.6,0.4), (0.3,0.3), (0.7,0.3), (0.2,0.2), (0.8,0.2), (0.15,0.15), (0.85,0.15), (0.4,0.2), (0.6,0.2), (0.3,0.1), (0.7,0.1), (0.2,0), (0.8,0)]),
    np.array([(1.5,0.8), (1.5-0.15,0.6), (1.5+0.15,0.6), (1.5-0.25,0.6), (1.5+0.25,0.6), (1.5-0.35,0.6), (1.5+0.35,0.6), (1.5-0.4,0.6), (1.5+0.4,0.6), (1.5-0.05,0.5), (1.5+0.05,0.5), (1.5-0.05,0.2), (1.5+0.05,0.2), (1.5-0.1,0), (1.5+0.1,0)]),
    np.array([(2.0,1.6), (2.0-0.2,1.4), (2.0+0.2,1.4), (2.0-0.2,1.0), (2.0+0.2,1.0), (2.0-0.2,0.6), (2.0+0.2,0.6), (2.0-0.2,0.5), (2.0+0.2,0.5), (2.0-0.1,0.8), (2.0+0.1,0.8), (2.0-0.1,0.4), (2.0+0.1,0.4), (2.0-0.1,0), (2.0+0.1,0)]),
]

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.0)
scatter = ax.scatter([], [], c='white', s=50)

# Update function for animation
def update(t):
    # Find the key frame interval
    for i in range(len(key_times)-1):
        if key_times[i] <= t <= key_times[i+1]:
            alpha = (t - key_times[i]) / (key_times[i+1] - key_times[i])
            points = (1 - alpha) * key_points[i] + alpha * key_points[i+1]
            break
    else:
        points = key_points[-1]  # if t > 1.0
    scatter.set_offsets(points)
    return scatter,

# Create animation
anim = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True)

plt.show()
