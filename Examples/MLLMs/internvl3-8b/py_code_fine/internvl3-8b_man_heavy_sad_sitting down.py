
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 5

# Initial positions of the points (in the example, we'll create a simple shape)
xs = np.random.randint(0, 10, num_points)
ys = np.random.randint(0, 10, num_points)

fig, ax = plt.subplots()
scat = ax.scatter(xs, ys, s=50, c='white')

def update(frame):
    scat.set_offsets(np.random.rand(num_points, 2) * 10)
    scat.set_color('white')  # Ensure they are white
    return scat,

ani = animation.FuncAnimation(fig, update, frames=200, interval=10, blit=True)
plt.show()
