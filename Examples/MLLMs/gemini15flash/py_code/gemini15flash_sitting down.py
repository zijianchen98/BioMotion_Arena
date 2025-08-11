
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5],  [ -1, 4], [0, 4], [1, 4],
    [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2],
    [0, 1], [ -0.5, 0], [0.5, 0]
])


# Define a function to update the positions of the point-lights for each frame
def update_positions(frame_num, points, line_collections):
    # Simple example: Circular motion
    angle = frame_num * 0.1  # Adjust speed here

    # Adjust the positions for sitting down animation
    new_positions = np.copy(initial_positions)
    new_positions[:, 1] -= 0.5*np.sin(angle + np.linspace(0, np.pi, 15))  # Vertical movement
    new_positions[:,0] += 0.3*np.cos(angle + np.linspace(0, np.pi, 15)) # slight horizontal swaying


    for i, lc in enumerate(line_collections):
        lc.set_offsets(new_positions)
    return line_collections


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-1, 7])
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the point-lights (scatter plot)
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(
    fig, update_positions, fargs=(initial_positions, [points]),
    frames=100, interval=50, blit=True, repeat=True
)


# Show the animation
plt.show()

