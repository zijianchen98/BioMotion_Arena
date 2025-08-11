
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Define the initial positions of the point lights
point_lights = np.array([
    [0, 0.8],    # Head
    [-0.2, 0.6], # Left shoulder
    [0.2, 0.6],  # Right shoulder
    [-0.4, 0.4], # Left elbow
    [0.4, 0.4],  # Right elbow
    [-0.5, 0.2], # Left hand
    [0.5, 0.2],  # Right hand
    [0, 0],      # Body
    [-0.1, -0.1],# Left hip
    [0.1, -0.1], # Right hip
    [-0.2, -0.3],# Left knee
    [0.2, -0.3],  # Right knee
    [-0.3, -0.5],# Left foot
    [0.3, -0.5],  # Right foot
    [-0.4, -0.7],# Left heel
    [0.4, -0.7],  # Right heel
])

# Create scatter plot object
scat = ax.scatter(point_lights[:, 0], point_lights[:, 1], color='white', s=30)

# Animation update function
def update(frame):
    global point_lights
    # Waving motion for right hand
    if frame < 25:
        point_lights[6, 1] = 0.2 + 0.1 * np.sin(frame * np.pi / 10)
    else:
        point_lights[6, 1] = 0.2
    
    scat.set_offsets(point_lights)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=50, blit=True)

plt.show()
