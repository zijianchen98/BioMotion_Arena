
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 7], [3, 2], [3, 8],
    [4, 1], [4, 9], [5, 0], [5, 10], [6, 1], [6, 9], [7, 2], [7, 8]
])

# Function to update the positions of the point lights for each frame
def update(frame_num, positions, points):
    # Simple rolling animation - replace with more complex biomechanical model if needed.
    new_positions = positions + np.array([0.1 * np.sin(frame_num/10), 0.1])
    # Wrap around if points go off screen.
    new_positions[:,0] = np.mod(new_positions[:,0],10)
    new_positions[:,1] = np.mod(new_positions[:,1],10)
    # Update positions of point lights.
    for i in range(len(positions)):
        points[i].set_data(new_positions[i,0], new_positions[i,1])
    return points


# Set up the figure and axes
fig = plt.figure(figsize=(6, 10))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(0, 10), ylim=(0, 10))
ax.set_facecolor('black')

# Create the point light objects
points = []
for i in range(len(positions)):
    point, = ax.plot(positions[i, 0], positions[i, 1], 'wo', markersize=8)
    points.append(point)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(positions, points),
                              frames=200, interval=50, blit=True)

# Show the animation
plt.show()

