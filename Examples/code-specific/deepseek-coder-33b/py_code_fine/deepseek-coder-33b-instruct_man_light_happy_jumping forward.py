
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')

# Create a point light source
point, = ax.plot([], [], 'o', color='white')

# Create a solid black background
ax.set_facecolor('black')

# Initialize the point light source
def init():
    point.set_data([], [])
    return point,

# Update the point light source
def update(frame):
    x = 1 - np.abs(1 - np.mod(frame, 2))
    y = np.sin(frame)
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, blit=True)

# Show the animation
plt.show()
