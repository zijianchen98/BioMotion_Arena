
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the sad woman's body
points = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'shoulder_left': [-0.5, 0.8],
    'shoulder_right': [0.5, 0.8],
    'elbow_left': [-0.7, 0.4],
    'elbow_right': [0.7, 0.4],
    'wrist_left': [-0.9, 0.2],
    'wrist_right': [0.9, 0.2],
    'hip_left': [-0.3, -0.2],
    'hip_right': [0.3, -0.2],
    'knee_left': [-0.4, -0.6],
    'knee_right': [0.4, -0.6],
    'ankle_left': [-0.5, -1.0],
    'ankle_right': [0.5, -1.0],
    'center_of_mass': [0, -0.4]
}

# Convert points to a list of coordinates
point_coords = np.array([points[key] for key in points])

# Function to update the position of the points
def update(frame):
    global point_coords
    t = frame / 100  # Time parameter
    amplitude = 0.5  # Amplitude of the jump
    frequency = 0.5  # Frequency of the jump
    
    # Update y-coordinates to simulate jumping
    point_coords[:, 1] += amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Apply a slight forward movement
    point_coords[:, 0] += 0.01 * t
    
    # Apply a slight downward force due to heavy weight
    point_coords[:, 1] -= 0.005 * t
    
    # Update the scatter plot
    scat.set_offsets(point_coords)
    
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(point_coords[:, 0], point_coords[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
