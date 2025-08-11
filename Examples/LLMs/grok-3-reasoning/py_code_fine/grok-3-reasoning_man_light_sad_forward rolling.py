
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define key_frames here. Each key frame is a (15, 2) numpy array of (x, y) positions.
# For example:
# key_frames = [
#     np.array([[x1,y1], [x2,y2], ...]),
#     np.array([[x1',y1'], [x2',y2'], ...]),
#     ...
# ]
# For demonstration, let's use dummy data
num_points = 15
key_frames = [np.random.rand(num_points, 2) * 10 for _ in range(4)]  # random positions between 0 and 10
key_times = np.arange(4)

def get_positions(t):
    if t < key_times[0]:
        return key_frames[0]
    elif t >= key_times[-1]:
        return key_frames[-1]
    else:
        i = np.searchsorted(key_times, t, side='right') - 1
        t0 = key_times[i]
        t1 = key_times[i+1]
        alpha = (t - t0) / (t1 - t0)
        positions = (1 - alpha) * key_frames[i] + alpha * key_frames[i+1]
        return positions

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, facecolor='black')

# Compute axis limits
all_positions = np.concatenate(key_frames, axis=0)
xmin = all_positions[:,0].min()
xmax = all_positions[:,0].max()
ymin = all_positions[:,1].min()
ymax = all_positions[:,1].max()
margin = 0.1 * max(xmax - xmin, ymax - ymin)
ax.set_xlim(xmin - margin, xmax + margin)
ax.set_ylim(ymin - margin, ymax + margin)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot
scatter = ax.scatter([], [], color='white', s=20)

def update(frame):
    t = frame / 30.0  # assume 30 fps, t in seconds
    positions = get_positions(t % key_times[-1])  # loop every key_times[-1] seconds
    scatter.set_offsets(positions)
    return scatter,

num_frames = 120  # for example, 4 seconds at 30 fps
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/30, blit=True)

plt.show()
