
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=6)

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.0, 0.9],    # Head
    [-0.2, 0.7],   # Left Shoulder
    [0.2, 0.7],    # Right Shoulder
    [-0.3, 0.5],   # Left Elbow
    [0.3, 0.5],    # Right Elbow
    [-0.4, 0.3],   # Left Hand
    [0.4, 0.3],    # Right Hand
    [-0.1, 0.5],   # Left Hip
    [0.1, 0.5],    # Right Hip
    [-0.2, 0.2],   # Left Knee
    [0.2, 0.2],    # Right Knee
    [-0.3, 0.0],   # Left Foot
    [0.3, 0.0],    # Right Foot
    [-0.0, 0.45],  # torso top
    [0.0, 0.05]    # torso bottom
])

# Define the animation function
def animate(i):
    # Define the jumping motion
    vertical_amplitude = 0.1
    horizontal_amplitude = 0.05
    frequency = 3  # Adjust for speed of jumping

    # Calculate the vertical and horizontal displacement for each point
    vertical_displacement = vertical_amplitude * np.sin(2 * np.pi * frequency * i / 100)
    horizontal_displacement = horizontal_amplitude * np.cos(2 * np.pi * frequency * i / 100)

    # Update the positions of the point-lights
    x = initial_positions[:, 0] + horizontal_displacement * initial_positions[:, 0] 
    y = initial_positions[:, 1] + vertical_displacement

    # Set the data for the point-lights
    points.set_data(x, y)

    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.show()
