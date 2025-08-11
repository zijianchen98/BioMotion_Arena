
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 4)

# Initialize the point-lights
points = ax.scatter([], [], color='white', s=100)

# Define the positions of the point-lights
def init():
    points.set_offsets([])
    return points,

def update(frame):
    # Define the positions of the point-lights
    positions = np.array([[0, 3], [-0.5, 2.5], [0, 2], [0.5, 2.5], [1, 3],
                          [-1, 2], [-0.5, 1.5], [0, 1], [0.5, 1.5], [1, 2],
                          [-1, 1], [-0.5, 1], [0, 0.5], [0.5, 1], [1, 1]])
    positions[:, 0] += 0.1 * frame
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 15), init_func=init, blit=True, repeat=True)

# Set up the background to be black
ax.set_facecolor('black')

# Show the animation
plt.show()
