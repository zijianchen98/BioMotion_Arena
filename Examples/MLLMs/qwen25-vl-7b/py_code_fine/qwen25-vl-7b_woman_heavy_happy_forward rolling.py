
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
]

# Define the number of frames
num_frames = 15

# Define the time interval between frames
time_interval = 0.1

# Define the figure size
fig_size = (6, 6)

# Create the figure and axis
fig, ax = plt.subplots(figsize=fig_size)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.axis('off')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the points
def animate(i):
    # Update the positions of the points
    for j in range(len(positions)):
        positions[j][0] += np.sin(2 * np.pi * i / num_frames)
        positions[j][1] += np.cos(2 * np.pi * i / num_frames)
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the updated positions of the points
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_frames, interval=time_interval, repeat=False)

# Display the animation
plt.show()
