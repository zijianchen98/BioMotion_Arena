
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 4], [-1, 3], [0, 3], [1, 3],
    [-1, 2], [0, 2], [1, 2],
    [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1],
    [-1, 0], [1, 0],
    [0, -1]
])


# Define the movement function for sitting down
def sit_down_motion(t):
    y_offset = -t**2 + 2*t # Represents the downwards curve of the sit motion
    x_offset = np.zeros_like(t) # No horizontal movement.

    offsets = np.column_stack([x_offset, y_offset])

    modified_positions = initial_positions.astype(float)
    
    # Apply offset based on body part 
    modified_positions[:, 1] += y_offset[:, np.newaxis] / initial_positions[:, 1][:, np.newaxis]
    
    # Add some slight leg movement
    modified_positions[12, 0] = -1 + 0.2 * np.sin(t * np.pi)
    modified_positions[13, 0] = 1 + 0.2 * np.sin(t * np.pi)
    modified_positions[14, 0] = 0.1 * np.sin(t * np.pi)

    return modified_positions


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])  # Adjust limits for visibility
ax.set_ylim([-2, 5])
ax.set_aspect('equal') # Ensure correct aspect ratio 
ax.set_facecolor('black')  # Set background color
scatter = ax.scatter([], [], s=30, c='white')  # Initialize scatter plot


# Define the animation function
def animate(i):
    t = i * 0.05
    positions = sit_down_motion(np.array([t]))[0]  # Calculate positions at time t
    scatter.set_offsets(positions)  # Update the scatter plot
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=50, blit=True)  # Adjust frames and interval for desired speed

plt.show()

