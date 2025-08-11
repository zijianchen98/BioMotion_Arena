
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for the sad woman with heavy weight
# The positions are defined in a 3D space, but we'll only use the x and y coordinates for the animation
point_light_positions = np.array([
    [-0.3, 0.5, 0],  # head
    [-0.2, 0.4, 0],  # left shoulder
    [0.2, 0.4, 0],   # right shoulder
    [-0.1, 0.3, 0],  # left elbow
    [0.1, 0.3, 0],   # right elbow
    [-0.2, 0.2, 0],  # left hand
    [0.2, 0.2, 0],   # right hand
    [0, 0.1, 0],     # torso
    [-0.1, 0, 0],    # left hip
    [0.1, 0, 0],     # right hip
    [-0.2, -0.1, 0], # left knee
    [0.2, -0.1, 0],  # right knee
    [-0.1, -0.2, 0], # left ankle
    [0.1, -0.2, 0],  # right ankle
    [0, -0.3, 0]     # heavy weight
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Update the point-light positions based on the frame number
    # For a forward rolling motion, we'll move the points in a circular motion
    angle = frame / 10.0
    for i, position in enumerate(point_light_positions):
        x, y, _ = position
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        
        # Add some noise to the motion to make it look more natural
        new_x += np.random.uniform(-0.01, 0.01)
        new_y += np.random.uniform(-0.01, 0.01)
        
        ax.plot(new_x, new_y, 'o', markersize=5, color='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
