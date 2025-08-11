
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
max_height = 1.5
min_height = 0.5
num_frames = 100

# Generate positions
positions = np.zeros((num_lights, num_frames, 2))
for i in range(num_lights):
    positions[i, :, 0] = i
positions[:, :, 1] = min_height + (max_height - min_height) * np.sin(np.linspace(0, 2 * np.pi, num_frames))

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, num_lights)
ax.set_ylim(0, max_height + 0.5)

# Initialize lights
lights = [plt.plot([], [], 'wo', markersize=10)[0] for _ in range(num_lights)]

# Animation function
def animate(frame):
    for i, light in enumerate(lights):
        light.set_data(positions[i, frame, 0], positions[i, frame, 1])

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Set up plot
ax.set_aspect('equal')
ax.set_facecolor('k')
plt.axis('off')

# Show animation
plt.show()
