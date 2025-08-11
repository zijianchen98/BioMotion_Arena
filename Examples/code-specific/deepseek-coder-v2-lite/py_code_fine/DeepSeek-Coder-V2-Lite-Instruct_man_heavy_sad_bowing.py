
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1] = 0.5

# Function to update positions
def update_positions(frame_number, positions):
    angle = 2 * np.pi * frame_number / num_frames
    positions[:, 1] = 0.5 + 0.1 * np.sin(angle)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Plot the lights
lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, fargs=(positions,),
                              interval=50, blit=True, repeat=True)

# Display the animation
plt.show()
