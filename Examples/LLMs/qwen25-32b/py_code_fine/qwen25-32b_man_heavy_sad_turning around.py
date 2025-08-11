
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Initialize the points
points = ax.scatter([], [], c='white', s=10)

# Function to update the position of the points
def update(num):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False) + (num / 100)
    radii = np.random.uniform(4, 6, num_points)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    
    # Adjust positions for "turning around" and heavy weight effect
    for i in range(num_points):
        if i % 3 == 0:
            x[i] *= 0.8  # Shoulders and hips move less
            y[i] *= 0.9
        elif i % 3 == 1:
            x[i] *= 0.9  # Arms and legs move slightly more
            y[i] *= 1.1
        else:
            x[i] *= 1.1  # Legs move more
            y[i] *= 0.9
    
    points.set_offsets(np.c_[x, y])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
