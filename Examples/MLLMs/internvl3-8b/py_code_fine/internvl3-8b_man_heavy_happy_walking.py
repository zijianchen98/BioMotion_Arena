
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Number of points
num_points = 15

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot initial positions
points = ax.scatter(
    [1.0]*num_points,
    [1.0]*num_points,
    [0]*num_points,
    c='white',
    s=100,
    alpha=1.0
)
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])
ax.set_aspect('equal')

def update_positions(frame):
    # Example of a smooth, biomechanically plausible path for a walking human
    x = 4 * np.random.rand(num_points) - 2
    y = 6 * np.random.rand(num_points) - 3
    z = np.arange(-16, 4, 1.6)
    
    points._offsets3d = (x, y, z)
    # Rotate the view a bit for better visual appeal
    ax.view_init(elev=20, azim=frame)
    return points,

ani = animation.FuncAnimation(fig, update_positions, frames=range(500), blit=True)
plt.show()
