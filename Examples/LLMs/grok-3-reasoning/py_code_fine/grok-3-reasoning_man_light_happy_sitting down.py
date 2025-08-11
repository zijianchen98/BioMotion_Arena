
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the points with their positions at t=0 (standing), t=0.5 (intermediate), t=1 (seated)
points = [
    {'name': 'head', 'pos': [(0, 1.0), (0.05, 0.8), (0, 0.7)]},
    {'name': 'neck', 'pos': [(0, 0.9), (0.05, 0.75), (0, 0.65)]},
    {'name': 'left_shoulder', 'pos': [(-0.1, 0.9), (-0.05, 0.75), (-0.1, 0.65)]},
    {'name': 'right_shoulder', 'pos': [(0.1, 0.9), (0.15, 0.75), (0.1, 0.65)]},
    {'name': 'left_elbow', 'pos': [(-0.15, 0.8), (-0.1, 0.65), (-0.15, 0.55)]},
    {'name': 'right_elbow', 'pos': [(0.15, 0.8), (0.2, 0.65), (0.15, 0.55)]},
    {'name': 'left_wrist', 'pos': [(-0.2, 0.7), (-0.15, 0.55), (-0.2, 0.45)]},
    {'name': 'right_wrist', 'pos': [(0.2, 0.7), (0.25, 0.55), (0.2, 0.45)]},
    {'name': 'pelvis', 'pos': [(0, 0.5), (0, 0.3), (0, 0.4)]},
    {'name': 'left_hip', 'pos': [(-0.05, 0.5), (-0.05, 0.3), (-0.05, 0.4)]},
    {'name': 'right_hip', 'pos': [(0.05, 0.5), (0.05, 0.3), (0.05, 0.4)]},
    {'name': 'left_knee', 'pos': [(-0.05, 0.25), (-0.1, 0.2), (-0.15, 0.4)]},
    {'name': 'right_knee', 'pos': [(0.05, 0.25), (0.1, 0.2), (0.15, 0.5)]},
    {'name': 'left_ankle', 'pos': [(-0.05, 0.0), (-0.1, 0.0), (-0.15, 0.0)]},
    {'name': 'right_ankle', 'pos': [(0.05, 0.0), (0.1, 0.0), (0.15, 0.0)]},
]

# Function to get position of a point at time t
def get_position(point, t):
    if t < 0.5:
        # Interpolate between pos[0] and pos[1]
        factor = t / 0.5
        x = point['pos'][0][0] + (point['pos'][1][0] - point['pos'][0][0]) * factor
        y = point['pos'][0][1] +riar (point['pos'][1][1] - point['pos'][0][1]) * factor
    else:
        # Interpolate between pos[1] and pos[2]
        factor = (t - 0.5) / 0.5
        x = point['pos'][1][0] + (point['pos'][2][0] - point['pos'][1][0]) * factor
        y = point['pos'][1][1] + (point['pos'][2][1] - point['pos'][1][1]) * factor
    return x, y

# Set up the figure and axis
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.1, 1.1)
ax.set_axis_off()

# Initial positions
initial_positions = np.array([point['pos'][0] for point in points])
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=10)

# Update function for animation
def update(frame):
    t = frame / 29  # t goes from 0 to 1 over 30 frames
    positions = np.array([get_position(point, t) for point in points])
    scatter.set_offsets(positions)
    return scatter,

# Create animation
anim = FuncAnimation(fig, update, frames=range(30), interval=50, repeat=True)

plt.show()
