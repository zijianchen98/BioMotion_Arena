
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initial positions of the points for the sadman lying down
points = np.array([
    [ 0.5,  0.0],  # Head
    [-0.1, 0.1],   # Left eye
    [ 0.1, 0.1],   # Right eye
    [ 0.0, -0.1],  # Nose
    [ 0.0, -0.2],  # Mouth
    [-0.4, -0.4],  # Left shoulder
    [ 0.4, -0.4],  # Right shoulder
    [-0.6, -0.6],  # Left hand
    [ 0.6, -0.6],  # Right hand
    [ 0.0, -1.0],  # Waist
    [-0.5, -1.5],  # Left hip
    [ 0.5, -1.5],  # Right hip
    [-0.6, -2.0],  # Left knee
    [ 0.6, -2.0],  # Right knee
    [ 0.0, -2.5]   # Feet
])

# Function to update the frame
def update(frame):
    plt.clf()
    plt.scatter(points[:, 0], points[:, 1], c='white', s=100)
    plt.xlim(-1.0, 1.0)
    plt.ylim(-3.0, 1.0)
    plt.gca().set_aspect('equal')
    plt.axis('off')

    # Simple oscillation to simulate lying down motion
    points[:, 1] = points[:, 1] + np.sin(frame / 10) * 0.05

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
