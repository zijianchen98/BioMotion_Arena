
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
lights = np.array([
    [-0.3, 0.2],  # Head
    [-0.2, 0.3],  # Right shoulder
    [-0.2, 0.1],  # Left shoulder
    [-0.1, 0.3],  # Right elbow
    [-0.1, 0.1],  # Left elbow
    [0.0, 0.3],   # Right wrist
    [0.0, 0.1],   # Left wrist
    [-0.3, 0.0],  # Hip
    [-0.1, 0.2],  # Right knee
    [-0.1, -0.2],  # Left knee
    [0.1, 0.2],   # Right ankle
    [0.1, -0.2],  # Left ankle
    [-0.2, -0.1],  # Right toe
    [-0.2, 0.1],  # Left toe
    [0.0, -0.2],  # Body center
])

# Define the motion parameters
frames = 100
roll_angle = np.linspace(0, 2*np.pi, frames)
roll_radius = 0.2

# Create a new figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the plot with the initial positions of the point-lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], color='white', s=10)

# Function to update the plot at each frame
def update(frame):
    global scatter
    scatter.remove()
    
    # Calculate the new positions of the point-lights
    new_positions = np.copy(lights)
    new_positions[:, 0] += roll_radius * np.cos(roll_angle[frame])
    new_positions[[1, 2, 4, 5, 7, 9, 11, 13], 0] -= roll_radius * np.cos(roll_angle[frame]) * 0.5
    new_positions[[3, 6, 8, 10, 12, 14], 0] -= roll_radius * np.cos(roll_angle[frame]) * 0.8
    new_positions[:, 1] += roll_radius * np.sin(roll_angle[frame])
    new_positions[[1, 2, 4, 5, 7, 9, 11, 13], 1] -= roll_radius * np.sin(roll_angle[frame]) * 0.5
    new_positions[[3, 6, 8, 10, 12, 14], 1] -= roll_radius * np.sin(roll_angle[frame]) * 0.8
    
    # Plot the new positions of the point-lights
    scatter = ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
