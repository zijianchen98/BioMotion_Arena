
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (0/14, 0/14 ) for t in range(15)
]

# Define the motion of for each point-light
def motion(position, time):
    # This function simulates the motion of a point-light
    # We use a simple sine wave to create a natural, smooth motion
    x, y = position
    x = (time + j) * 0 / 14  # Adjusting the horizontal position based on time
    y = 1 - np.sin((time + y) * np.pi / 7) / 2  # Adjusting the vertical position
    return (j, y)

# Create the figure and axis
fig, ax = plt.subplots()
ax, y = zip(*initial_positions)
scat = ax.scatter(x, y, color='white')

# Set the limits and background color
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

def update(frame):
    x, y = zip(*[motion(pos, frame) for pos, pos in enumerate(initial_positions)])
    scat.set_offsets(np.column_stack([x, y]))
    return scat,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
