
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
num_lights = 15
duration = 100  # frames
fps = 30
dt = 1 / fps

# Define the body segments and their initial positions
# (Simplified representation for demonstration - can be extended)
body = {
    'head': (0, 0),
    'shoulder': (1, 0),
    'elbow': (2, 0),
    'wrist': (3, 0),
    'hip': (0.5, 1),
    'knee': (1.5, 1),
    'ankle': (2.5, 1)
}

# Define the movement patterns for turning around
# This is a simplified example and can be refined for better realism
def movement(frame, speed=0.1):
    for segment in body:
        if segment == 'head':
            angle = frame * speed
            x = 1 + np.cos(angle) * 0.5
            y = 0 + np.sin(angle) * 0.5
        elif segment == 'shoulder':
            angle = frame * speed
            x = 1 + np.cos(angle) * 0.3
            y = 0 + np.sin(angle) * 0.3
        elif segment == 'elbow':
            angle = frame * speed
            x = 2 + np.cos(angle) * 0.2
            y = 0 + np.sin(angle) * 0.2
        elif segment == 'wrist':
            angle = frame * speed
            x = 3 + np.cos(angle) * 0.1
            y = 0 + np.sin(angle) * 0.1
        elif segment == 'hip':
            angle = frame * speed
            x = 0.5 + np.cos(angle) * 0.2
            y = 1 + np.sin(angle) * 0.2
        elif segment == 'knee':
            angle = frame * speed
            x = 1.5 + np.cos(angle) * 0.2
            y = 1 + np.sin(angle) * 0.2
        elif segment == 'ankle':
            angle = frame * speed
            x = 2.5 + np.cos(angle) * 0.1
            y = 1 + np.sin(angle) * 0.1
        else:
            x, y = body[segment]
        
        body[segment] = (x, y)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
lights = []
for _ in range(num_lights):
    lights.append(plt.Circle((0, 0), radius=0.03, color='white'))

# Initialize the animation
ani = animation.FuncAnimation(fig, update, frames=duration, interval=dt*1000, blit=True, repeat=True)

# Update function
def update(frame):
    for light in lights:
        light.center = (0, 0)  # Move all lights to the center
    movement(frame)
    for light in lights:
        light.center = body['head']
    return lights

# Save the animation (optional)
# ani.save("turning_around.gif", writer='pillow', fps=fps)

plt.show()
