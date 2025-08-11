
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
time_steps = 200  # Number of frames in the animation
jump_height = 1.0  # Maximum height of the jump
jump_period = 2 * np.pi  # Period of the jump motion

# Function to calculate the positions of the points at each frame
def points_at_time(t):
    # Define the initial positions of the points for the human figure
    # These would be adjusted to represent the human figure in a jumping pose
    x = np.linspace(-1, 1, 5)  # Horizontal positions of the points
    y = np.zeros_like(x)  # Initial vertical positions

    # Calculate the vertical positions based on a sinusoidal jump motion
    y = jump_height * np.sin(t / jump_period) * np.ones_like(x)

    # Return the positions as a list of tuples
    return list(zip(x, y))

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, jump_height + 1)
ax.set_facecolor('black')  # Set the background color to black
ax.axis('off')  # Hide the axes

# Create a scatter plot for the points
scatter = ax.scatter([], [], s=100, color='white')

# Animation update function
def update(frame):
    positions = points_at_time(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=time_steps, blit=True)

# Display the animation
plt.show()
