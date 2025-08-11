
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
plt.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
# These coordinates are just an example and should be adjusted to represent the initial pose.
initial_positions = np.array([
    [0, 4],     # Head
    [-1, 3],    # Left Shoulder
    [1, 3],     # Right Shoulder
    [-2, 2],    # Left Elbow
    [2, 2],     # Right Elbow
    [-2, 1],    # Left Wrist
    [2, 1],     # Right Wrist
    [0, 2],     # Torso center
    [-0.5, 1],  # Hip center
    [-1, 0],    # Left Hip
    [1, 0],     # Right Hip
    [-1.5, -1],   # Left Knee
    [1.5, -1],   # Right Knee
    [-1.5, -2],   # Left Ankle
    [1.5, -2]    # Right Ankle
])

# Store initial positions for resetting
original_positions = initial_positions.copy()

# Define the animation function
def animate(i):
    global initial_positions

    # Simulate forward rolling motion
    # These transformations are simplified for demonstration purposes.
    # Actual biomechanical simulation would be significantly more complex.

    angle = i * np.pi / 180  # Convert degrees to radians. Adjust speed by changing 'i' or '180'.

    # Rotation around the origin (center of the figure)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # Translation to simulate rolling forward. Adjust the speed as needed.
    translation = np.array([0, -0.05 * i])  # Move downwards


    # Apply transformations to each point
    transformed_positions = np.dot(initial_positions, rotation_matrix.T) + translation


    # Update the point positions
    points.set_data(transformed_positions[:, 0], transformed_positions[:, 1])


    # Reset the animation if it goes too far.
    if i > 100:
          initial_positions = original_positions.copy()
          return points, # Return the points for a frame refresh

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, blit=True, interval=20, repeat=True)

# Show the animation
plt.show()
