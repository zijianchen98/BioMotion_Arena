
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the initial positions of the point-lights
# These positions should roughly correspond to the joints of a human figure
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.8, 1.0], # Left Elbow
    [0.8, 1.0],  # Right Elbow
    [-1.2, 0.5], # Left Wrist
    [1.2, 0.5],  # Right Wrist
    [-0.3, 0.0], # Left Hip
    [0.3, 0.0],  # Right Hip
    [-0.8, -0.5],# Left Knee
    [0.8, -0.5], # Right Knee
    [-0.8, -1.0],# Left Ankle
    [0.8, -1.0], # Right Ankle
    [-0.4, -1.5], # Left Foot
    [0.4, -1.5]   # Right Foot
])

# Define the motion of each point-light over time
# This is where you would implement the "jumping forward" motion
# For simplicity, let's just make each point-light oscillate slightly
def update_points(num_frames):
    positions = np.zeros((num_frames, num_points, 2))
    for i in range(num_points):
        for frame in range(num_frames):
            # Simulate jumping motion with a sine wave
            x_offset = 0.1 * np.sin(2 * np.pi * frame / 50) # Smaller for forward movement
            y_offset = 0.3 * np.sin(2 * np.pi * frame / 25)  # Larger for jumping up and down
            positions[frame, i, 0] = initial_positions[i, 0] + x_offset
            positions[frame, i, 1] = initial_positions[i, 1] + y_offset

    return positions

# Set the number of frames for the animation
num_frames = 100

# Generate the positions for all frames
positions = update_points(num_frames)

# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 3])
ax.set_aspect('equal')
plt.axis('off')  # Hide axes

# Create the scatter plot for the point-lights
scatter = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white', s=50)

# Define the animation function
def animate(frame):
    scatter.set_offsets(positions[frame, :, :])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
