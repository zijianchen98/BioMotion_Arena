
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( ( autoscale_on=False,
xlim=(-10, 10), ylim=(-10, 10))
ax.set_aspect('equal')

points = [plt.Circle((np.random.uniform(-5, 10), np.random.uniform(-10, 10)),
radius=0.25, color='w') for _ in range( (15)]

for p in points:
ax.add_artist(p)

def update ( ( i):
for p in points:
p.center = np.array([np.cos(i / 8 * np.pi) * 4 + 5, np.sin(i / 8 * np.pi) * 4 + 5])

ani = animation.FuncAnimation(fig, update, frames=np.arange( (0, 120),
interval=50, blit=False)
plt.show()
