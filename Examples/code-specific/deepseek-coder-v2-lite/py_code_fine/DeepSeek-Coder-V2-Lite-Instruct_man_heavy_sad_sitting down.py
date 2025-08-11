
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-0.5, 0.5, num_lights)
positions[:, 1] = 0.5

# Function to update positions
def update_positions(frame_number, positions):
    # Simple sine wave motion for the lights
    phase = frame_number / 20.0
    positions[:, 1] = 0.5 + 0.1 * np.sin(positions[:, 0] + phase)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, fargs=(positions,), interval=50, blit=True)

# Show the animation
plt.show()
