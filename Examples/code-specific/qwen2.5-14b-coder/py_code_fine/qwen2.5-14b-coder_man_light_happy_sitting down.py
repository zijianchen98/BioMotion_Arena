
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and the frame rate
num_lights = 15
fps = 30

# Define the duration of the animation in seconds
duration = 5

# Calculate the total number of frames
total_frames = int(duration * fps)

# Define the initial positions of the lights
initial_positions = np.random.rand(num_lights, 2) * 100

# Define the target positions of the lights for the sitting down action
target_positions = np.array([
    [50, 80], [55, 75], [60, 70], [65, 65], [70, 60],
    [30, 80], [35, 75], [40, 70], [45, 65], [50, 60],
    [20, 90], [25, 85], [30, 80], [35, 75], [40, 70]
])

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.axis('off')

# Create the lights as scatter plot points
lights, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'o', color='white')

# Define the update function for the animation
def update(frame):
    # Calculate the current positions of the lights using linear interpolation
    current_positions = initial_positions + (target_positions - initial_positions) * (frame / total_frames)
    
    # Update the positions of the lights
    lights.set_offsets(current_positions)
    
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
