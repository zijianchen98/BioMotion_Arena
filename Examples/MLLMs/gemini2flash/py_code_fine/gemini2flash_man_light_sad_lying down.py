
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 4],      # Head
    [-1, 3],   # Left Shoulder
    [1, 3],    # Right Shoulder
    [-2, 2],   # Left Elbow
    [2, 2],    # Right Elbow
    [-3, 1],   # Left Wrist
    [3, 1],    # Right Wrist
    [0, 2],      # Torso Upper
    [0, 1],      # Torso Lower
    [-1, 0],   # Left Hip
    [1, 0],    # Right Hip
    [-1, -1],  # Left Knee
    [1, -1],   # Right Knee
    [-0.5, -2], # Left Ankle
    [0.5, -2]  # Right Ankle
])

# Define the animation function
def animate(i):
    # Define the motion of the point-lights for the 'lying down' action
    # This is a simplified example, you can add more complex movements
    x = initial_positions[:, 0]
    y = initial_positions[:, 1]

    # Add some sinusoidal motion to simulate breathing or slight movements while lying down
    x += 0.1 * np.sin(i * 0.1)
    y += 0.05 * np.cos(i * 0.1)

    # Update the positions of the point-lights
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True, repeat=True)

# Show the animation
plt.show()
