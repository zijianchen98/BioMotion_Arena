
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
frames = 100
θ_max = np.pi / 4  # Maximum bowing angle (45 degrees)

# Define initial y-coordinates
head_y = 1.0
neck_y = 0.9
waist_y = 0.5
shoulder_y = 0.85
elbow_y = 0.7
wrist_y = 0.55
hip_y = 0.45
knee_y = 0.25
ankle_y = 0.0

# Define x-offset for left and right points
offset = 0.05

# Initial positions of the points
points_initial = {
    'head': (0, head_y),
    'neck': (0, neck_y),
    'waist': (0, waist_y),
    'left_shoulder': (-offset, shoulder_y),
    'right_shoulder': (offset, shoulder_y),
    'left_elbow': (-offset, elbow_y),
    'right_elbow': (offset, elbow_y),
    'left_wrist': (-offset, wrist_y),
    'right_wrist': (offset, wrist_y),
    'left_hip': (-offset, hip_y),
    'right_hip': (offset, hip_y),
    'left_knee': (-offset, knee_y),
    'right_knee': (offset, knee_y),
    'left_ankle': (-offset, ankle_y),
    'right_ankle': (offset, ankle_y),
}

# Points that rotate during bowing
rotating_points = ['head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist']

# Function to rotate a point around a pivot
def rotate_point(point, θ, pivot):
    x, y = point
    px, py = pivot
    x_trans = x - px
    y_trans = y - py
    x_rot = x_trans * np.cos(θ) + y_trans * np.sin(θ)
    y_rot = -x_trans * np.sin(θ) + y_trans * np.cos(θ)
    return (x_rot + px, y_rot + py)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1.1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the points
points = list(points_initial.values())
scatter = ax.scatter([p[0] for p in points], [p[1] for p in points], color='white', s=10)

# Update function for the animation
def update(frame):
    θ = θ_max * np.sin(np.pi * frame / frames)
    new_points = []
    for key in points_initial:
        if key in rotating_points:
            new_point = rotate_point(points_initial[key], θ, points_initial['waist'])
        else:
            new_point = points_initial[key]
        new_points.append(new_point)
    scatter.set_offsets(new_points)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=20, blit=True, repeat=True)

# Show the plot
plt.show()
