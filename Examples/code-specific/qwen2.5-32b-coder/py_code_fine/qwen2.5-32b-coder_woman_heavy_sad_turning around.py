
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
background_color = 'black'
point_light_color = 'white'
frames = 100
interval = 50

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor=background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the point lights
theta = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)
r = np.random.uniform(0.2, 0.4, num_lights)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create scatter plot for point lights
scat = ax.scatter(x, y, s=100, color=point_light_color)

# Function to update the positions of the point lights
def update(frame):
    # Update angles for turning around motion
    theta += 0.05
    x = r * np.cos(theta + frame * 0.1)  # Adding frame * 0.1 for rotation effect
    y = r * np.sin(theta + frame * 0.1)
    
    # Apply a slight downward shift to simulate weight
    y -= 0.01 * np.sin(frame * 0.1)
    
    # Update scatter plot data
    scat.set_offsets(np.c_[x, y])

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

# Show the animation
plt.show()
