
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# **Constants**
num_points = 15
frames = 100
fps = 30

# **Initial setup for point-lights**
# Define the coordinates for the point-lights based on a running motion
# (These values can be tuned for realism)
x_coords = np.array([
    -0.5,  # Left foot
    -0.3,  # Left knee
    0.0,   # Hip
    0.3,   # Right knee
    0.5,   # Right foot
    -0.2,  # Left hand
    0.2,   # Right hand
    0,     # Center of mass
    -0.4,  # Left shoulder
    0.4,   # Right shoulder
    -0.6,  # Left elbow
    0.6,   # Right elbow
    -0.8,  # Head
    0.8,   # Back of the head
    -0.4,  # Waist
    0.4    # Upper body
])

y_coords = np.array([
    0.0, 0.1, 0.2, 0.1, 0.0,  # Legs
    -0.1, 0.1, 0.0, # Arms and Center of mass
    0.3, 0.3, -0.1, -0.1, # Shoulders and Elbows
    0.5, 0.5, 0.4, 0.4  # Head and Waist
])

# **Create a figure**
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 0.8)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# **Function to initialize the animation**
def init():
    points.set_data([], [])
    return points,

# **Function to update the points for each frame**
def update(frame):
    # Update y-coordinates to simulate running motion
    y_running = y_coords + 0.05 * np.sin(2 * np.pi * (frame / frames) + np.linspace(0, 2 * np.pi, num_points))
    
    points.set_data(x_coords, y_running)
    return points,

# **Create the animation**
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

# **Show the animation**
plt.show()
