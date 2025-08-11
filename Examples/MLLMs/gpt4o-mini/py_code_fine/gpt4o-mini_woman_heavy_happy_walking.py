
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of point lights
num_points = 15

# Initialize the positions of the point lights
# Group them to represent a walking figure, 3 segments for head, torso and legs
points_start = np.array([[0, 0.5], [-0.1, 0.6], [0.1, 0.6],  # Head
                         [0, 0.2], [-0.1, 0.3], [0.1, 0.3],  # Shoulders
                         [0, 0], [-0.1, 0], [0.1, 0],  # Torso
                         [0, -0.5], [-0.1, -0.6], [0.1, -0.6],  # Hips
                         [-0.2, -1.2], [0.2, -1.2], [0, -1.7]])  # Legs

# Calculate walking cycle offsets using sine wave for smooth walking motion
def walking_motion(frame):
    phase = frame * 0.1
    offsets = np.array([[0, 0], 
                        [-0.1 * np.sin(phase), 0.05 * np.cos(phase)], 
                        [0.1 * np.sin(phase), 0.05 * np.cos(phase)], 
                        [0, 0], 
                        [-0.1 * np.sin(phase), -0.05 * np.cos(phase)], 
                        [0.1 * np.sin(phase), -0.05 * np.cos(phase)], 
                        [0, -0.5], 
                        [-0.1 * np.sin(phase), -0.1 * np.cos(phase)], 
                        [0.1 * np.sin(phase), -0.1 * np.cos(phase)], 
                        [0, -0.5], 
                        [-0.1 * np.sin(phase), -0.15 * np.cos(phase)], 
                        [0.1 * np.sin(phase), -0.15 * np.cos(phase)], 
                        [-0.2 * np.sin(phase), -0.15 * np.cos(phase)], 
                        [0.2 * np.sin(phase), -0.15 * np.cos(phase)], 
                        [0, -0.25]])  # slight upward movement for legs
    return points_start + offsets

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 1)
ax.set_facecolor('black')
points_scatter = ax.scatter([], [], s=100, color='white')

# Animation function
def update(frame):
    points = walking_motion(frame)
    points_scatter.set_offsets(points)
    return points_scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
