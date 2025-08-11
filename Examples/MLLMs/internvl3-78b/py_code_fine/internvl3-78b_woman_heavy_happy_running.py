
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the trajectory of the point-lights
x = lambda t: np.sin(t)
y = lambda t: np.cos(t)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the point-lights
point_lights, = ax.plot([], [], 'bo')

# Function to update the position of the point-lights
def update(t):
    point_lights.set_data(x(t), y(t))
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), blit=True)

# Show the animation
plt.show()
