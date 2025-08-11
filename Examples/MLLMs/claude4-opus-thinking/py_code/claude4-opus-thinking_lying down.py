
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Initial positions of the points (representing a man lying down)
# The points can be initialized in a flat, horizontal arrangement.
# Adjust these values to simulate specific joint positions for a lying down action.
initial_positions = np.array([
    [0, 0],  # Head
    [-0.5, -0.5], [0.5, -0.5],  # Shoulders
    [-0.5, -1], [0.5, -1],  # Elbows
    [-0.5, -1.5], [0.5, -1.5],  # Hands
    [-0.3, -2], [0.3, -2],  # Hips
    [-0.2, -3], [0.2, -3],  # Knees
    [-0.1, -4], [0.1, -4],  # Feet
    [0, -5]  # Center point (spine)
])

# Function to update the animation
def update(frame):
    # Clear the previous points
    scat.set_offsets(np.zeros((num_points, 2)))
    
    # Update the positions based on the frame number for realistic motion
    # Here we implement a very basic simulation of lying down motion
    delta_y = 0.02 * np.sin(frame / 10.0)  # Small oscillation to simulate breathing/motion
    new_positions = initial_positions.copy()
    new_positions[:, 1] += delta_y
    
    # Update the scatters with new positions
    scat.set_offsets(new_positions)
    return scat,

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-6, 1)
ax.set_facecolor('black')  # Background color
ax.axis('off')  # Turn off axis

# Create a scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
