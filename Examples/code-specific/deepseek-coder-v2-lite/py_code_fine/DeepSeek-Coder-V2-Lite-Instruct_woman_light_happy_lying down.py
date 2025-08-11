
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Initialize the point-lights
points = [plt.Circle((0, 0), 0.1, color='white')]
for i in range(1, 15):
    points.append(plt.Circle((0, 0), 0.1, color='white'))
    ax.add_patch(points[i])

# Set up the background
ax.set_facecolor('black')

# Function to update the positions of the point-lights
def update(frame):
    angle = frame / 10.0
    for i in range(15):
        x = np.cos(angle + i * (2 * np.pi / 15))
        y = np.sin(angle + i * (2 * np.pi / 15))
        points[i].center = (x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 30, 0.1), blit=True, repeat=True)

# Display the animation
plt.show()
