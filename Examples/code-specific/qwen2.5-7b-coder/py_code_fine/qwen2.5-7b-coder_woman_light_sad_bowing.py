
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
frames = 60
width, height = 800, 600
frame_duration = 100  # milliseconds

# Initialize the positions of the points
positions = np.random.rand(num_points, 2) * [width, height]

# Define the function to update the positions
def update(frame):
    global positions
    # Apply some simple physics to make the points move realistically
    velocities = np.zeros_like(positions)
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                dx, dy = positions[j] - positions[i]
                dist = np.sqrt(dx**2 + dy**2)
                if dist < 50:
                    force = 0.01 / dist**2
                    velocities[i] += force * np.array([dx, dy])
    positions += velocities * frame_duration / 1000
    
    # Keep the points within the bounds of the screen
    positions[:, 0] = np.clip(positions[:, 0], 0, width)
    positions[:, 1] = np.clip(positions[:, 1], 0, height)
    
    # Draw the updated positions
    scatter.set_offsets(positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_facecolor('black')
scatter = ax.scatter([], [], s=50, c='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=frame_duration)

plt.show()
