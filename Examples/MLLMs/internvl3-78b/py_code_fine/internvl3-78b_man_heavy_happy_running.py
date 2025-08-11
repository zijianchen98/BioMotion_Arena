
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    """Initialize the plot objects."""
    scat.set_offsets(np.c_[x, y])
    return scat,

def update(t):
    """Update the positions of the point-lights."""
    global x, y
    for i in range(len(x)):
        x[i] += np.cos(angles[i]) * speed[i]
        y[i] += np.sin(angles[i]) * speed[i]
        # Periodic boundary conditions
        if x[i] > 66 or x[i] < -5: 
            x[i] = -66 if x[i] > 66 else 66
        if y[i] > 33 or y[i] < -33:
            y[i] = -33 if y[i] > 33 else 33
    scat.set_offsets(np.c_[x, y])
    return scat,

# Initializing positions, speeds, and angles for each light point
np.random.seed(42)
x = np.random.uniform(-33, 33, 15)
y = np.random.uniform(-16, 16, 15)
speed = np.random.uniform(1, 2, 15)
angles = np.random.uniform(0, 2 * np.pi, 15)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(-5, 66)
ax.set_ylim(-33, 33)
ax.set_facecolor('k')
scat = ax.scatter(x, y, c='w', s=100)

ani = animation.FuncAnimation(fig, update, init_func=init, frames=1000, 
                              interval=60, blit=True, repeat=True)

plt.show()
