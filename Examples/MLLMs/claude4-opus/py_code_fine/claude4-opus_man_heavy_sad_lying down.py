
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Parameters**
num_points = 15  # Number of point-lights
frames = 100     # Number of frames in the animation

# **Initial Positions of Point-Lights**
# Simulating a sad man lying down with joint position coordinates
# (These values can be adjusted for more realism)
positions = np.array([
    [0, 1.5],   # Head
    [-0.5, 1.0],  # Left shoulder
    [0.5, 1.0],   # Right shoulder
    [-0.5, 0.5],  # Left elbow
    [0.5, 0.5],   # Right elbow
    [-0.6, 0],    # Left wrist
    [0.6, 0],     # Right wrist
    [0, 0.5],     # Torso
    [-0.3, -0.5], # Left hip
    [0.3, -0.5],  # Right hip
    [-0.3, -1.0], # Left knee
    [0.3, -1.0],  # Right knee
    [-0.5, -1.5], # Left ankle
    [0.5, -1.5],  # Right ankle
    [0.5, -1.2],  # Right foot
    [-0.5, -1.2]  # Left foot
])

# **Animation Function**
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-2, 2)  # Set x-axis limits
    plt.ylim(-2, 2)  # Set y-axis limits
    plt.axis('off')  # Turn off the axis

    # **Simulating Motion for a Sad Look**
    # Adjust y values to create a slight "sinking" effect
    offsets = np.sin((frame / frames) * np.pi) * np.array([0, 0, 0, 0, 0, -0.1, -0.1, 0, 0, 0, -0.1, -0.1, -0.2, -0.2, -0.1, -0.1])
    new_positions = positions + offsets.reshape(-1, 1)

    plt.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)  # Draw the point-lights

# **Create Animation**
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# **Display the Animation**
plt.show()
