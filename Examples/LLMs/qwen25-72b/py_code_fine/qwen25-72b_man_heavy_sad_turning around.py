
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the sadman's joints
points = {
    'head': [0, 1],
    'neck': [0, 0],
    'shoulder_left': [-0.5, -0.5],
    'elbow_left': [-0.7, -1],
    'wrist_left': [-0.9, -1.5],
    'shoulder_right': [0.5, -0.5],
    'elbow_right': [0.7, -1],
    'wrist_right': [0.9, -1.5],
    'hip_left': [-0.4, -2],
    'knee_left': [-0.6, -3],
    'ankle_left': [-0.8, -4],
    'hip_right': [0.4, -2],
    'knee_right': [0.6, -3],
    'ankle_right': [0.8, -4],
    'center_of_mass': [0, -2.5]
}

# Convert the points to a list of coordinates
point_coords = np.array([points[key] for key in points])

# Function to update the positions of the points
def update(frame):
    global point_coords
    angle = frame * np.pi / 180  # Convert frame number to angle in radians
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    point_coords = np.dot(point_coords - points['center_of_mass'], rotation_matrix) + points['center_of_mass']
    scat.set_offsets(point_coords)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(point_coords[:, 0], point_coords[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Display the animation
plt.show()
