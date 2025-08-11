
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the frame rate
num_points = 15
fps = 30

# Define the walking cycle parameters
step_length = 0.5
stride_time = 1.0 / fps * 4  # 4 frames per stride
swing_time = 1.0 / fps * 6  # 6 frames per swing
stance_time = stride_time + swing_time

# Define the initial positions and velocities of the points
positions = np.zeros((num_points, 2))
velocities = np.zeros((num_points, 2))

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the update function for the animation
def update(frame):
    global positions, velocities
    
    # Update the positions based on the walking cycle
    time = frame / fps
    for i in range(num_points):
        if i % 2 == 0:  # left leg
            phase = (time - i * stance_time / num_points) % stance_time
            if phase < stride_time:
                positions[i, 0] = step_length * phase / stride_time
                positions[i, 1] = 0.1 * np.sin(2 * np.pi * phase / stride_time)
            else:
                positions[i, 0] = step_length
                positions[i, 1] = 0.1 * np.sin(2 * np.pi * (phase - stride_time) / swing_time)
        else:  # right leg
            phase = (time - (i - 1) * stance_time / num_points) % stance_time
            if phase < stride_time:
                positions[i, 0] = step_length - step_length * phase / stride_time
                positions[i, 1] = 0.1 * np.sin(2 * np.pi * phase / stride_time)
            else:
                positions[i, 0] = 0
                positions[i, 1] = 0.1 * np.sin(2 * np.pi * (phase - stride_time) / swing_time)
    
    # Update the plot data
    points.set_data(positions[:, 0], positions[:, 1])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=120, blit=True)

# Show the animation
plt.show()
