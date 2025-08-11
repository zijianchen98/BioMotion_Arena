
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')  # Set background to black
ax.axis('off')  # Turn off the axis

# Initialize point-light positions
# Define starting positions
x_positions = np.array([0, -0.5, 0.5] + [0]*12)
y_positions = np.array([1.5, 0, 0] + [0]*12)

# Create point lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Function to update animation
def update(frame):
    # Smooth forward roll logic
    angle = np.radians(frame * 5)  # Speed of roll
    y_positions[0] -= 0.1  # Move head down
    y_positions[1:] += 0.05  # Move remaining points down
    x_positions[1:] += np.sin(angle) * 0.1  # Simulate sideways roll
    
    # Update the data for points
    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 120), interval=50, blit=True)

# Show the animation
plt.show()
