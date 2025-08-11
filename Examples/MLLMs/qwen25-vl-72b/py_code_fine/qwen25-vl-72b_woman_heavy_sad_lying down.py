
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = np.array([
    [5, 8], [4, 7], [6, 7], [3, 6], [5, 6], [7, 6],
    [2, 5], [4, 5], [6, 5], [8, 5], [3, 4], [5, 4], [7, 4],
    [4, 3], [6, 3]
])

# Function to update the positions of the points
def update(frame):
    # Update the positions of the points based on the specified action
    new_positions = initial_positions + np.random.normal(0, 0.1, initial_positions.shape)
    
    # Ensure the points stay within the bounds of the plot
    new_positions[:, 0] = np.clip(new_positions[:, 0], 0, 10)
    new_positions[:, 1] = np.clip(new_positions[:, 1], 0, 10)
    
    # Update the positions of the points in the plot
    for i, point in enumerate(points):
        point.set_data(new_positions[i, 0], new_positions[i, 1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
