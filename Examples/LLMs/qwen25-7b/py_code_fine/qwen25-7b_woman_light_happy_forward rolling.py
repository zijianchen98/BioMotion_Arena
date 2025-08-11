
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
positions = np.array([
    [10, 4], [2, 5], (3, 6), (4, 7), (5, 8),
    (6, 9), (7, 10), (8, 12), (9, 13),
    (10, 14), (12, 15), (13, 16), (14, 17), (15, 18), (16, 19)
])

# Define the forward rolling motion
def update_positions(frame):
    # Update the positions to simulate the rolling motion
    for i in range(len(positions)):
        x, y = positions[i]
        new_x = 1 + frame * (i - 1)
        if new_x > 20:
            new_x -= 20
        positions[i] = (new_x, y)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Initialize the scatter plot
scat = ax.scatter(*positions.T, color='white')

# Animation function
def animate(i):
    scat.set_offsets(update_positions(i))
    return scat,

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
