
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Initial positions of the points (as white points on a black background)
x = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
y = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')

# Create the scatter plot
scat = ax.scatter(x, y, c='white', s=100)

def update(frame):
    global x, y
    # Define the jumping motion
    if frame < 20:
        y = [pos + np.sin(frame/10) * 0.4 for pos in y]
    elif frame < 40:
        y = [pos - np.sin((frame-20)/10) * 0.4 for pos in y]
    else:
        x = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        y = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    
    # Update the scatter plot
    scat.set_offsets(np.c_[x, y])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=100)

# Display the animation
plt.show()
