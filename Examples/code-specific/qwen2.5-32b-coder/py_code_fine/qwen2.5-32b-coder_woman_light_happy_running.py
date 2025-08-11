
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Initialize positions for the point lights (these are simplified and may need refinement)
# These coordinates are just a starting point and should be refined for a more accurate representation
initial_positions = np.array([
    [0.1, 0.8],  # Head
    [0.2, 0.7],  # Right Shoulder
    [0.4, 0.6],  # Right Elbow
    [0.6, 0.7],  # Right Wrist
    [0.8, 0.8],  # Left Shoulder
    [1.0, 0.7],  # Left Elbow
    [1.2, 0.8],  # Left Wrist
    [0.4, 0.4],  # Right Hip
    [0.6, 0.3],  # Right Knee
    [0.8, 0.4],  # Right Ankle
    [0.4, 0.1],  # Right Foot
    [1.0, 0.4],  # Left Hip
    [1.2, 0.3],  # Left Knee
    [1.4, 0.4],  # Left Ankle
    [1.4, 0.1]   # Left Foot
])

# Define the trajectory function for each point light
def trajectory(t, index):
    x, y = initial_positions[index]
    # Simple sinusoidal motion to simulate running
    if index in [1, 3, 5, 7, 9, 11, 13]:  # Arms and Legs
        x += 0.1 * np.sin(2 * np.pi * (t / 100 + index * 0.1))
        y += 0.1 * np.cos(2 * np.pi * (t / 100 + index * 0.1))
    elif index in [0, 8, 10, 12, 14]:  # Body parts
        y -= 0.05 * np.sin(2 * np.pi * (t / 100 + index * 0.1))
    return x, y

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, color='white')

# Update function for the animation
def update(frame):
    positions = np.array([trajectory(frame, i) for i in range(num_lights)])
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True, interval=50)

# Show the plot
plt.show()
