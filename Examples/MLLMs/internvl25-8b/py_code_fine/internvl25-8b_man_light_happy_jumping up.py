
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure
fig, ax = plt.subplots(figsize=(10,20))
ax.set_xlim(0, 100)
ax.set_ylim(0, 400)
ax.axis('off')

# Create the dots
n_points = 15
points = [ax.scatter((i+1), np.random.uniform(100, 400), color='white', s=1000)]
for _ in range(n_points-1):
    points.append(ax.scatter(np.random.uniform(0, 100), np.random.uniform(100, 400), color='white', s=1000))

def init():
    for i in range(len(points)):
        points[i].set_offsets((np.random.randi(np.arange(0, 100)) / 100, np.random.randi(np.arange(300, 400)) / 100))
    return points

def update(frame):
    for point in points[1:]:
        point.set_offsets((point.get_offsets()[0][0] + (frame % 10) * 10, point.get_offsets()[0][1] + (frame % 5) * 10))
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, interval=30, blit=False)

# Display the animation
plt.show()
