
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each point light to simulate turning around
target_positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    angle = np.random.uniform(0, 2 * np.pi)
    radius = np.random.uniform(0.2, 0.8)
    target_positions[i] = [radius * np.cos(angle), radius * np.sin(angle)]

# Define the time steps for the animation
num_frames = 60
frame_time = 1 / num_frames

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights as scatter plot
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'w.', markersize=10)

# Define the update function for the animation
def update(frame):
    # Calculate the current positions of the point lights
    current_positions = initial_positions + (target_positions - initial_positions) * frame * frame_time
    
    # Update the positions of the point lights
    points.set_offsets(current_positions)
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 * frame_time, blit=True)

# Show the animation
plt.show()
