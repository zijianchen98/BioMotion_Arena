
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of light points
num_points = 15

# Define the initial positions of the points
points = np.array([[-3, 1], [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1], [3, 1],
                   [-3, -1], [-2, -1], [-1, -1], [0, -1], [1, -1], [2, -1], [3, -1]])

# Define initial velocities for X and Y axes separately (random to simulate realism)
velocities = np.random.uniform(-0.1, 0.1, size=(2, num_points))

# Background color
background_color = 'black'
circle_color = 'white'

fig, ax = plt.subplots()
ax.set_facecolor(background_color)
ax.set_xlim([-4, 4])
ax.set_ylim([-2, 2])
ax.set_axis_off()

# Creating the animation function
def animate(i):
    circle = plt.Circle((0, 0), radius=0.1, fc=circle_color, linewidth=0.2)
    ax.add_artist(circle)
    # Update positions based on velocities
    new_points = np.array([(pts[0] + velocities[0][i], pts[1] + velocities[1][i])
                           for pts in points])
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim([-4, 4])
    ax.set_ylim([-2, 2])
    ax.set_axis_off()
    # Plot each point
    for p in range(num_points):
        ax.add_patch(plt.Circle((new_points[p][0], new_points[p][1]), 0.1, fc='none', edgecolor='white'))
    return [circle,]

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.05), interval=20, blit=False, save_count_code='tiff', repeat=False)
plt.show()
