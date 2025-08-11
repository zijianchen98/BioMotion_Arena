
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 5  # seconds
fps = 30  # frames per second
frames = duration * fps

# Points initialization
points = np.zeros((num_points, 2))

# Define the initial positions of the points (based on a sad jumping woman)
def init_points():
    # Head
    points[0] = [0, 2]
    # Shoulders
    points[1] = [-0.5, 1.5]
    points[2] = [0.5, 1.5]
    # Elbows
    points[3] = [-0.8, 1]
    points[4] = [0.8, 1]
    # Hands
    points[5] = [-1, 0.5]
    points[6] = [1, 0.5]
    # Hips
    points[7] = [-0.5, 0]
    points[8] = [0.5, 0]
    # Knees
    points[9] = [-0.5, -1]
    points[10] = [0.5, -1]
    # Feet
    points[11] = [-0.5, -1.5]
    points[12] = [0.5, -1.5]
    # Weight (ground)
    points[13] = [0, -2]
    points[14] = [0, -2.5]

def animate(i):
    # Clear the plot
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-3, 3)
    plt.gca().set_facecolor('black')
    
    # Update the vertical position to create a jumping effect
    jump_height = np.sin((i / frames) * np.pi) * 2  # Jumping arc
    for j in range(num_points):
        points[j][1] += jump_height if j < 11 else 0  # Do not affect weight position

    # Draw points
    plt.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Initialize the points
init_points()

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/fps)

# Show the animation
plt.show()
