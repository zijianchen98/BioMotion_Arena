
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights and their initial positions
num_points = 15
# Define the posture positions representing human joints (simplified for the bowing motion)
initial_positions = np.array([
    [0, 1],    # Head
    [-0.5, 0.5], [0.5, 0.5], # Shoulders
    [-0.5, 0], [0.5, 0],     # Elbows
    [-0.5, -0.5], [0.5, -0.5], # Hands
    [0, 0],  # Spine (pivot point)
    [0, -1], # Hip
    [-0.5, -1.5], [0.5, -1.5], # Knees
    [-0.5, -2], [0.5, -2],     # Feet
])

# Function to create the bowing effect by updating the positions
def update(frame):
    # Update y-coordinates for a bowing motion
    factor = 0.1 * np.sin(frame / 10)  # Variations for bowing
    new_positions = initial_positions.copy()
    # Simulate the bow by adjusting y coordinates
    new_positions[0, 1] -= factor * 0.5  # head
    new_positions[1, 1] -= factor * 0.3  # left shoulder
    new_positions[2, 1] -= factor * 0.3  # right shoulder
    new_positions[-1, 1] -= factor       # hip
    for i in range(3, num_points):
        new_positions[i, 1] -= factor * (i + 1) / 15  # lower points

    point_lights.set_data(new_positions[:, 0], new_positions[:, 1])
    return point_lights,

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # Hide axis

# Create a scatter plot for point-lights
point_lights, = ax.plot([], [], 'o', color='white')

# Set up the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

plt.style.use('dark_background')  # Set a dark background
plt.show()
