
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points for the point-light display
num_points = 15

# Define the coordinates of the point-lights
def initialize_points():
    # y-coordinates approximating human body posture in a sad walking pose
    y_positions = np.array([-1, -0.8, -1.2, -1.0, -0.7, -1.1, -0.5, -1.3, -0.6, -1.4, -0.5, -0.9, -0.2, -0.3, -1.5])
    x_positions = np.array([0, -0.2, 0.2] * 5)  # Spread points along vertical and horizontal
    return x_positions, y_positions

# Update function for the animation
def update(frame):
    global x_positions, y_positions
    plt.cla()  # Clear the previous frame
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axis('off')  # Turn off the axes

    # Calculate new positions for the point-lights for walking motion
    # Simple walking animation (y decreases to simulate leg movement)
    y_positions -= 0.05 if frame % 2 == 0 else -0.02
    y_positions[::2] += 0.02  # Alternate the walking steps

    # Draw the points
    plt.scatter(x_positions, y_positions, color='white')

# Create plot
fig = plt.figure()
x_positions, y_positions = initialize_points()

# Set a black background
fig.patch.set_facecolor('black')

# Animate
ani = animation.FuncAnimation(fig, update, frames=60, interval=50)

# Show the animation
plt.show()
