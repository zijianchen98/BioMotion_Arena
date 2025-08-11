
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the joints for the initial frame.
# The array should have 15 columns: left ear, right ear, left eye, right eye, 
# nose, left shoulder, right shoulder, left elbow, right elbow, left wrist, 
# right wrist, left hip, right hip, left knee, right knee, left ankle, right ankle.
initial_positions = np.array([
    [-2, -2, -0.25],
    [2, -2, 0.25],
    [0, -0.5, -0.25],
    [0, -0.5, 0.25],
    [0, -0.25, 0],
    [1, 2, -1],
    [-1, 2, 1],
    [1, 1.5, -0.5],
    [-1, 1.5, 0.5],
    [0, 1, -0.3],
    [0, 1, 0.3],
    [0, 0.5, -0.75],
    [0, 0.5, 0.75],
    [0, 0.25, -0.5],
    [0, 0.25, 0.5],
])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_aspect('equal')
ax.axis('off')

# Remove the axis labels
ax.axis('off')

# Function to update positions
def update_positions(frame_count):
    global initial_positions
    total_movements = frame_count // 20
    positions = initial_positions + total_movements * np.array([
        [0.1, 0, -0.1, 0, 0, 0.1, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.2, 0.2, 0, 0, 0.1, 0.1, 0.1, 0, -0.2, -0.2, 0.1, 0.1, 0.1],
        [0, 0, 0, 0, 0, 0, -0.1, -0.1, -0.1, 0, 0.2, 0.2, -0.1, -0.1, -0.1],
        [0, 0, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0],
        [1, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, -1, 0, 1, 0],
        [-1, 0, 0, 0, 1, 0, 0, -1, 0, 1, 0, 1, 0, -1, 0],
        [0, 0, 0.3, 0.3, 0, 0, 0.2, 0.2, 0.2, -0.3, 0, -0.2, 0.2, 0.2, 0.2],
        [0, 0, 0, 0, 0, 0, -0.2, -0.2, -0.2, 0.3, 0, 0.2, -0.2, -0.2, -0.2],
        [0, 0, 0, 0, 0, 0.3, 0.3, 0, 0, 0, 0, 0, -0.3, -0.3, 0],
        [1, 0.5, 0, 0, -1, 0, 0, 1, 0, -1, 0, -1, 0, 1, 0],
        [-1, 0.5, 0, 0, 1, 0, 0, -1, 0, 1, 0, 1, 0, -1, 0],
        [0, 0.4, 0.4, 0, 0, 0.4, 0.4, 0, 0, 0, 0, 0, 0.4, 0.4, 0],
        [0, 0.4, -0.4, 0, 0, -0.4, -0.4, 0, 0, 0, 0, 0, -0.4, -0.4, 0],
        [0, 0.2, 0.2, 0, 0, 0, 0.2, 0.2, 0, 0, 0, 0, -0.2, -0.2, 0],
        [0, 0.2, -0.2, 0, 0, 0, -0.2, -0.2, 0, 0, 0, 0, 0.2, 0.2, 0]
    ])
    return positions

# Draw the animation
def animate(frame):
    positions = update_positions(frame)
    line_set.set_data(positions[:, 0], positions[:, 1])
    return line_set,

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=600, interval=50, blit=True)

# Display the plot
plt.show()
