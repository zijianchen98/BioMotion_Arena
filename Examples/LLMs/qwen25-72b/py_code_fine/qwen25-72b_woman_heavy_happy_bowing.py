
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a woman bowing
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "hip_left", "knee_left", "ankle_left", "shoulder_right", "elbow_right",
    "wrist_right", "hip_right", "knee_right", "ankle_right", "pelvis"
]

# Initial positions of the points (x, y)
initial_positions = {
    "head": (0, 1.5),
    "neck": (0, 1.0),
    "shoulder_left": (-0.5, 0.8),
    "elbow_left": (-0.7, 0.4),
    "wrist_left": (-0.8, 0.1),
    "hip_left": (-0.3, -0.2),
    "knee_left": (-0.4, -0.6),
    "ankle_left": (-0.5, -1.0),
    "shoulder_right": (0.5, 0.8),
    "elbow_right": (0.7, 0.4),
    "wrist_right": (0.8, 0.1),
    "hip_right": (0.3, -0.2),
    "knee_right": (0.4, -0.6),
    "ankle_right": (0.5, -1.0),
    "pelvis": (0, -0.4)
}

# Function to update the positions of the points during the bow
def update_bow(frame):
    angle = np.radians(frame * 5)  # Smoothly increase the angle of the bow
    for key in initial_positions:
        x, y = initial_positions[key]
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        points[key].set_data(new_x, new_y)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the points
points = {}
for key in key_points:
    points[key], = ax.plot(*initial_positions[key], 'wo', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update_bow, frames=60, interval=50)

# Show the animation
plt.show()
