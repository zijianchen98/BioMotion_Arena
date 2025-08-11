
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the woman's body
points = np.array([
    [0, 0],  # Head
    [-0.1, -0.1],  # Left Shoulder
    [0.1, -0.1],  # Right Shoulder
    [-0.2, -0.2],  # Left Elbow
    [0.2, -0.2],  # Right Elbow
    [-0.3, -0.3],  # Left Hand
    [0.3, -0.3],  # Right Hand
    [0, -0.4],  # Waist
    [-0.1, -0.5],  # Left Hip
    [0.1, -0.5],  # Right Hip
    [-0.2, -0.6],  # Left Knee
    [0.2, -0.6],  # Right Knee
    [-0.3, -0.7],  # Left Foot
    [0.3, -0.7],  # Right Foot
    [0, -0.8]  # Center of Mass
])

# Function to rotate points around the center of mass
def rotate_points(points, angle):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))
    return np.dot(points - points[-1], R) + points[-1]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=10)

# Animation update function
def update(frame):
    angle = frame * 5  # Rotate 5 degrees per frame
    new_points = rotate_points(points, angle)
    scatter.set_offsets(new_points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Display the animation
plt.show()
