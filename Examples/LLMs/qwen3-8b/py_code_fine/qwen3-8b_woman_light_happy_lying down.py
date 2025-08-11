
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights
num_points = 15

# Define the body parts and their positions (approximate coordinates for a happy woman lying down)
body_parts = {
    'head': np.array([0, 0.6]),
    'neck': np.array([0, 0.4]),
    'shoulder_left': np.array([-0.2, 0.2]),
    'elbow_left': np.array([-0.4, 0.05]),
    'wrist_left': np.array([-0.5, -0.05]),
    'hand_left': np.array([-0.55, -0.15]),
    'shoulder_right': np.array([0.2, 0.2]),
    'elbow_right': np.array([0.4, 0.05]),
    'wrist_right': np.array([0.5, -0.05]),
    'hand_right': np.array([0.55, -0.15]),
    'hip_left': np.array([-0.1, -0.3]),
    'knee_left': np.array([-0.25, -0.5]),
    'ankle_left': np.array([-0.35, -0.7]),
    'foot_left': np.array([-0.4, -0.8]),
    'hip_right': np.array([0.1, -0.3]),
    'knee_right': np.array([0.25, -0.5]),
    'ankle_right': np.array([0.35, -0.7]),
    'foot_right': np.array([0.4, -0.8]),
}

# Assign each point light to a body part
point_indices = list(body_parts.keys())
point_positions = np.array([body_parts[p] for p in point_indices])

# Define the animation parameters
frame_rate = 30
total_frames = 100
t = np.linspace(0, 2 * np.pi, total_frames)

# Define a function to simulate realistic motion (sine wave with phase shift)
def get_position(t, index):
    phase = np.pi / 4 * index
    x = point_positions[index, 0] + 0.1 * np.sin(t + phase)
    y = point_positions[index, 1] + 0.1 * np.cos(t + phase)
    return x, y

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(num_points)]
for p in points:
    ax.add_patch(p)

# Animation function
def animate(i):
    for idx, point in enumerate(points):
        x, y = get_position(t[i], idx)
        point.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=total_frames, interval=1000 / frame_rate, blit=False)

# Show the animation
plt.show()
