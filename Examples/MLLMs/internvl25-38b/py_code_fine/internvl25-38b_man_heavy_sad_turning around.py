
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
radius = 10
theta_amplitude = np.pi / 3
frames = 360
speed = 2 * np.pi / frames

# Initialize plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-radius - 1, radius + 1)
ax.set_ylim(-radius - 1, radius + 1)
ax.axis('off')

# Create initial point locations
angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
points = np.array([np.cos(angles), np.sin(angles)]).T * radius

# LineCollection
line, = ax.plot([0], [0], 'wo')

def update(frame):
    global points
    angle = frame * speed
    sin_component = np.sin(angle)
    cos_component = np.cos(angle)
    
    # Apply a transformation to simulate turning animation
    rotation_matrix = np.array([[cos_component, -sin_component], [sin_component, cos_component]])
    points = np.dot(points, rotation_matrix)
    
    # Set new points
    line.set_data(points.T)

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=False)
plt.show()
