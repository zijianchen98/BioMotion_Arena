
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
n_points = 15
frames = 100
weight_offset = 0.5  # Adjust this value to simulate the heavy weight

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')

# Create a set of initial points for the happy man's body
points = np.zeros((n_points, 2))
points[:, 0] = np.random.uniform(-0.5, 0.5, n_points)  # X coordinates
points[:, 1] = np.linspace(-2.5, 2.5, n_points)  # Y coordinates

# Create scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update the points for each frame
def update(frame):
    global points
    # Simulate a running motion with a sine wave
    for i in range(n_points):
        points[i, 0] += 0.1 * np.cos(frame / 10.0)  # Movement in x-direction
        points[i, 1] += np.sin(frame / 10.0) * weight_offset  # Movement in y-direction
    # Keep the points in the bounds
    points = np.clip(points, -3, 3)
    sc.set_offsets(points)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

# Display the animation
plt.show()
