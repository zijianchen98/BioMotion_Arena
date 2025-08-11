
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
    for i in range(num_lights):
        positions[i, 1] -= 0.02  # Move down slowly
        if positions[i, 1] < -0.5:
            positions[i, 1] = 0.5  # Reset position when out of bounds

    return positions,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis

# Plot the lights
points, = ax.plot([], [], 'wo', markersize=light_radius*50)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, fargs=(positions,),
                              interval=50, blit=True, repeat=True)

# Display the animation
plt.show()
