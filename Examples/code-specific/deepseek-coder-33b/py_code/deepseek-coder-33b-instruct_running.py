
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the number of points
n = 15

# Set the initial positions of the points
pos = np.random.rand(2, n)

# Set the initial velocities of the points
vel = np.random.rand(2, n)

# Set the points
scat = ax.scatter(pos[0,:], pos[1,:], s=100, c='w')

def update(num):
    global pos, vel
    # Update the positions of the points
    pos = pos + vel

    # Bounce the points off the walls
    for i in range(2):
        pos[i, pos[i,:] > 1] = 2 - pos[i, pos[i,:] > 1]
        vel[i, pos[i,:] > 1] = -vel[i, pos[i,:] > 1]
        pos[i, pos[i,:] < 0] = -pos[i, pos[i,:] < 0]
        vel[i, pos[i,:] < 0] = -vel[i, pos[i,:] < 0]

    # Update the scatter plot
    scat.set_offsets(pos.T)

# Set the axis limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# Turn off the axis
ax.axis('off')

ani = animation.FuncAnimation(fig, update, interval=50)

plt.show()
