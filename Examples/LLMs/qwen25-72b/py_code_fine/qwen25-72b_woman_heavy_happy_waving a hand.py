
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the happy woman waving her hand
points = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'shoulder_left': [-0.5, 0.8],
    'elbow_left': [-1.0, 0.5],
    'wrist_left': [-1.5, 0.8],
    'hand_left': [-2.0, 1.0],
    'shoulder_right': [0.5, 0.8],
    'elbow_right': [1.0, 0.5],
    'wrist_right': [1.5, 0.8],
    'hip_left': [-0.5, -0.5],
    'knee_left': [-0.5, -1.0],
    'ankle_left': [-0.5, -1.5],
    'hip_right': [0.5, -0.5],
    'knee_right': [0.5, -1.0],
    'ankle_right': [0.5, -1.5]
}

# Convert points to a list of coordinates
point_coords = np.array([points[key] for key in points])

# Function to update the position of the points
def update(frame):
    global point_coords
    # Waving hand motion
    angle = np.sin(frame * 0.1) * 0.5
    point_coords[4] = [-2.0 + angle, 1.0 + angle * 0.5]
    point_coords[5] = [-2.5 + angle, 1.2 + angle * 0.5]
    
    # Update the positions of the points
    scatter.set_offsets(point_coords)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scatter = ax.scatter(point_coords[:, 0], point_coords[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
