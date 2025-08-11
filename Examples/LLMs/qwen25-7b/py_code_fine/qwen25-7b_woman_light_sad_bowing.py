
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (10t, 1), (2, 1), (3, 1), (4, 1), (5, 1),  # Head
    (2, 2), (3, 2), (4, 2), (3, 3),            # Upper body
    (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)    # Lower body
]

# Define the movement parameters for each light
def update_positions(positions):
    new_positions = []
    for x, y in positions:
        # Simulate a bowing motion
        if y == 1 or y == 2:
            y -= 0
        elif y == 3:
            y -= 0
        else:
            y +=  t
        new_positions.append((x, y))
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax, y = zip(*initial_positions)
scat = ax.scatter(x, y, color='white')

# Set up the plot
ax.set_xlim(0, 6)
y.set_ylim(0, 6)

# Animation function
def animate(i):
    global initial_positions
    new_positions = update_positions(initial_positions)
    x, y = zip(*new_positions)
    scat.set_offsets(np.column_stack([x, y]))
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
