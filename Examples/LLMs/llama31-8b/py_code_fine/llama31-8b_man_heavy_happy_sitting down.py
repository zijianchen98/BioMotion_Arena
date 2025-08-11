
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create a black background
ax.set_facecolor('black')

# Define the point lights
lights = [
    {'x': 0.5, 'y': 0.3, 'angle': 0, 'radius': 0.05},
    {'x': 0.7, 'y': 0.5, 'angle': 0, 'radius': 0.05},
    {'x': 0.9, 'y': 0.7, 'angle': 0, 'radius': 0.05},
    {'x': 0.1, 'y': 0.5, 'angle': 0, 'radius': 0.05},
    {'x': -0.1, 'y': 0.7, 'angle': 0, 'radius': 0.05},
    {'x': -0.3, 'y': 0.5, 'angle': 0, 'radius': 0.05},
    {'x': -0.5, 'y': 0.3, 'angle': 0, 'radius': 0.05},
    {'x': -0.7, 'y': 0.1, 'angle': 0, 'radius': 0.05},
    {'x': -0.9, 'y': -0.1, 'angle': 0, 'radius': 0.05},
    {'x': -0.1, 'y': -0.3, 'angle': 0, 'radius': 0.05},
    {'x': 0.1, 'y': -0.5, 'angle': 0, 'radius': 0.05},
    {'x': 0.3, 'y': -0.7, 'angle': 0, 'radius': 0.05},
    {'x': 0.5, 'y': -0.9, 'angle': 0, 'radius': 0.05},
    {'x': 0.7, 'y': -0.1, 'angle': 0, 'radius': 0.05},
    {'x': 0.9, 'y': 0.1, 'angle': 0, 'radius': 0.05},
]

# Define the movement parameters
num_frames = 100
frame_duration = 0.05  # seconds

# Define the movement function
def movement(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    for i, light in enumerate(lights):
        # Move the light in a circular motion
        angle = light['angle'] + (frame / num_frames) * 2 * np.pi
        x = light['x'] + np.cos(angle) * 0.2
        y = light['y'] + np.sin(angle) * 0.2
        
        # Update the light position
        light['x'] = x
        light['y'] = y
        light['angle'] = angle
        
        # Draw the light
        ax.add_patch(patches.Circle((x, y), light['radius'], edgecolor='white', facecolor='white', alpha=0.5))

# Create the animation
ani = animation.FuncAnimation(fig, movement, frames=num_frames, interval=frame_duration * 1000)

plt.show()
