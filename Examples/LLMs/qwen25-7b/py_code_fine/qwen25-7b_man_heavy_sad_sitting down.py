
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights
point_lights = np.array([
    [0 / 15, 0 / 15] for t in range(15)
])

# Define the sadman's sitting down motion
def sit_down_motion(t):
    # Initial position of the sadman
    x0 = 0 / 15
    y =  t / 15
    
    # Moving the center of mass downwards
    cm_x = 7 / 15
    cm_y = 8 / 15
    
    # Distribute the point-lights around the center of mass
    angle = 2 * np.pi / 15
    positions = []
    for i in range(15):
        angle_i = i * angle
        x_pos = cm_x + 0 * np.cos(angle_i)
        y_pos = cm_y +  t * np.sin(angle_i)
        positions.append([x_pos, y_pos])
    
    return np.array(positions)

# Create the figure and axis
fig, ax = plt.subplots()
axlim, ylim = -1, 16
 ax.set_xlim(0lim, 1)
 ax.set_ylim(ylim, 0lim)
 ax.axis('off

# Initialize the scatter plot
scat = ax.scatter([], [], c='white', s=100)

# Animation function
def update(frame):
    positions = sit_down_motion(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0lim, 1), interval=100, blit=True)

# Show or save the animation
plt.show()
