
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.2
black_background = np.zeros((60, 60))

# Initial positions of the lights
positions = np.random.rand(num_lights, 2) * 50 + 5

# Function to update the positions of the lights
def update_positions(frame_number, positions):
    for i in range(num_lights):
        # Simple sinusoidal motion for each light
        positions[i, 0] += 0.1 * np.cos(frame_number / 10 + i * 0.2)
        positions[i, 1] += 0.1 * np.sin(frame_number / 10 + i * 0.2)
        # Boundary conditions
        positions[i, 0] = np.clip(positions[i, 0], 0, 59)
        positions[i, 1] = np.clip(positions[i, 1], 0, 59)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(0, 60)

# Initialize the scatter plot for the lights
scatter = ax.scatter([], [], s=light_radius*100, color='white')

# Function to initialize the scatter plot
def init():
    scatter.set_offsets(positions)
    return scatter,

# Function to update the scatter plot
def update(frame_number):
    positions = update_positions(frame_number, positions)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), init_func=init,
                              interval=50, blit=True, repeat=True)

# Display the animation
plt.show()
