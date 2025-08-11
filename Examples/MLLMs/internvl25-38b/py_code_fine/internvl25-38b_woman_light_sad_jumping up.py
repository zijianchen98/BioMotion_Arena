
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions of point-lights for a sadwoman
num_lights = 15
initial_positions = np.array([
    [0.5, 0.0],  # Head
    [0.4, 0.2],  # Left shoulder
    [0.6, 0.2],  # Right shoulder
    [0.35, 0.4], # Left elbow
    [0.65, 0.4], # Right elbow
    [0.4, 0.4],  # Left hip
    [0.6, 0.4],  # Right hip
    [0.2, 0.6],  # Left knee
    [0.8, 0.6],  # Right knee
    [0.1, 0.8],  # Left foot
    [0.9, 0.8],  # Right foot
    [0.5, 0.5],  # Torso center
    [0.45, 0.5], # Left breast
    [0.55, 0.5], # Right breast
    [0.5, 0.7],  # Waist
])

# Define the function to update positions for jumping motion
def update(num, positions, scatter):
    angle = np.sin(num / 10.0) * np.pi / 4  # Vertical displacement for jumping
    positions[:, 1] += 0.05 * np.sin(num / 5.0)  # Bounce effect
    positions[:, 0] += 0.1 * np.sin(num / 15.0)  # Side-to-side movement

    # Ensure the head moves up and down with a sadwoman jumping motion
    positions[0, 1] = 0.0 + 0.1 * np.sin(num / 10.0)

    # Update scatter plot
    scatter.set_offsets(positions)
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=300, fargs=(initial_positions, scatter), interval=50, blit=True)

# Show the plot
plt.show()
