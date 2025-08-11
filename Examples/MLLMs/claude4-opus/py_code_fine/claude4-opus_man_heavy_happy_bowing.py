
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 1)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Initialize point lights positions for the body parts
points = np.array([
    [0, 0.8],   # Head
    [-0.5, 0.5], # Left Shoulder
    [0.5, 0.5],  # Right Shoulder
    [-0.5, 0.2], # Left Elbow
    [0.5, 0.2],  # Right Elbow
    [-0.5, -0.2],# Left Hand
    [0.5, -0.2], # Right Hand
    [0, 0.0],   # Center Hip
    [-0.5, -0.8],# Left Knee
    [0.5, -0.8], # Right Knee
    [-0.2, -1.5],# Left Foot
    [0.2, -1.5], # Right Foot
    [0, -0.5],   # Center Weight
    [-0.3, -0.75],# Left Weight
    [0.3, -0.75], # Right Weight
])

# Initialize a scatter object for the point lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=500)

# Animation function
def update(frame):
    global points
    # Define bowing motion
    bow_angle = np.sin(frame * 0.1) * (np.pi / 8)  # Bowing angle variation
    # Update positions based on the bowing angle
    points[:, 1] = (np.sin(bow_angle + np.pi/4) * 0.5 + np.array([0.8, 0.5, 0.5, 0.2, 0.2, -0.2, -0.2, 0.0, -0.8, -0.8, -1.5, -1.5, -0.5, -0.75, -0.75]))
    
    scatter.set_offsets(points)
    return scatter,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
