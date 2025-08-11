
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define key times for the animation
key_times = np.array([0, 0.2, 0.3, 0.5, 0.7, 0.8, 1.0])

# Define key positions for each point at each key time
key_positions = np.zeros((15, 7, 2))

# Head
key_positions[0, :, 0] = 0
key_positions[0, :, 1] = [1.8, 1.6, 1.7, 2.3, 1.9, 1.6, 1.8]

# Left shoulder
key_positions[1, :, 0] = -0.2
key_positions[1, :, 1] = [1.6, 1.4, 1.5, 2.1, 1.7, 1.4, 1.6]

# Right shoulder
key_positions[2, :, 0] = 0.2
key_positions[2, :, 1] = [1.6, 1.4, 1.5, 2.1, 1.7, 1.4, 1.6]

# Left elbow
key_positions[3, :, 0] = -0.3
key_positions[3, :, 1] = [1.4, 1.2, 1.3, 1.9, 1.5, 1.2, 1.4]

# Right elbow
key_positions[4, :, 0] = 0.3
key_positions[4, :, 1] = [1.4, 1.2, 1.3, 1.9, 1.5, 1.2, 1.4]

# Left wrist
key_positions[5, :, 0] = -0.4
key_positions[5, :, 1] = [1.2, 1.0, 1.1, 1.7, 1.3, 1.0, 1.2]

# Right wrist
key_positions[6, :, 0] = 0.4
key_positions[6, :, 1] = [1.2, 1.0, 1.1, 1.7, 1.3, 1.0, 1.2]

# Left hip
key_positions[7, :, 0] = -0.1
key_positions[7, :, 1] = [1.0, 0.8, 0.9, 1.5, 1.1, 0.8, 1.0]

# Right hip
key_positions[8, :, 0] = 0.1
key_positions[8, :, 1] = [1.0, 0.8, 0.9, 1.5, 1.1, 0.8, 1.0]

# Left knee
key_positions[9, :, 0] = [-0.1, -0.15, -0.1, -0.1, -0.1, -0.15, -0.1]
key_positions[9, :, 1] = [0.6, 0.4, 0.5, 1.1, 0.7, 0.4, 0.6]

# Right knee
key_positions[10, :, 0] = [0.1, 0.15, 0.1, 0.1, 0.1, 0.15, 0.1]
key_positions[10, :, 1] = [0.6, 0.4, 0.5, 1.1, 0.7, 0.4, 0.6]

# Left ankle
key_positions[11, :, 0] = -0.1
key_positions[11, :, 1] = [0.2, 0.2, 0.25, 0.7, 0.3, 0.2, 0.2]

# Right ankle
key_positions[12, :, 0] = 0.1
key_positions[12, :, 1] = [0.2, 0.2, 0.25, 0.7, 0.3, 0.2, 0.2]

# Left foot
key_positions[13, :, 0] = -0.1
key_positions[13, :, 1] = [0.0, 0.0, 0.05, 0.5, 0.1, 0.0, 0.0]

# Right foot
key_positions[14, :, 0] = 0.1
key_positions[14, :, 1] = [0.0, 0.0, 0.05, 0.5, 0.1, 0.0, 0.0]

# Function to get position at time t for a point
def get_position(t, key_times, key_positions, point_index):
    idx = np.searchsorted(key_times, t, side='right') - 1
    if idx < 0:
        return key_positions[point_index, 0, :]
    elif idx >= len(key_times) - 1:
        return key_positions[point_index, -1, :]
    else:
        t1 = key_times[idx]
        t2 = key_times[idx + 1]
        pos1 = key_positions[point_index, idx, :]
        pos2 = key_positions[point_index, idx + 1, :]
        alpha = (t - t1) / (t2 - t1)
        return pos1 + alpha * (pos2 - pos1)

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.5)
ax.set_aspect('equal')

# Initial positions
initial_positions = [get_position(0, key_times, key_positions, i) for i in range(15)]
scatter = ax.scatter([p[0] for p in initial_positions], [p[1] for p in initial_positions], color='white', s=10)

# Update function for animation
def update(frame):
    t = frame / 99  # since frames go from 0 to 99
    positions = [get_position(t, key_times, key_positions, i) for i in range(15)]
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
