
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 points for the "happy man" bowing
positions = np.array([
    [0, 0 ] for t in range(15)
])

def update_points(num, points, lines):
    for line, pos in zip(lines, points):
        x, y = pos[num]
        line.set_data([*], [*])
    return lines

fig, ax = plt.subplots()
ax, = ax.plot([], [], 'o', color='white')
lines = [ax for _ in range(15)]

# Set up the axes
ax.set_xlim(-10, 15)
y.set_ylim(-1, 1)

# Initialization function to reset the plot
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Call the animator
anim = animation.FuncAnimation(fig, update_points, frames=300, fargs=(positions, lines), init_func=init, blit=True)

# Show or save the animation
plt.show()
