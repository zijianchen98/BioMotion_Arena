
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a woman bowing
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "shoulder_right", "elbow_right", "wrist_right", "hip_left",
    "knee_left", "ankle_left", "hip_right", "knee_right", "ankle_right", "pelvis"
]

# Initial positions (simplified 2D coordinates)
initial_positions = {
    "head": [0, 1.8],
    "neck": [0, 1.6],
    "shoulder_left": [-0.3, 1.4],
    "elbow_left": [-0.6, 1.2],
    "wrist_left": [-0.9, 1.0],
    "shoulder_right": [0.3, 1.4],
    "elbow_right": [0.6, 1.2],
    "wrist_right": [0.9, 1.0],
    "hip_left": [-0.2, 0.8],
    "knee_left": [-0.2, 0.4],
    "ankle_left": [-0.2, 0.0],
    "hip_right": [0.2, 0.8],
    "knee_right": [0.2, 0.4],
    "ankle_right": [0.2, 0.0],
    "pelvis": [0, 0.8]
}

# Function to update the positions for a bowing motion
def update_positions(frame):
    angle = np.radians(30 * np.sin(2 * np.pi * frame / 100))  # Bowing angle
    for key in initial_positions:
        x, y = initial_positions[key]
        if key != "pelvis":
            x_new = x * np.cos(angle) - (y - 0.8) * np.sin(angle)
            y_new = x * np.sin(angle) + (y - 0.8) * np.cos(angle) + 0.8
            initial_positions[key] = [x_new, y_new]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.0)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the point lights
point_lights = [plt.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Initialization function
def init():
    for i, key in enumerate(key_points):
        point_lights[i].set_data(initial_positions[key])
    return point_lights

# Animation update function
def animate(frame):
    update_positions(frame)
    for i, key in enumerate(key_points):
        point_lights[i].set_data(initial_positions[key])
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
