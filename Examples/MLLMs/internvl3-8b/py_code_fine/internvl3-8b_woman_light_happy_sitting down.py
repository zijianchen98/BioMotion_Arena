
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define initial positions of the 15 points for the seated woman
points = np.array([
    [0.2, 0.0], [0.2, 0.1], [0.2, 0.2], [0.2, 0.3], [0.2, 0.4],
    [0.3, 0.1], [0.3, 0.2], [0.3, 0.3], [0.3, 0.4],
    [0.4, 0.2], [0.5, 0.1], [0.5, 0.2], [0.6, 0.1], [0.6, 0.2], [0.6, 0.3]
])

def update_positions(data):
    # Update the positions of the points in a smooth manner
    points[:, 1] += 0.01  # Move down
    points[3, 0] += 0.01  # Move slightly to the right for a sitting action
    return [data]

fig = plt.figure()
ax = plt.axes(x_lim=[0, 1], y_lim=[0, 1])
x, = ax.plot([], [], 'o', color='white')
animation = animation.FuncAnimation(
    fig, update_positions, fargs = (x,), frames=150, interval=50)

plt.axis('off')  # Hide the axes
plt.show()
