
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the happy man's joints
points = {
    'head': [0, 1.8],
    'neck': [0, 1.6],
    'shoulder_left': [-0.4, 1.4],
    'shoulder_right': [0.4, 1.4],
    'elbow_left': [-0.7, 1.2],
    'elbow_right': [0.7, 1.2],
    'wrist_left': [-0.9, 1.0],
    'wrist_right': [0.9, 1.0],
    'hip_left': [-0.3, 1.0],
    'hip_right': [0.3, 1.0],
    'knee_left': [-0.3, 0.6],
    'knee_right': [0.3, 0.6],
    'ankle_left': [-0.3, 0.2],
    'ankle_right': [0.3, 0.2],
    'weight': [0, 0.1]
}

# Convert points to a list of coordinates
point_coords = np.array([points[key] for key in points])

# Function to update the position of the points
def update(frame):
    global point_coords
    angle = frame * np.pi / 180  # Convert frame number to angle in radians
    bow_angle = np.sin(angle) * 0.2  # Simulate a bowing motion
    
    # Update the y-coordinates of the points to simulate the bowing motion
    point_coords[:, 1] -= bow_angle
    
    # Update the scatter plot
    scat.set_offsets(point_coords)
    
    # Reset the y-coordinates after the frame
    point_coords[:, 1] += bow_angle
    
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 2.0)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(point_coords[:, 0], point_coords[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Display the animation
plt.show()
