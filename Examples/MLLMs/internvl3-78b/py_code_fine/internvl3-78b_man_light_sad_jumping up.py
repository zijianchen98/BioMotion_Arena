
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the frame
frame_size = 10
fig, ax = plt.subplots(figsize=(frame_size, frame_size))
ax.set_xlim(0, frame_size)
ax.set_ylim(0, frame_size)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize point-lights with positions and velocities
num_points = 15
positions = np.random.rand(num_points, 2) * frame_size
velocities = np.random.rand(num_points, 2) * 1.5  # Light weight implies higher speed

# Function to update the animation
def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities
    # Reflect off the walls
    for i in range(num_points):
        for j in range(2):
            if positions[i, j] > frame_size or positions[i, j] < 0:
                velocities[i, j] *= -1
                positions[i, j] = min(max(positions[i, j], 0), frame_size)
    ax.clear()
    ax.set_xlim(0, frame_size)
    ax.set_ylim(0, frame_size)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    for pos in positions:
        ax.plot(pos[0], pos[1], 'wo')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, repeat=True)
plt.show()
