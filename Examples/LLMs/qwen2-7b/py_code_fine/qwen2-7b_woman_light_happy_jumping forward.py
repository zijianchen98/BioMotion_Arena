
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
N_POINTS = 15
ACTION = 'jumping forward'
FRAME_RATE = 60
DURATION = 5  # in seconds

def update(frame):
    # Clear the figure
    fig.clear()
    
    # Set up the plot
    ax = fig.add_subplot((projection='3d')
    ax.set_aspect('equal')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-100, 100)
    ax.set_xlabel('X ')
    ax.set_ylabel(' Y ')
    ax.set_zlabel(' Z ')
    ax.set_title(f"{ACTION} woman with light weight")
    
    # Update the positions of the points based on frame number
    for i in range(N):
        x = np.sin(np.deg2rad(((frame * i) % 360))
        y = np.cos(np.deg2rad((frame * i) % 360))
        z = np.sin(np.deg2rad(((frame * i) / 2) % 360))
        
        # Scale the points according to the action's
        if ACTION == 'jumping forward':
            scale_factor = frame * 2
        else:
            scale_factor = 1
        
        # Plot the point
        ax.scatter(x, y, z, color='white', s=scale_factor)

    # Remove axes and grid for better focus on the motion
    ax.axis('off')
    ax.grid(False)

# Create the figure and animation
fig = plt.figure(figsize=(8, 8))
ani = FuncAnimation(fig, update, frames=np.arange(0, DURATION * FRAME_RATE, 1),
                    interval=1000 / FRAME_RATE, blit=False)

plt.show()

