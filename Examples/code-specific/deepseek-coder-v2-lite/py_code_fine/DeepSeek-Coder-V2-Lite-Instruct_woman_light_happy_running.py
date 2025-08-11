
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-0.5, 0.5, num_lights)
positions[:, 1] = 0.5

# Function to update positions
def update_positions(frame_number, positions):
    # Running animation
    positions[:, 1] -= 0.05  # Move lights up
    positions[:, 0] += 0.03  # Move lights horizontally
    if frame_number % 5 == 0:  # Change direction every 5 frames
        positions[:, 0] *= -1
    return positions

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize scatter plot for the lights
scatter = ax.scatter([], [], s=light_radius*100, color='white')

# Generate initial data
data = [positions]

# Generate frames
for _ in range(num_frames):
    positions = update_positions(_, positions)
    data.append(positions)

# Set up the animation
def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame_number):
    positions = data[frame_number]
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, repeat=True, blit=True)

# Set background to black
ax.set_facecolor('black')

# Show the animation
plt.show()
