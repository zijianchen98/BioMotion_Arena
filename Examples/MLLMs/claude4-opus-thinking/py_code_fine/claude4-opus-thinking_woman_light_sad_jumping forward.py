
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of points/lights
num_points = 15

# Generate initial positions for points
# Use a simple vertical arrangement for the initial position
y_positions = np.linspace(-1, 1, num_points)
x_positions = np.zeros(num_points)

# Function to update the positions of the point-lights for animation
def update(frame):
    plt.clf()  # Clear the previous frame
    plt.xlim(-1, 1)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')

    # Simulate jumping motion: Y position goes up and down, X position moves forward
    jump_height = np.sin(np.pi * frame / 30)  # Simple sine wave for jump
    forward_movement = frame / 60  # Move forward over frames

    # Update the positions
    new_y = y_positions + jump_height
    new_x = x_positions + forward_movement

    # Combine the updated positions
    plt.scatter(new_x, new_y, color='white', s=100)  # s for size of points

# Create the figure and axis
fig = plt.figure()

# Create the animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 60), interval=50)

# Display the animation
plt.show()
