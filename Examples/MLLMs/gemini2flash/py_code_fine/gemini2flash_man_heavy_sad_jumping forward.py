
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the animation parameters
fps = 30  # Frames per second
duration = 5  # Duration of the animation in seconds
num_frames = fps * duration  # Total number of frames

# Define the initial positions of the point-lights
# You'll need to adjust these coordinates to match the desired pose
initial_positions = np.array([
    [0, 2],   # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1, 1],  # Left Elbow
    [1, 1],   # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 0.75], # Hip center
    [-0.7, 0.25], # Left Hip
    [0.7, 0.25],  # Right Hip
    [-1, -0.5], # Left Knee
    [1, -0.5],  # Right Knee
    [-1.2, -1.2], # Left Ankle
    [1.2, -1.2], # Right Ankle
    [0, -1.5]    # Foot Center
])

# Define the motion of each point-light over time
# This is where you'll need to define the "jumping forward" action
motion = np.zeros((num_frames, num_points, 2))

# Example motion: Simple vertical oscillation for jumping with forward movement
for i in range(num_points):
    motion[:, i, 0] = 0.5*np.sin(np.linspace(0, 4 * np.pi, num_frames)) # X-axis Movement
    motion[:, i, 1] = np.sin(np.linspace(0, 2 * np.pi, num_frames)) #Y-axis movement, jumping

# Combine the initial positions and motion to get the final positions of the points
positions = initial_positions + motion

# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')  # Ensure that the axes are scaled equally
ax.set_facecolor('black')  # Set background to black
ax.axis('off')  # Turn off axes

# Create the scatter plot for the point-lights
scat = ax.scatter([], [], c='white', s=20)

# Define the animation function
def animate(i):
    scat.set_offsets(positions[i])
    return (scat,)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True)

# Save the animation (optional)
# ani.save('sadman_jumping_forward.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

# Display the animation
plt.show()
