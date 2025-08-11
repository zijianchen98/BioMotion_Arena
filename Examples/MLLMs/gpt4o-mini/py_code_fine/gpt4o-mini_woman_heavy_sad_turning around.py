
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Initialize the point-light positions for a sad woman turning around
# These points may resemble shoulder, elbows, wrists, hips, knees and feet in a rough way
positions = np.array([
    [0, 3],   # head
    [-1, 2],  # left shoulder
    [1, 2],   # right shoulder
    [-1, 1],  # left elbow
    [1, 1],   # right elbow
    [-1, 0],  # left wrist
    [1, 0],   # right wrist
    [0, 2],   # torso
    [-1, -1], # left hip
    [1, -1],  # right hip
    [-1, -2], # left knee
    [1, -2],  # right knee
    [-1, -3], # left foot
    [1, -3],  # right foot
    [0, -1],  # center of weight (heavy)
])

# Function to update the points position for each frame in the animation
def update(frame):
    plt.clf()  # Clear previous frame
    plt.xlim(-5, 5)
    plt.ylim(-4, 4)
    plt.gca().set_facecolor('black')
    
    # Update the positions to simulate a turning motion
    angle = np.radians(frame)
    for i in range(len(positions)):
        x = positions[i, 0] * np.cos(angle) - positions[i, 1] * np.sin(angle)
        y = positions[i, 0] * np.sin(angle) + positions[i, 1] * np.cos(angle)
        plt.scatter(x, y, color='white', s=100)  # Draw point-lights

# Create the figure and the animation
fig = plt.figure()
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# Show the animation
plt.show()
