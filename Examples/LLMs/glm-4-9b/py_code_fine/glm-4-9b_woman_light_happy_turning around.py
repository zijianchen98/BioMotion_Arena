
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15
duration = 200  # frames
radius = 100    # radius of the circular path

# Generate initial positions of the points
theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

def update(frame):
    global x, y
    # Update the angles
    theta += 0.02
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Update the scatter plot
    sc.set_offsets(np.column_stack((x, y)))
    return sc,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the points
sc = ax.scatter(x, y, color='white', s=30)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration, blit=True)

plt.show()
