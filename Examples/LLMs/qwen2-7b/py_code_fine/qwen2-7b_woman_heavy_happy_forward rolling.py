
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure and axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot( (111, projection='3d'

# Define the number of points and their initial positions
num_points = 15
initial_positions = np.random.uniform(-1, 1, (num_points, 3)

# Set up the animation parameters
frame_duration = 0.05 # in seconds
total_frames = 60
frame_count = 0

# Function to update the animation frame by frame
def update_frame(frame):
    global frame_count
    frame_count += 1
    if frame_count > total_frames:
        frame_count = 0

    # Calculate the movement of each point based on the specified action
    movement_direction = np.array([np.sin(frame_count / 30), np.sin(frame_count / 15), np.sin(frame_count / 45)])
    movement_distance = 0.1 * np.cos(frame_count / 15)
    new_positions = initial_positions + movement_direction * movement_distance

    # Update the positions of the points
    ax.clear()
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel(' Y')
    ax.set_zlabel(' Z')
    ax.set_title('Forward Rolling')
    
    for i in range(num_points):
        ax.scatter(new_positions[i][0], new_positions[i][1], new_positions[i][2], color='white')

# Animate the points
ani = FuncAnimation(fig, update_frame, frames=np.arange((1, total_frames + 1), interval=frame_duration * 1000)

plt.show()

