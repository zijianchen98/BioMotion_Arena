
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
num_frames = 60
data = np.zeros((num_frames, 15, 2))

# Example: Head movement (point 0)
data[:, 0, 0] = np.linspace(0, 100, num_frames)
data[:, 0, 1] = np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 10 + 150

# Example: Other body parts (points 1-14)
for i in range(1, 15):
    data[:, i, 0] = data[:, 0, 0] + np.random.rand(num_frames) * 20 - 10  # Add some offset from the head
    data[:, i, 1] = data[:, 0, 1] + np.random.rand(num_frames) * 20 - 10

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 200)  # Adjust limits as needed
ax.set_ylim(-50, 200)
ax.set_facecolor('black')

# Initialize the points
points = ax.plot([], [], 'wo', markersize=5)[0]

# Animation update function
def update(frame):
    x = data[frame, :, 0]
    y = data[frame, :, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Display the animation (optional, depending on your environment)
plt.show()

# Save the animation (optional)
# ani.save('biological_motion.gif', writer='imagemagick')  # Requires imagemagick

