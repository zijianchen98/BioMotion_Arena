
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the walking motion parameters
num_points = 15
walk_speed = 0.05
frame_rate = 30
total_frames = int(2 * walk_speed * frame_rate)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
point_lights = [plt.Circle((0, 0), 0.02, color='white') for _ in range(num_points)]
for light in point_lights:
    ax.add_artist(light)

def update(frame):
    # Clear the previous positions
    for light in point_lights:
        light.center = (0, 0)
    
    # Update the positions based on the walking motion
    angle_step = 2 * np.pi / num_points
    for i in range(num_points):
        angle = angle_step * i + frame * walk_speed * 2 * np.pi
        radius = 0.8 - 0.4 * np.cos(angle)
        x = radius * np.sin(angle)
        y = radius * np.cos(angle)
        point_lights[i].center = (x, y)
    
    return point_lights

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=int(1000 / frame_rate), blit=True)

# Show the animation
plt.show()
