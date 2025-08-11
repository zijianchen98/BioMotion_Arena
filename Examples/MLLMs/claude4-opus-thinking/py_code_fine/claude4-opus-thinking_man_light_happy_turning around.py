
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initialize point coordinates
# Starting positions for the point lights arranged in a human-like form (15 points)
initial_positions = np.array([
    [0, 5],   # head
    [-1, 4],  # left shoulder
    [1, 4],   # right shoulder
    [-1, 3],  # left elbow
    [1, 3],   # right elbow
    [0, 2],   # torso
    [-1, 1],  # left hip
    [1, 1],   # right hip
    [-1, 0],  # left knee
    [1, 0],   # right knee
    [0, -1],  # left ankle
    [0, -2],  # right ankle
    [0, 4.5], # head position adjustment
    [-1, 4.5],
    [1, 4.5],
    [0, 3.5]
])

# Function to update the positions of point lights for turning
def update(frame):
    plt.clf()
    angle = np.radians(frame * 5)  # Rotation angle for each frame
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = initial_positions @ rotation_matrix
    
    plt.scatter(rotated_positions[:,0], rotated_positions[:,1], color='white', s=100)
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.gca().set_facecolor('black')
    plt.axis('off')

# Create figure for the animation
fig = plt.figure()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=72, interval=100, repeat=True)

# To display the animation
plt.show()
