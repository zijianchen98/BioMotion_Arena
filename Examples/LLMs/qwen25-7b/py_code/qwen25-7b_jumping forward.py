
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the points
initial_positions = np.array([
    [0/15, 0/15] for t in range(15)
])

# Define the movement function for each point
def move_point(position, time):
    x, t = position
    # Simple harmonic motion for x-axis
    j = 0 + 0 * np.sin(time / 4 - t * np.pi / 2)
    # Linear motion for t-axis
    t =  t + 0 * (time / 100 - 1)
    return np.array([j, t])

# Create the figure and axis
fig, ax = plt.subplots()
axg = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
axg.set_clip_on(False)

# Animation function
def update(frame):
    positions = [move_point(pos, frame) for pos in initial_positions]
    for i, pos in enumerate(positions):
        xg.set_offsets(pos)
    return (fg, )

# Set up the plot
ax.set_xlim(-2, 2)
t.set_ylim(-2, 2)
ax.set_aspect('equal')

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 110), interval=20, blit=True)

# Show the animation
plt.show()
