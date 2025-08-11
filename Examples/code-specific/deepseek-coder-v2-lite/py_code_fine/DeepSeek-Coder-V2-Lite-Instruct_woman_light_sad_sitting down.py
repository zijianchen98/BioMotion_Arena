
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(5, 95, num_lights)
positions[:, 1] = 50

# Define the animation function
def animate(frame):
    for i in range(num_lights):
        positions[i, 1] = 50 + 10 * np.sin(0.2 * np.pi * frame + i * 0.2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

# Create the lights
lights = [plt.plot([], [], 'wo', markersize=10)[0] for _ in range(num_lights)]

# Initialize the background
ax.scatter(positions[:, 0], positions[:, 1], s=100, c='w', zorder=10)

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False, repeat=True)

# Display the animation
plt.show()
