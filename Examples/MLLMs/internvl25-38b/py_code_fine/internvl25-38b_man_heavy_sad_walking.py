
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the sadman's model with 15 points (biomechanical model for walking with heavy weight)
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions of the points (adjust as needed for better visual representation)
initial_positions = [
    (0.5, 0.5),  # head
    (0.4, 0.4),  # shoulder left
    (0.6, 0.4),  # shoulder right
    (0.4, 0.3),  # elbow left
    (0.6, 0.3),  # elbow right
    (0.3, 0.2),  # wrist left
    (0.7, 0.2),  # wrist right
    (0.4, 0.2),  # hip left
    (0.6, 0.2),  # hip right
    (0.3, 0.1),  # knee left
    (0.7, 0.1),  # knee right
    (0.2, 0.0),  # ankle left
    (0.8, 0.0),  # ankle right
    (0.1, -0.1), # foot left
    (0.9, -0.1)  # foot right
]
points = np.array(initial_positions)

# Update function for the animation
def update(frame):
    global points
    angle = frame / 20.0
    for i in range(num_points):
        if i in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            points[i, 0] = initial_positions[i][0] + 0.1 * np.sin(angle + i * 0.5)
            points[i, 1] = initial_positions[i][1] + 0.1 * np.cos(angle + i * 0.5)

    line.set_data(points[:, 0], points[:, 1])
    return line,

# Set up the figure for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()
line, = ax.plot([], [], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, blit=True, interval=30)

# Show the animation
plt.show()
