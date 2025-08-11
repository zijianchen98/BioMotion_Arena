
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point-light configuration for a sad man lying down
def create_point_lights(frame):
    # Define the point-light positions (x, y)
    # Here we simplify the representation for the 'sad man lying down'
    body = np.array([
        [0, 0],  # Head
        [-0.2, -0.1],  # Left Shoulder
        [0.2, -0.1],   # Right Shoulder
        [-0.3, -0.3],  # Left Elbow
        [0.3, -0.3],   # Right Elbow
        [-0.25, -0.5], # Left Hand
        [0.25, -0.5],  # Right Hand
        [-0.4, -0.5],  # Left Hip
        [0.4, -0.5],   # Right Hip
        [-0.4, -0.8],  # Left Knee
        [0.4, -0.8],   # Right Knee
        [-0.3, -1.0],  # Left Foot
        [0.3, -1.0],   # Right Foot
        [0, -1.2]      # Mid-Body (approximate center of mass)
    ])
    
    # Shift the position slightly to simulate slow movement
    shift = 0.05 * np.sin(frame / 10)  # Simple oscillatory movement
    body[:, 1] += shift
    
    return body

# Setup the figure for animation
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1.5, 0.1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point-light objects
point_lights = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(15)]

# Animation update function
def update(frame):
    positions = create_point_lights(frame)
    for i, point_light in enumerate(point_lights):
        point_light.set_data(positions[i])
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

# Display the animation
plt.show()
