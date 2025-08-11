
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters
n_points = 15
duration = 5  # duration of the animation in seconds
fps = 30  # frames per second
total_frames = duration * fps

# Initial positions of the point lights representing a happy man
# (x, y) coordinates of the 15 point lights
initial_positions = np.array([
    [0, 2],    # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.75, 1], [0.75, 1],  # Hands
    [-0.5, 0], [0.5, 0],  # Waist
    [-0.5, -1], [0.5, -1],  # Legs
    [-0.75, -1.5], [0.75, -1.5],  # Feet
    [0, -2],   # Back of the body
    # Extra points in case of details
    [0.25, -1.5], [-0.25, -1.5]  # Extra leg details
])

# Animation function
def update(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axis('off')  # Turn off the axes
    
    # Calculate rotation angle
    angle = (frame / total_frames) * 2 * np.pi  # Rotate full circle

    # Generating new positions based on rotation
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle),  np.cos(angle)]])
    new_positions = initial_positions @ rotation_matrix

    # Plot the points
    plt.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Create the figure and animation
fig = plt.figure(figsize=(6, 6), facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps)

# Show the animation
plt.show()
