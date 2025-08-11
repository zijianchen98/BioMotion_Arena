
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Function to generate the positions of the point-lights during the bowing motion
def get_bowing_positions(frame, num_frames):
    # Bowing motion parameters:
    # The y-position goes down as the frame increases, simulating a bow
    # The x-positions stay roughly centered and form a shape resembling a person
    bowing_effect = np.clip(1 - frame / num_frames, 0, 1)  # Decrease as animation progresses
    x_positions = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) * 0.1
    y_positions = np.array([1, 1, 1, 0.5, 0.5, 0.5, 0, 0, 0, -0.5, -0.5, -0.5, -1, -1, -1]) * bowing_effect
    return x_positions, y_positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=12)  # white points

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function to update the points
def update(frame):
    x, y = get_bowing_positions(frame, num_frames)
    points.set_data(x, y)
    return points,

# Define number of frames
num_frames = 50

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
