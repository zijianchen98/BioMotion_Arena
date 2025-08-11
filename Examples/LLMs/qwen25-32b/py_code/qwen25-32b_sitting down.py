
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights representing the man sitting down
initial_positions = {
    'head': [0, 2],
    'torso_top': [0, 1.5],
    'torso_bottom': [0, 1],
    'left_shoulder': [-0.5, 1.5],
    'right_shoulder': [0.5, 1.5],
    'left_elbow': [-0.75, 1.25],
    'right_elbow': [0.75, 1.25],
    'left_wrist': [-1, 1],
    'right_wrist': [1, 1],
    'left_hip': [-0.5, 0.5],
    'right_hip': [0.5, 0.5],
    'left_knee': [-0.5, 0],
    'right_knee': [0.5, 0],
    'left_ankle': [-0.5, -0.5],
    'right_ankle': [0.5, -0.5]
}

# Convert to numpy array for easier manipulation
positions = np.array(list(initial_positions.values()))

# Define the trajectory of each light during the sitting down motion
def update_positions(frame):
    # Simplified model for sitting down
    if frame <= 5:
        # Move torso and head down
        positions[0] = [0, 2 - 0.2 * frame]
        positions[1] = [0, 1.5 - 0.2 * frame]
        positions[2] = [0, 1 - 0.2 * frame]
    elif frame <= 10:
        # Continue moving torso and head down and bend knees
        positions[0] = [0, 2 - 0.4 * frame + 0.2]
        positions[1] = [0, 1.5 - 0.4 * frame + 0.2]
        positions[2] = [0, 1 - 0.4 * frame + 0.2]
        positions[11][1] = 0 - 0.1 * (frame - 5)
        positions[12][1] = 0 - 0.1 * (frame - 5)
    else:
        # Sit down and stabilize
        positions[0] = [0, 1]
        positions[1] = [0, 0.5]
        positions[2] = [0, 0]
        positions[11][1] = -0.5
        positions[12][1] = -0.5

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
points, = ax.plot([], [], 'wo')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    update_positions(i)
    x = positions[:, 0]
    y = positions[:, 1]
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=15, init_func=init, blit=True, interval=100)

plt.show()
