
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
FPS = 30  # Frames per second
DURATION = 5  # Duration in seconds
NUM_LIGHTS = 15
WALK_STEPS = 10  # Number of steps in the walking animation

# Define the path (sadman with heavy weight) walking motion
def walk_motion(num_steps):
    x_positions = []
    for i in range(num_steps):
        # Simulate a smooth walking motion
        position = 0 + (np.sin(i / 10 * np.pi) * 2 - 1) * 10
        if i % 2 == 0:
            position += (np.sin(i / 10 * np.pi) * 2 - 1) * 0
        else:
            position -= (np.sin(i / 10 * np.pi) * 2 - 1) * 0
        x_positions.append(position)
    return np.array([x_positions])

# Create the figure and axis
fig, ax = plt.subplots()
ax_size = 10
ax_color = 'w'
background_color = 'k'

# Set up the plot
axs = [walk_motion(WALK_STEPS)
axs = np.repeat(np.expand_dims(x_positions, axis=1), NUM_LIGHTS, axis=1)

# Create the scatter plot
scat = ax.scatter(x=xs[0], y=np.zeros(NUM_LIGHTS), c=on_color, s=on_size, edgecolors='none')

# Function to update the scatter plot for each frame
def update(frame):
    scat.set_offsets(xs[frame % WALK_STEPS])
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=int(FPS * DURATION), interval=1000, blit=True)

# Show or save the animation
plt.show()

# To save the animation, uncomment the following line:
# ani.save('sadman_walking.gif', writer='pillow')
