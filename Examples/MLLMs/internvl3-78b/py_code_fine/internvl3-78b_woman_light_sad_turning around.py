
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
num_points = 15
background_color = 'black'
point_color = 'white'
figure_size = (8, 8)
num_frames = 100
radius = 0.4
speed = 0.05

# Setup the figure and axis
fig, ax = plt.subplots(figsize=figure_size)
ax.set_facecolor(background_color)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
ax.axis('off')

# Initial positions of points (randomly distributed on a circle)
angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
points = np.array([radius * np.cos(angles), radius * np.sin(angles)]).T

# Create point objects
scatter = ax.scatter(points[:, 0], points[:, 1], color=point_color)

def update(frame):
    global points
    # Move points
    points = np.dot(points, np.array([[np.cos(speed * frame), -np.sin(speed * frame)],
                                      [np.sin(speed * frame), np.cos(speed * frame)]]))
    
    # Update scatter plot
    scatter.set_offsets(points)
    return scatter,

# Animate
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
