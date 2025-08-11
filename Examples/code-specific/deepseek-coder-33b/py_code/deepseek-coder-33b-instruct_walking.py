
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')
ax.grid(False)
ax.set_axis_off()
ax.set_facecolor('k')

# create 15 points
points = np.random.rand(2, 15)

# create 15 scatter points
scat = ax.scatter(points[0], points[1], s=100, facecolor='w', edgecolor='k')

# animation function.  This is called sequentially
def animate(i):
    # update the points
    points[1] = np.sin(points[0] + i/10.0)
    # update the scatter points
    scat.set_offsets(points.T)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, interval=20, blit=False)

plt.show()
