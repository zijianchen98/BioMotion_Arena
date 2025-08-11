
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward roll
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "shoulder_right", "elbow_right", "wrist_right", "hip_left",
    "knee_left", "ankle_left", "hip_right", "knee_right", "ankle_right",
    "center_of_mass"
]

# Define the initial positions of the points
initial_positions = {
    "head": [0, 1.8],
    "neck": [0, 1.6],
    "shoulder_left": [-0.3, 1.5],
    "elbow_left": [-0.5, 1.3],
    "wrist_left": [-0.7, 1.1],
    "shoulder_right": [0.3, 1.5],
    "elbow_right": [0.5, 1.3],
    "wrist_right": [0.7, 1.1],
    "hip_left": [-0.2, 1.0],
    "knee_left": [-0.4, 0.6],
    "ankle_left": [-0.6, 0.2],
    "hip_right": [0.2, 1.0],
    "knee_right": [0.4, 0.6],
    "ankle_right": [0.6, 0.2],
    "center_of_mass": [0, 1.0]
}

# Define the animation frames
frames = 60
fps = 30

# Function to update the positions of the points for each frame
def update_positions(frame):
    t = frame / fps
    positions = {}
    for key in key_points:
        x, y = initial_positions[key]
        # Apply a sine wave to simulate the rolling motion
        x += 0.5 * np.sin(2 * np.pi * t)
        y += 0.5 * np.cos(2 * np.pi * t)
        positions[key] = [x, y]
    return positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], c='white', s=50)

# Update function for the animation
def animate(frame):
    positions = update_positions(frame)
    x = [positions[key][0] for key in key_points]
    y = [positions[key][1] for key in key_points]
    scat.set_offsets(np.c_[x, y])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/fps, repeat=True)

# Show the animation
plt.show()
