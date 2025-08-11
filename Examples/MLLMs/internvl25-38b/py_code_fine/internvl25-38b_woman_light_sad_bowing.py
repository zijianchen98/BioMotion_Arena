
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Initialize position arrays
positions = np.zeros((num_points, 2))

# Define the frame rate
frame_rate = 60
num_frames = 100

# Function to update the positions for bowing motion
def update_positions(frame):
    t = 2 * np.pi * frame / num_frames
    for i in range(num_points):
        positions[i, 0] = i * 0.1
        positions[i, 1] = np.sin(t) * (num_points - i) * 0.1 - 5 + i * 0.1
    return positions

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, num_points)
ax.set_ylim(-10, 10)
ax.axis('off')

# Create point-light scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Animation function
def animate(frame):
    new_positions = update_positions(frame)
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
 ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000.0 / frame_rate, blit=True)

# Display the animation
plt.show()
