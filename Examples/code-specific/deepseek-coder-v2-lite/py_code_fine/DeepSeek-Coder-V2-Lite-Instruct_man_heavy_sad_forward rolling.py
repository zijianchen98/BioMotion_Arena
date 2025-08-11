
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-1, 1, num_lights)
positions[:, 1] = 1

# Define the motion
def update_positions(frame_number, positions):
    # Sadman rolling forward
    angle = (frame_number / num_frames) * np.pi
    positions[:, 0] = np.sin(angle) * positions[:, 0]
    positions[:, 1] -= 0.02  # Slight downward movement
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis

# Initialize the scatter plot for the lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*100, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(positions,), frames=num_frames, interval=50, blit=False, repeat=True)

# Show the animation
plt.show()
