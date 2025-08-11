
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


# Function to update the positions of the point-lights for each frame
def update(frame):
    global initial_positions
    x_positions = initial_positions[:, 0] + 2*np.sin(0.2*frame + np.linspace(0, 2*np.pi, 15))
    y_positions = initial_positions[:, 1] + frame*0.5 - 2*np.cos(0.1*frame + np.linspace(0, 2*np.pi, 15))
    
    #keep the y positions in range
    y_positions = np.clip(y_positions, -5, 10)


    scat.set_offsets(np.column_stack((x_positions, y_positions)))
    return scat,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the scatter plot of point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)


# Save the animation as a GIF (optional)
ani.save('biological_motion.gif', writer='imagemagick')


# Show the animation
plt.show()

