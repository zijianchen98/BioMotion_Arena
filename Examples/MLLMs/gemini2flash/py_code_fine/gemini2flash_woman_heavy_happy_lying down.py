
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames for the animation
num_frames = 100

# Define the initial coordinates of the 15 points
points = np.array([
    [0.0, 1.5],   # Head
    [-0.3, 1.3],  # Left Shoulder
    [0.3, 1.3],   # Right Shoulder
    [-0.6, 1.0],  # Left Elbow
    [0.6, 1.0],   # Right Elbow
    [-0.3, 0.7],  # Left Wrist
    [0.3, 0.7],   # Right Wrist
    [0.0, 1.0],   # Torso
    [-0.2, 0.4],  # Left Hip
    [0.2, 0.4],   # Right Hip
    [-0.4, 0.1],  # Left Knee
    [0.4, 0.1],   # Right Knee
    [-0.2, -0.2], # Left Ankle
    [0.2, -0.2], # Right Ankle
    [0.0, -0.5]    # Foot
])

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 2])
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot with white points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=20)


# Define the animation function
def animate(i):
    # Define the movements of the points for the 'lying down' action
    # This is just an example, adjust the movements as needed to make the animation realistic

    # Apply the movement to each point
    new_points = points + np.array([
        [0.0, 0.0], 
        [0.01 * np.sin(i * 0.1), 0.005 * np.cos(i * 0.1)], 
        [-0.01 * np.sin(i * 0.1), 0.005 * np.cos(i * 0.1)],
        [0.02 * np.cos(i * 0.1), 0.01 * np.sin(i * 0.1)],
        [-0.02 * np.cos(i * 0.1), 0.01 * np.sin(i * 0.1)],
        [0.015 * np.sin(i * 0.1), -0.005 * np.cos(i * 0.1)],
        [-0.015 * np.sin(i * 0.1), -0.005 * np.cos(i * 0.1)],
        [0.0, 0.002 * np.sin(i * 0.2)], 
        [0.005 * np.cos(i * 0.1), 0.005 * np.sin(i * 0.1)], 
        [-0.005 * np.cos(i * 0.1), 0.005 * np.sin(i * 0.1)],
        [0.002 * np.sin(i * 0.1), 0.01 * np.cos(i * 0.1)], 
        [-0.002 * np.sin(i * 0.1), 0.01 * np.cos(i * 0.1)],
        [0.001 * np.cos(i * 0.1), -0.005 * np.sin(i * 0.1)], 
        [-0.001 * np.cos(i * 0.1), -0.005 * np.sin(i * 0.1)],
        [0.0, -0.001 * np.cos(i * 0.2)]
    ])
    
    # Update the scatter plot
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Save the animation (optional)
# ani.save('lying_down_animation.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()
