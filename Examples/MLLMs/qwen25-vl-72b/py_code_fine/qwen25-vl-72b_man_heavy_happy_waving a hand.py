
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0, 0], [1, 0], [2, 0],
    [0, 1], [1, 1], [2, 1],
    [0, 2], [1, 2], [2, 2],
    [0, 3], [1, 3], [2, 3],
    [1, 4], [1, 5], [1, 6]
])

# Define the movement of each point over time
def update_points(num):
    global points
    x = points[:, 0]
    y = points[:, 1]

    # Update the position of each point based on the specified action
    if num % 2 == 0:
        x[0] += 0.1
        x[1] -= 0.1
        x[2] += 0.1
        x[3] -= 0.1
        x[4] += 0.1
        x[5] -= 0.1
        x[6] += 0.1
        x[7] -= 0.1
        x[8] += 0.1
        x[9] -= 0.1
        x[10] += 0.1
        x[11] -= 0.1
        x[12] += 0.1
        x[13] -= 0.1
        x[14] += 0.1
    else:
        x[0] -= 0.1
        x[1] += 0.1
        x[2] -= 0.1
        x[3] += 0.1
        x[4] -= 0.1
        x[5] += 0.1
        x[6] -= 0.1
        x[7] += 0.1
        x[8] -= 0.1
        x[9] += 0.1
        x[10] -= 0.1
        x[11] += 0.1
        x[12] -= 0.1
        x[13] += 0.1
        x[14] -= 0.1

    points[:, 0] = x
    points[:, 1] = y

    return points

# Create the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 7)
ax.set_facecolor('black')

# Create the scatter plot for the points
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the animation function
def animate(num):
    global points
    points = update_points(num)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
