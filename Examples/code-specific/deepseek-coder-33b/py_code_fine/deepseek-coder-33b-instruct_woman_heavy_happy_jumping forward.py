
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

# Create a list to hold the point-lights
points = []

# Create the point-lights
for i in range(15):
    point, = ax.plot([], [], 'o', color='white')
    points.append(point)

# Function to update the point-lights
def update(num):
    for i, point in enumerate(points):
        x = np.linspace(0, 2, 1000)
        y = np.sin(x + num/10.0 + i*np.pi/6)
        point.set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, blit=True)

# Show the animation
plt.show()
