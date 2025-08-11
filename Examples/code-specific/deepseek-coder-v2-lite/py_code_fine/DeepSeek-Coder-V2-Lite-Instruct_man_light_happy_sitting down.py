
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
    # Simulate sitting down motion
    angle = (frame_number / num_frames) * np.pi
    positions[:, 1] = 0.5 - 0.5 * np.cos(angle)
    return positions

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Initialize lights
lights = [plt.Circle((pos[0], pos[1]), light_radius, color='white') for pos in positions]

# Add lights to the plot
for light in lights:
    ax.add_artist(light)

# Animation function
def animate(frame_number):
    positions = update_positions(frame_number, positions)
    for i, light in enumerate(lights):
        light.center = (positions[i, 0], positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
