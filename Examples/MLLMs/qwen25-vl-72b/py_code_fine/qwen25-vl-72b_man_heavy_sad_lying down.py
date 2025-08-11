
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = np.array([
    [5, 8], [4, 7], [6, 7], [3, 6], [5, 6], [7, 6],
    [2, 5], [4, 5], [6, 5], [8, 5], [3, 4], [5, 4], [7, 4],
    [4, 3], [6, 3]
])

# Function to update the positions of the points
def update(frame):
    # Calculate new positions based on the lying down motion
    new_positions = initial_positions + np.array([np.sin(frame / 10), -np.cos(frame / 10)]) * 0.1
    
    # Update the positions of the points
    for i, point in enumerate(points):
        point.set_data(new_positions[i])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
