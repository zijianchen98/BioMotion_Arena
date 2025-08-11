
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
n_points = 15  # Number of points
frame_count = 60  # Total frames in the animation
jump_height = 3  # Max height of the jump
jump_duration = 30  # Frame count for the jumping action

# Points' initial positions (y-coordinates)
initial_heights = np.linspace(-1, 1, n_points)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update each frame of the animation
def update(frame):
    # Calculate the height for the jump gesture
    if frame < jump_duration:
        height = (jump_height * np.sin(np.pi * frame / jump_duration))  # Sine wave for smooth jump
    else:
        height = 0  # In descending motion after the peak

    # Update y-coordinates of the points
    y_data = initial_heights + height
    x_data = np.zeros(n_points)  # x-coordinates remain constant
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frame_count, init_func=init, blit=True, interval=33)

# Show the animation
plt.show()
