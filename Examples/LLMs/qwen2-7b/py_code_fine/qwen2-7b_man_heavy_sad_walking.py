
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot((autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10))
ax.set_aspect('equal')
ax.grid()

# Man
man = plt.Circle((0, 0), 0.75, color='w', zorder=2)

# Animation
def animate(i):
    # Generate new positions
    x = np.cos(i * 0.05)
    y = np.sin(i * 0.05)
    
    # Update man position
    man.center = (x, y
    
    return man,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange((0, 120), interval=20, blit=True)

plt.show()
