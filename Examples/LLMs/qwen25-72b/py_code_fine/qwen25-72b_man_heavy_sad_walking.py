
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the sadman's joints
points = np.array([
    [0, 1],  # Head
    [-0.2, 0.8],  # Neck
    [-0.4, 0.6],  # Left Shoulder
    [-0.6, 0.4],  # Left Elbow
    [-0.8, 0.2],  # Left Hand
    [0.2, 0.8],  # Right Shoulder
    [0.4, 0.6],  # Right Elbow
    [0.6, 0.4],  # Right Hand
    [-0.2, 0],  # Left Hip
    [-0.4, -0.2],  # Left Knee
    [-0.6, -0.4],  # Left Foot
    [0.2, 0],  # Right Hip
    [0.4, -0.2],  # Right Knee
    [0.6, -0.4],  # Right Foot
    [0, -0.6]  # Center of Mass
])

# Define the walking gait parameters
gait_period = 2 * np.pi
gait_amplitude = 0.2
gait_frequency = 1 / gait_period

# Function to update the position of the points based on the gait
def update_points(t):
    x_offset = gait_amplitude * np.sin(gait_frequency * t)
    y_offset = -gait_amplitude * np.cos(gait_frequency * t) * 0.5  # Heavy weight effect

    # Update the positions of the points
    points[:, 0] += x_offset
    points[:, 1] += y_offset

    # Adjust the positions of the feet to simulate walking
    left_foot_offset = gait_amplitude * np.sin(gait_frequency * t + np.pi) * 0.5
    right_foot_offset = gait_amplitude * np.sin(gait_frequency * t) * 0.5

    points[10, 0] += left_foot_offset
    points[13, 0] += right_foot_offset

    return points

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Animation update function
def animate(i):
    global points
    points = update_points(i)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.1), interval=50, blit=True)

# Display the animation
plt.show()
