
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the shape for the body of the woman lying down
body_shape = [
    [9, 5],
    [6, 5],
    [3, 5],
    [0, 7],
    [0, 3],
    [-3, -2],
    [0, -2],
    [0, -4]
]

# Define the head position
head_position = {
    "x": 5,
    "y": 5
}

# Define the duration of one frame in milliseconds
frame_duration_ms = 50

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 15)
ax.set_ylim(0, 15)
ax.set_axis_off()
ax.set_facecolor('black')

points, = ax.plot(range(len(body_shape[0])), [0]*len(body_shape[0]), 'o', color='white')

def update(frame):
    global points, body_shape, head_position

    # Define positions of the body
    positions = [[head_position["x"], head_position["y"]]]

    # Append positions from the body_shape
    for pos in body_shape:
        positions.append([frame * 0.5 + pos[0], frame * 0.02 + pos[1]])

    # Update points
    points.set_data(range(len(positions)), [0]*len(positions))

    # Remove points not in the current positions
    for i in range(len(points)):
        if i < len(positions):
            points.set_data(range(len(positions)), positions)
        else:
            points.set_data(range(len(points)-1), positions[:i])

def animate():
    ani = FuncAnimation(fig, update, frames=np.arange(0, 200, 1/frame_duration_ms), blit=True)
    plt.show()

animate()
