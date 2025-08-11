
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the positions of the points
num_frames = 100
positions = np.zeros((num_frames, 15, 2))

# Define the initial position of the points
initial_positions = np.array([
    [0.2, 0.8], [0.4, 0.9], [0.6, 0.9], [0.8, 0.8],
    [0.3, 0.7], [0.5, 0.8], [0.7, 0.8], [0.9, 0.7],
    [0.4, 0.6], [0.6, 0.6],
    [0.3, 0.5], [0.5, 0.5], [0.7, 0.5], [0.9, 0.5],
    [0.5, 0.4]
])

# Define the movement of the points
for i in range(num_frames):
    if i < num_frames / 2:
        positions[i] = initial_positions + i * 0.01
    else:
        positions[i] = initial_positions + (num_frames - i) * 0.01

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create a scatter plot for the points
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white')

# Define the update function for the animation
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
