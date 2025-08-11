
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_points = 15

# Initial positions of point-lights (based on a simple human body structure)
# Example coordinates for 15 points: head, shoulders, elbows, wrists, hips, knees, and feet
initial_positions = np.array([
    [0, 1.8],   # Head
    [-0.2, 1.4], [0.2, 1.4],  # Shoulders
    [-0.3, 1.0], [0.3, 1.0],  # Elbows
    [-0.4, 0.5], [0.4, 0.5],  # Wrists
    [-0.25, 1.0], [0.25, 1.0],  # Hips
    [-0.15, 0.0], [0.15, 0.0],  # Knees
    [-0.1, -0.5], [0.1, -0.5],  # Feet
    [-0.2, 0.2], [0.2, 0.2],   # Body
])

# Create a scatter plot for the point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Update function for the animation
def update(frame):
    # Bowing motion: adjust y-coordinates
    bow_strength = 0.1 * np.sin(frame / 10.0)  # Create a bowing effect
    new_positions = initial_positions.copy()
    # Update y-coordinates to simulate bowing
    new_positions[:, 1] -= bow_strength
    points.set_offsets(new_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# Display the animation
plt.show()
