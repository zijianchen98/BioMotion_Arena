
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)

# Initialize the lights as scatter plot
lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    # Update positions (simple random walk)
    for i in range(num_lights):
        positions[i, 1] += 0.02 * (np.random.rand() - 0.5)  # Random vertical movement
        positions[i, 0] += 0.05  # Constant horizontal movement
        if positions[i, 0] > 1:
            positions[i, 0] = 0

    # Update the scatter plot
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
