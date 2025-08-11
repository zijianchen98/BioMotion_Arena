
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = np.array([
    [5, 9], [4, 8], [6, 8], [3, 7], [5, 7], [7, 7],
    [2, 6], [4, 6], [6, 6], [8, 6], [1, 5], [3, 5],
    [5, 5], [7, 5], [9, 5]
])

# Function to update the positions of the points
def update(frame):
    # Calculate new positions based on the frame number
    new_positions = initial_positions + np.sin(frame / 10) * np.array([0, -1])
    
    # Update the positions of the points
    for i, point in enumerate(points):
        point.set_data(new_positions[i][0], new_positions[i][1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
