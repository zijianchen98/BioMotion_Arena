
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0.5, 3], [1.5, 3], [2.5, 3],
    [1, 2], [2, 2],
    [1, 1], [2, 1],
    [1.5, 0], [1, -1], [2, -1]

])


# Define a function to update the positions of the point lights for each frame
def update(frame, points, line):
    #Simulate walking motion.  This is a simple example and can be greatly expanded
    #for more realistic motion.
    x_offset = np.sin(frame * 0.1) * 0.5
    y_offset = np.cos(frame * 0.1) * 0.2
    new_positions = initial_positions + np.array([x_offset, y_offset])
    
    points.set_offsets(new_positions)
    return points,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-2, 5])  # Adjust x-axis limits as needed
ax.set_ylim([-3, 7])  # Adjust y-axis limits as needed
ax.set_aspect('equal') # Ensure circles are circular.
ax.set_facecolor('black')  #Set background to black

# Create the point lights
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(
    fig, update, fargs=(points, ), frames=range(200), interval=50, blit=True
)

# Show the animation
plt.show()

