
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
x_positions = np.array([-0.5, 0.5, -0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 
                        0, 0, 0, 0, 0, -0.25, 0.25])  # X coordinates for point-lights
y_positions = np.array([2.5, 2.5, 1.5, 1.5, 0.5, 0.5, -0.5, -0.5, 
                        3, 3.5, 4, 2.5, 1.5, 2, 2])  # Initial Y coordinates

# Function to update the position of lights for each frame
def update(frame):
    plt.clf()
    plt.xlim(-1, 1)
    plt.ylim(-1, 5)
    plt.gca().set_facecolor('black')
    plt.axis('off')
    
    # Calculate new positions for waving motion
    wave_offset = 0.1 * np.sin(frame / 10.0)  # Waving motion effect
    animated_y_positions = y_positions + wave_offset
    
    # Remove points to create the effect of a waving hand
    points = np.vstack((x_positions, animated_y_positions)).T
    plt.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Set up the figure and animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

plt.show()
