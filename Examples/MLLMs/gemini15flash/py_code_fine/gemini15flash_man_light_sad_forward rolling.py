
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-0.5, 1], [0.5, 1], [0, 0]
])

# Function to update the positions of the point-lights for each frame
def update(frame, points, line):
    # Simulate forward rolling motion (replace with more sophisticated motion model if needed)
    #This is a simplified model.  For a truly realistic rolling motion, more complex physics and biomechanics would be required.
    dt = 0.1  # Time step
    angular_velocity = 0.2 # Adjust to control speed

    # Rotation around the center of mass (approx. [0,2])
    rotation_matrix = np.array([
        [np.cos(angular_velocity * frame * dt), -np.sin(angular_velocity * frame * dt)],
        [np.sin(angular_velocity * frame * dt), np.cos(angular_velocity * frame * dt)]
    ])

    # Apply rotation and translation (to simulate rolling)
    rotated_points = np.dot(points - [0, 2], rotation_matrix) + [0, 2]

    #Linear translation (to simulate rolling)
    rotated_points[:,1] -= angular_velocity * frame * dt

    #Update plot data
    line.set_data(rotated_points[:, 0], rotated_points[:, 1])
    return line,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, points), frames=100, interval=50, blit=True)

# Show the animation
plt.show()

