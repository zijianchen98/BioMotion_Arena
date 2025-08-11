
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
# Adjust these coordinates to match the desired pose
initial_positions = np.array([
    [0, 5],  # Head top
    [-1, 4],  # Left shoulder
    [1, 4],  # Right shoulder
    [-1, 3],  # Left elbow
    [1, 3],  # Right elbow
    [-1, 2],  # Left wrist
    [1, 2],   # Right wrist
    [-1.5, 1],  # Left hip
    [1.5, 1],  # Right hip
    [-1.5, 0],  # Left knee
    [1.5, 0],  # Right knee
    [-1.5, -1],  # Left ankle
    [1.5, -1],  # Right ankle
    [-2, -2],  # Left toe
    [2, -2]   # Right toe
])

# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Set x-axis limits
ax.set_ylim(-3, 6)  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')  # Set background color to black
points, = ax.plot([], [], 'wo', markersize=5)


# Define the animation function
def animate(i):
    # Calculate the current positions of the point lights based on the frame number
    # This part needs to be implemented based on your specific animation
    # Here's a simple example for sitting down motion:
    y_offset = np.sin(2 * np.pi * i / num_frames) * 0.5 # Oscillating motion

    current_positions = initial_positions.copy()
    current_positions[:, 1] -= i * 4/ num_frames
    

    # Update the point light positions
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=30, blit=True)



plt.show()
