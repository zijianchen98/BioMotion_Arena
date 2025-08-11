
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.0, 0.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define the number of points
num_points = 15

# Initial positions of points (should resemble a sad woman bowing)
# The y-values will be modified to simulate the bowing motion
positions = np.zeros((num_points, 2))
for i in range(num_points):
    positions[i, 0] = np.sin(i * np.pi / 6)  # x-coordinate
    positions[i, 1] = -i / 5  # y-coordinate, starting height

# Create a scatter plot for the points
points, = ax.plot(positions[:, 0], positions[:, 1], 'o', color='white')

# Define the animation function
def update(frame):
    # Simulate the bowing motion by changing the y-values
    bow_angle = 0.05 * np.sin(frame / 10.0)  # Simulated bowing motion over time
    positions[:, 1] += bow_angle  # Increase/decrease the height of points
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

# Show the animation
plt.show()
