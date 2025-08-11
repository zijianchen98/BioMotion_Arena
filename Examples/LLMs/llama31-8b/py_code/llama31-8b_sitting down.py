
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Define the point lights
lights = [
    {'x': 0, 'y': 0.5, 'radius': 0.05},  # Head
    {'x': -0.2, 'y': 0.4, 'radius': 0.03},  # Left shoulder
    {'x': 0.2, 'y': 0.4, 'radius': 0.03},  # Right shoulder
    {'x': -0.2, 'y': 0.3, 'radius': 0.02},  # Left elbow
    {'x': 0.2, 'y': 0.3, 'radius': 0.02},  # Right elbow
    {'x': -0.2, 'y': 0.2, 'radius': 0.01},  # Left wrist
    {'x': 0.2, 'y': 0.2, 'radius': 0.01},  # Right wrist
    {'x': -0.1, 'y': 0.1, 'radius': 0.01},  # Left hand
    {'x': 0.1, 'y': 0.1, 'radius': 0.01},  # Right hand
    {'x': -0.2, 'y': 0.6, 'radius': 0.03},  # Left hip
    {'x': 0.2, 'y': 0.6, 'radius': 0.03},  # Right hip
    {'x': -0.2, 'y': 0.5, 'radius': 0.02},  # Left knee
    {'x': 0.2, 'y': 0.5, 'radius': 0.02},  # Right knee
    {'x': -0.2, 'y': 0.4, 'radius': 0.01},  # Left ankle
    {'x': 0.2, 'y': 0.4, 'radius': 0.01}  # Right ankle
]

# Function to update the animation
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the point lights
    for i, light in enumerate(lights):
        if i < 9:
            # Sitting motion for upper body
            light['x'] = np.sin(frame * 0.1 + i * 0.1) * 0.2
            light['y'] = 0.5 + np.cos(frame * 0.1 + i * 0.1) * 0.2
        else:
            # Sitting motion for lower body
            light['x'] = np.sin(frame * 0.1 + i * 0.1) * 0.2
            light['y'] = 0.6 + np.cos(frame * 0.1 + i * 0.1) * 0.2

        # Draw the point light
        ax.add_patch(plt.Circle((light['x'], light['y']), light['radius'], color='white'))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 200), interval=20)

# Display the animation
plt.show()
