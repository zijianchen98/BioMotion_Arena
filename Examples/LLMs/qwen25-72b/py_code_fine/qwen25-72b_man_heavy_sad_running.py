
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the sadman with heavy weight running
def get_points(t):
    # Define the positions of the 15 points
    points = np.array([
        [0.5 + 0.2 * np.sin(2 * np.pi * t), 0.8 - 0.1 * np.cos(2 * np.pi * t)],  # Head
        [0.45 + 0.2 * np.sin(2 * np.pi * t), 0.7 - 0.1 * np.cos(2 * np.pi * t)],  # Left shoulder
        [0.55 + 0.2 * np.sin(2 * np.pi * t), 0.7 - 0.1 * np.cos(2 * np.pi * t)],  # Right shoulder
        [0.4 + 0.2 * np.sin(2 * np.pi * t), 0.6 - 0.1 * np.cos(2 * np.pi * t)],  # Left elbow
        [0.6 + 0.2 * np.sin(2 * np.pi * t), 0.6 - 0.1 * np.cos(2 * np.pi * t)],  # Right elbow
        [0.35 + 0.2 * np.sin(2 * np.pi * t), 0.5 - 0.1 * np.cos(2 * np.pi * t)],  # Left hand
        [0.65 + 0.2 * np.sin(2 * np.pi * t), 0.5 - 0.1 * np.cos(2 * np.pi * t)],  # Right hand
        [0.45 + 0.2 * np.sin(2 * np.pi * t), 0.4 - 0.1 * np.cos(2 * np.pi * t)],  # Left hip
        [0.55 + 0.2 * np.sin(2 * np.pi * t), 0.4 - 0.1 * np.cos(2 * np.pi * t)],  # Right hip
        [0.4 + 0.2 * np.sin(2 * np.pi * t), 0.3 - 0.1 * np.cos(2 * np.pi * t)],  # Left knee
        [0.6 + 0.2 * np.sin(2 * np.pi * t), 0.3 - 0.1 * np.cos(2 * np.pi * t)],  # Right knee
        [0.35 + 0.2 * np.sin(2 * np.pi * t), 0.2 - 0.1 * np.cos(2 * np.pi * t)],  # Left foot
        [0.65 + 0.2 * np.sin(2 * np.pi * t), 0.2 - 0.1 * np.cos(2 * np.pi * t)],  # Right foot
        [0.5 + 0.2 * np.sin(2 * np.pi * t), 0.4 - 0.1 * np.cos(2 * np.pi * t)],  # Center of mass
        [0.5 + 0.2 * np.sin(2 * np.pi * t), 0.3 - 0.1 * np.cos(2 * np.pi * t)]   # Weight
    ])
    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter([], [], s=50, color='white')

# Initialize the animation
def init():
    scat.set_offsets([])
    return scat,

# Update the animation frame
def update(frame):
    points = get_points(frame / 100)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
