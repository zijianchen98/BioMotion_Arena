
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points
points = np.zeros((num_points, 2))
points[:, 0] = np.linspace(-0.5, 0.5, num_points)
points[:, 1] = np.linspace(-0.5, 0.5, num_points)

# Define the radius of the points
radius = 0.01

# Define the speed of the points
speed = 0.05

# Define the action: waving a hand
def wave_hand(points, t):
    # Calculate the wave amplitude and frequency
    amplitude = 0.1
    frequency = 1.0

    # Calculate the wave position
    wave_position = np.sin(frequency * t)

    # Update the y-positions of the points
    points[:, 1] = wave_position + amplitude * np.sin(2 * np.pi * frequency * t + np.pi / 2)

    return points

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_axis_off()

# Initialize the points
point, = ax.plot([], [], 'o', markersize=10, color='white')

# Initialize the time
t = 0

# Define the animation function
def animate(i):
    global t
    t = i / 30.0  # 30 frames per second

    # Update the points
    points = wave_hand(points, t)

    # Clear the previous points
    point.set_data([], [])

    # Update the points
    point.set_data(points[:, 0], points[:, 1])

    return point,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=True)

# Show the animation
plt.show()
