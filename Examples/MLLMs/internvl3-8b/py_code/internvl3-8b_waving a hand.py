
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define animation frames
def animate(i):
    current_points = points[:, :i+1]
    min_x = np.min(current_points[:, 0])
    max_x = np.max(current_points[:, 0])
    min_y = np.min(current_points[:, 1])
    max_y = np.max(current_points[:, 1])
    x_ticks = np.linspace(min_x, max_x, 11)
    y_ticks = np.linspace(min_y, max_y, 11)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    
    for j in range(i+1):
        plt.plot(current_points[j, 0], current_points[j, 1], 'w,')
    return ax

# Set up initial figure
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Initial points
frame_length = 50
n_points = 15

# Create wave pattern
points = np.zeros((n_points, frame_length))
points[0] = [0, 20]
for j in range(1, n_points-1):
    points[j] = [j*2, (-1)**j*(5+j*2)]
points[n_points-1] = [((n_points-2)*2)+10, 20]

# Animation
ani = animation.FuncAnimation(fig, animate, frames=frame_length, blit=True)
plt.show()
