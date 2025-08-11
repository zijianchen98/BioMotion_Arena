
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate point-light positions for the forward roll action
def get_positions(frames):
    # Starting positions for a forward roll
    x = np.array([0, -0.2, 0.2, -0.1, 0.1, -0.15, 0.15, 0, 0, 0, 0, 0, 0, 0, 0])
    y = np.array([0, 0.5, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.4, -0.5])

    # Update positions for the animation
    movements = np.zeros((frames, len(x), 2))
    for i in range(frames):
        angle = -np.pi / (frames - 1) * i  # Forward roll motion
        for j in range(len(x)):
            movements[i, j, 0] = x[j] * np.cos(angle) - y[j] * np.sin(angle)
            movements[i, j, 1] = x[j] * np.sin(angle) + y[j] * np.cos(angle)
    return movements

# Animation Configuration
frames = 100
positions = get_positions(frames)

# Create a figure for the animation
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.6, 0.1)
ax.axis('off')  # Turn off the axis

# Create an empty list to hold the point-light objects
points = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(len(positions[0]))]

# Animation function to update positions for each frame
def update(frame):
    for point, pos in zip(points, positions[frame]):
        point.set_data(pos[0], pos[1])
    return points

# Create the animation using the FuncAnimation class
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Display the animation
plt.show()
