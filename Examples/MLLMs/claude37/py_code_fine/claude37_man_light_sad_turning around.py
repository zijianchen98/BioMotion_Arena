
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
duration = 5  # total duration of the animation in seconds
fps = 30  # frames per second
num_frames = duration * fps

# Initialize positions of points simulating a human figure in a sad posture
initial_positions = np.array([
    [0, 1],   # head
    [-0.5, 0.5], [0.5, 0.5],  # shoulders
    [-0.3, 0], [0.3, 0],  # elbows
    [-0.2, -0.5], [0, -0.5], [0.2, -0.5],  # hands
    [0, -1]   # feet
])

def update(frame):
    plt.clf()  # clear previous frame
    angle = (frame / num_frames) * 2 * np.pi  # calculate angle for rotation

    # Create rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate points
    rotated_positions = np.dot(initial_positions, rotation_matrix)

    # Plot points
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white', s=100)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_facecolor('black')  # black background
    plt.axis('off')  # turn off axis
   
# Create the figure and set the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps)

# Display the animation
plt.show()
