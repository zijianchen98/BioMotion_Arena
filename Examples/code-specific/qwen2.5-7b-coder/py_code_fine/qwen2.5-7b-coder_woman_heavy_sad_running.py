
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the sad woman running
num_points = 15
frame_rate = 30
duration = 5  # seconds
time_steps = int(frame_rate * duration)

# Initialize the positions of the points
np.random.seed(42)
initial_positions = np.random.rand(num_points, 2) * 8 - 4  # range from -4 to 4 on both axes

# Define the biomechanical parameters
step_length = 0.2
step_duration = 0.5  # seconds
stride_frequency = 2 / step_duration  # Hz

# Calculate the time steps for each frame
time_step_size = 1 / frame_rate
time_steps_array = np.arange(time_steps) * time_step_size

# Generate the animation frames
frames = []
for t in time_steps_array:
    # Update the positions based on the stride frequency and step length
    phase = t * stride_frequency % 1
    x_displacement = step_length * np.sin(2 * np.pi * phase)
    y_displacement = step_length * np.cos(2 * np.pi * phase)
    
    new_positions = initial_positions + np.array([x_displacement, y_displacement])
    
    # Ensure the points stay within the bounds of the screen
    new_positions[:, 0] = np.clip(new_positions[:, 0], -4, 4)
    new_positions[:, 1] = np.clip(new_positions[:, 1], -4, 4)
    
    # Create a scatter plot for the current frame
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    scatter = ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)
    frames.append(scatter)

# Create the animation
ani = FuncAnimation(fig, lambda s: s.set_offsets(frames[ani.current_frame].get_offsets()), frames, interval=time_step_size * 1000, repeat=False)

# Save the animation as a GIF file
ani.save('sad_woman_running.gif', writer='pillow', fps=frame_rate)

plt.show()
