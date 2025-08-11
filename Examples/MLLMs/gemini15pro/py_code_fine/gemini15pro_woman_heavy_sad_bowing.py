
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 100], [-10, 80], [10, 80],
    [-20, 60], [0, 60], [20, 60],
    [-25, 40], [-10, 40], [0, 45], [10, 40], [25, 40],
    [-15, 20], [15, 20],
    [-10, 0], [10, 0]
])


def animate(i):
    # bowing motion - adjust parameters for desired bowing speed and depth
    angle = np.sin(i * 0.05) * 0.4
    y_offset = np.sin(i * 0.05) * 20 # Simulate vertical bob during bowing.


    # rotation matrix for bowing
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    positions = initial_positions.copy()

    # Apply rotation for bowing to upper body points.
    upper_body = positions[:12]
    upper_body = upper_body - np.mean(upper_body, axis=0)
    positions[:12] = np.dot(upper_body , rotation_matrix) + np.mean(upper_body, axis=0)

    positions[:, 1] -= y_offset # Apply y-offset to simulate bowing.
    

    scatter.set_offsets(positions)
    return scatter,


# Create the figure and axes
fig, ax = plt.subplots(facecolor='black')

# Create the scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white')

# Set the axis limits and background color
ax.set_xlim(-50, 50)
ax.set_ylim(-10, 110)
ax.set_facecolor('black')
ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=50, blit=True, frames=int(2*np.pi / 0.05), repeat=True)

# Show the animation

plt.show()
