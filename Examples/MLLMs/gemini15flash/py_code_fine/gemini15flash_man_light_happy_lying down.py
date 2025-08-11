
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Define a function to update the positions of the point-lights for each frame

def update_positions(frame_num, points, positions):
    # Simulate a simple rolling motion
    new_positions = positions.copy()
    for i in range(len(positions)):
        x, y = new_positions[i]
        x += np.sin(frame_num * dt + i) * 0.05  # Adjust for different speeds
        y += np.cos(frame_num * dt + i) * 0.05  # Adjust for different speeds
        if i < 7:
          x += np.sin(frame_num * dt + 2*i) * 0.1  # more random motion for the top points
          y += np.cos(frame_num * dt + 2*i) * 0.1

        new_positions[i] = [x, y]
    for point, xy in zip(points, new_positions):
        point.set_data(xy[0], xy[1])
    return points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 15])
ax.set_ylim([-5, 15])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-lights
points = [ax.plot([], [], 'wo')[0] for _ in range(15)]


# Create the animation
ani = animation.FuncAnimation(
    fig, update_positions, frames=num_frames, fargs=(points, initial_positions), interval=50, blit=True
)

# Show the animation
plt.show()

