
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 100  # Frames
fps = 30
fig_size = (8, 8)
point_radius = 0.05

# Define the sadman's turning motion
def sadman_motion(frame):
    # This is a simplified motion model.  A more sophisticated model
    # would use kinematic equations and potentially incorporate
    # muscle activation data for increased realism.

    # Simple turning motion around the vertical axis
    angle = frame / fps * np.pi * 2  # Rotate from 0 to 2*pi over 100 frames
    
    # Define coordinates of the points - roughly mimicking the sadman's body
    points = []
    for i in range(num_points):
        # Create a circle-like motion, adjusted by the angle
        x = 0.5 + 0.3 * np.cos(i * 2 * np.pi / num_points + angle)
        y = 0.5 + 0.3 * np.sin(i * 2 * np.pi / num_points + angle)
        points.append((x, y))
    
    return points

# Create the figure and axes
fig, ax = plt.subplots(figsize=fig_size)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(-0.7, 0.7)

# Create the points
points = []
for i in range(num_points):
    points.append(plt.scatter(0, 0, s=point_radius * 100, color='white')) # Adjusted size for visibility

# Animation function
def animate(frame):
    points_data = sadman_motion(frame)
    for i, p in enumerate(points):
        p.set_data(*points_data[i])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation
ani.save('sadman_turning.gif', writer='pillow', fps=fps)

plt.show()
