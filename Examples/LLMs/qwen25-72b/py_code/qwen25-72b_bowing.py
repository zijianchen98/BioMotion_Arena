
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a man bowing
key_points = [
    "head", "neck", "shoulder_left", "shoulder_right",
    "elbow_left", "elbow_right", "wrist_left", "wrist_right",
    "hip_left", "hip_right", "knee_left", "knee_right",
    "ankle_left", "ankle_right", "pelvis"
]

# Initial positions of the points (x, y)
initial_positions = {
    "head": (0, 1.8),
    "neck": (0, 1.6),
    "shoulder_left": (-0.3, 1.4),
    "shoulder_right": (0.3, 1.4),
    "elbow_left": (-0.6, 1.2),
    "elbow_right": (0.6, 1.2),
    "wrist_left": (-0.9, 1.0),
    "wrist_right": (0.9, 1.0),
    "hip_left": (-0.3, 0.8),
    "hip_right": (0.3, 0.8),
    "knee_left": (-0.3, 0.4),
    "knee_right": (0.3, 0.4),
    "ankle_left": (-0.3, 0.0),
    "ankle_right": (0.3, 0.0),
    "pelvis": (0, 0.6)
}

# Function to update the positions of the points during the bowing motion
def update_bow(frame):
    angle = frame * np.pi / 180  # Convert frame to angle in radians
    for key in initial_positions:
        x, y = initial_positions[key]
        new_y = y * np.cos(angle) - x * np.sin(angle)
        new_x = x * np.cos(angle) + y * np.sin(angle)
        positions[key] = (new_x, new_y)
    return [positions[key] for key in key_points]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.axis('off')

# Create a list to hold the scatter points
scatters = []
for _ in range(15):
    scat = ax.scatter([], [], c='white', s=50)
    scatters.append(scat)

# Initialize the positions
positions = {key: initial_positions[key] for key in key_points}

# Animation update function
def animate(frame):
    updated_positions = update_bow(frame)
    for i, scat in enumerate(scatters):
        scat.set_offsets([updated_positions[i]])
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 45, 100), interval=50, blit=True)

# Display the animation
plt.show()
