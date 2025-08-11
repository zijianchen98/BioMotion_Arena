
import matplotlib.pyplot as plt
import numpy as np
import time

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect(1)
ax.set_axis_off()

# Create 15 point-light stimuli
points = ax.scatter(np.random.rand(15), np.random.rand(15), color='white', s=80)

# Define the movement function
def update(frame):
    global points
    # Update points for 15 points
    new_x = np.random.rand(15)
    new_y = (new_y_1 := np.random.rand(15)) + (new_y_2 := np.random.rand(15))
    points.set_offsets(np.column_stack([new_x, new_y]))
    return points,

# Create an animation object using the update function
animation = FuncAnimation(fig, update, frames=range(50), blit=True)

# Display the animation
plt.show()
