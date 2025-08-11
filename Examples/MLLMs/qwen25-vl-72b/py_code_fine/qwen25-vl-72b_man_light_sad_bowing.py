
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = [
    (0, 4), (-1, 3), (1, 3), (-2, 2), (2, 2),
    (-3, 1), (3, 1), (-4, 0), (4, 0), (-3, -1),
    (3, -1), (-2, -2), (2, -2), (-1, -3), (1, -3)
]

# Set the initial positions of the points
for i, pos in enumerate(initial_positions):
    points[i].set_data(pos)

# Define the update function for the animation
def update(frame):
    # Calculate new positions based on the bowing motion
    angle = frame / 10
    new_positions = []
    for x, y in initial_positions:
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        new_positions.append((new_x, new_y))
    
    # Update the positions of the points
    for i, pos in enumerate(new_positions):
        points[i].set_data(pos)
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
