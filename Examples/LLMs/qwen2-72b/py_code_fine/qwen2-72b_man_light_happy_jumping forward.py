
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the positions of the points
num_frames = 100
num_points = 15
positions = np.zeros((num_frames, num_points, 2))

# Define the initial positions of the points in a "happy man" configuration
initial_positions = np.array([
    [0.4, 0.8], [0.6, 0.8], [0.5, 0.7], [0.4, 0.6], [0.6, 0.6],
    [0.3, 0.5], [0.7, 0.5], [0.5, 0.4], [0.4, 0.3], [0.6, 0.3],
    [0.3, 0.2], [0.7, 0.2], [0.5, 0.1], [0.4, 0.0], [0.6, 0.0]
])

# Define the motion parameters for each point
velocities = np.random.uniform(-0.01, 0.01, size=(num_points, 2))
accelerations = np.random.uniform(-0.001, 0.001, size=(num_points, 2))

# Set the initial positions
positions[0] = initial_positions

# Update the positions over time
for i in range(1, num_frames):
    positions[i] = positions[i-1] + velocities + accelerations
    velocities += accelerations

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')

# Create a scatter plot for the points
scatter = ax.scatter(positions[0][:, 0], positions[0][:, 1], c='white')

# Function to update the scatter plot at each frame
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
