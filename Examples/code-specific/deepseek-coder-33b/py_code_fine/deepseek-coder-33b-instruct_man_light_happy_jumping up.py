
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

# Create a point
point, = ax.plot([0], [0], 'o')

# Function to update the animation
def update(num):
    point.set_data(num, np.sin(num))
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                              interval=50, blit=True)

# Show the animation
plt.show()
