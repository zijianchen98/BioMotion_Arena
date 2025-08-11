
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the animation duration and frame rate
duration = 5  # seconds
fps = 30

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=6)

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.0, 1.2],  # Head
    [-0.2, 0.9],  # Left Shoulder
    [0.2, 0.9],  # Right Shoulder
    [-0.4, 0.6],  # Left Elbow
    [0.4, 0.6],  # Right Elbow
    [-0.5, 0.3],  # Left Hand
    [0.5, 0.3],  # Right Hand
    [-0.1, 0.4],  # Left Hip
    [0.1, 0.4],  # Right Hip
    [-0.2, 0.0],  # Left Knee
    [0.2, 0.0],  # Right Knee
    [-0.2, -0.4], # Left Foot
    [0.2, -0.4], # Right Foot
    [-0.1, 0.6], # Chest
    [0.0, 0.5]   # Stomach
])

# Define the animation function
def animate(i):
    # Define the bowing motion
    angle = np.sin(i / fps * np.pi) * 0.5  # Angle from -0.5 to 0.5 radians

    # Calculate the new positions of the point-lights
    positions = initial_positions.copy()
    positions[:, 1] -= np.sin(positions[:, 0] * np.pi) * angle  # Bend forward

    # Apply a slight sway
    sway = np.sin(i / fps * np.pi * 2) * 0.02
    positions[:, 0] += sway

    # Update the point-lights
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

# Save the animation
# ani.save('bowing_animation.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

# Show the animation
plt.show()
