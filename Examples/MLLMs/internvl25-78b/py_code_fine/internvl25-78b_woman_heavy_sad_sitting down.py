
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
points = ax.scatter([], [], s=100, color='white')

n_points = 15
positions = np.random.rand(n_points, 2)

def init():
    points.set_offsets(np.zeros((n_points, 2)))
    return points,

def update(frame):
    global positions
    new_positions = np.copy(positions)
    
    # Simulate sitting down motion
    for i in range(n_points):
        if positions[i, 1] > 0.1:
            new_positions[i, 1] -= 0.01
    
    positions = new_positions
    points.set_offsets(positions)
    
    return points,

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
plt.axis('off')
plt.show()
