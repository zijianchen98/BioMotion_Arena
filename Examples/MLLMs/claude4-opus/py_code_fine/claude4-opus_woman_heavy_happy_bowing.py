
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Constants**
num_points = 15  # Total number of point-lights
fps = 30         # Frames per second
duration = 5     # Total duration of the animation in seconds
frames = fps * duration  # Total number of frames

# **Initialize Points**
# Basic positions for a happy woman bowing (simplified)
initial_position = np.array([[0, 2], [-1, 1.5], [1, 1.5], [-1, 1], [1, 1],
                             [0, 0], [-0.5, -1], [0.5, -1], [-0.5, -2], [0.5, -2],
                             [0, -3], [-0.75, -3], [0.75, -3], [-0.5, -3.5], [0.5, -3.5]])

# **Animation Function**
def update(frame):
    plt.clf()
    angle = np.pi * frame / frames  # Create a smooth motion transition
    # Update the y-coordinate for the bowing motion
    vertical_movement = np.sin(angle)
    
    # Adjust each point's y position according to the motion
    points = initial_position + np.array([0, vertical_movement])
    
    # Plot points
    plt.scatter(points[:, 0], points[:, 1], color='white', s=100)  # s is the size of points
    plt.xlim(-2, 2)
    plt.ylim(-4, 3)
    plt.gca().set_facecolor('black')  # Set background color to black
    plt.axis('off')  # Turn off the axis

# **Create the Animation**
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps)

# **Show the Animation**
plt.show()
