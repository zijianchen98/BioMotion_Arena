
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15  # Number of point lights
duration = 4     # Duration of the animation in seconds
fps = 30         # Frames per second
frames = duration * fps  # Total frames

# Initialize point light positions
# Fixed positions representing a human figure (example coordinates)
positions = np.array([
    [0, 2], [1, 2], [-1, 2],  # Head
    [0, 1.5],  # Neck
    [0, 1],    # Shoulder (left)
    [0, 0.5],  # Elbow (left)
    [-0.5, 0], # Wrist (left)
    [0, 1],    # Shoulder (right)
    [0, 0.5],  # Elbow (right)
    [0.5, 0],  # Wrist (right)
    [0, 1],    # Hip (left)
    [0, 0],    # Knee (left)
    [0, -0.5], # Ankle (left)
    [0, 1],    # Hip (right)
    [0, 0],    # Knee (right)
    [0, -0.5], # Ankle (right)
    [0, -1]    # Load at the back
])

# Create a function to update the plot
def update(frame):
    plt.clf()  # Clear current figure
    plt.xlim(-3, 3)
    plt.ylim(-2, 3)
    plt.gca().set_facecolor('black')
    
    # Calculate the angle of rotation
    angle = (frame / frames) * (2 * np.pi)  # Full rotation
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate points
    rotated_positions = positions @ rotation_matrix
    
    # Add weight to the plot (sagging)
    weight_position = np.array([0, -1])  # Position for the weight
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white', s=100)
    plt.scatter(weight_position[0], weight_position[1], color='white', s=200)  # Heavy weight
    
# Create the figure and axis
fig = plt.figure()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, repeat=True)

# Show the animation
plt.show()
