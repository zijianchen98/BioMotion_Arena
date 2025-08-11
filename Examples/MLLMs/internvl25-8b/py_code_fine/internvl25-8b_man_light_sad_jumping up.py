
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 12)
ax.set_axis_off()

# Create a scatter object and populate it with white points
points = [plt.Rectangle((i, j), 0.1, 0.1, edgecolor='white', facecolor='black') for i in range(15)]
scatter = ax.scatter([], [], c='white', s=100)

# Function to animate the jumping motion
def animate(i):
    y_positions = np.sin(np.linspace(0, np.pi, 15) * (i / 30)) + np.linspace(i/3, i/2, 15) * 2
    current_y = np.sin(np.linspace(0, np.pi, 15) * (i / 30))
    scatter.set_offsets([(i, current_y + y_positions[j]) for j in range(15)])
    scatter.set_ydata(y_positions)

    # Simulate the jumping up motion
    current_position = np.linspace(0.5, 0, 15)
    if i == 30:
        current_position = np.linspace(10, 0, 15)

    return [p.set_xdata([(i - 0.2, current_position[j]) for j in range(15)]) for p in points]

# Animate the jumping motion
ani = animation.FuncAnimation(fig, animate, frames=range(0, 61), interval=50, blit=True)

# Show the animation
plt.show()
