
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
fps = 30
duration = 5  # in seconds
steps = fps * duration

# Initial positions for the point-lights
positions = np.array([
    [4, 7],    # head
    [4, 5],    # torso
    [3, 4],    # left shoulder
    [5, 4],    # right shoulder
    [2, 3],    # left elbow
    [6, 3],    # right elbow
    [1, 2],    # left hand
    [7, 2],    # right hand
    [4, 6],    # left hip
    [4, 4],    # right hip
    [2, 5],    # left knee
    [6, 5],    # right knee
    [1, 4],    # left foot
    [7, 4],    # right foot
    [3.5, 3.5] # center of mass
])

# Function to simulate walking motion
def simulate_walking(positions, step):
    phase = step / steps * 2 * np.pi
    amplitude = 0.5
    frequency = 2

    walk_pattern = 0.5 * amplitude * np.sin(frequency * phase)

    motion = np.zeros(positions.shape)
    motion[8:14, 1] = walk_pattern * np.sin(np.arange(6) * np.pi / 6)
    motion[7, 0] += 0.5 * walk_pattern
    motion[11, 0] -= 0.5 * walk_pattern

    return positions + motion

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    pos = simulate_walking(positions, frame)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=1000/fps)

plt.show()
