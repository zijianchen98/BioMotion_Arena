
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a new figure
fig = plt.figure()

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)

# Generate random data
data = np.random.rand(15, 2)

# Plot the point-lights
scat = plt.scatter(data[:, 0], data[:, 1],
                   s=50, c='w', edgecolors='w')

# Set the plot limits to x/y axis
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Animation function
def update(frame_number):
    data[:, 1] = np.random.rand(15)
    scat.set_offsets(data)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=50)

# Show the animation
plt.show()
