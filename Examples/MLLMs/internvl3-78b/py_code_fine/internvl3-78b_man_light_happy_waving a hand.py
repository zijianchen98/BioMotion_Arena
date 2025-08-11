
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure to hold the plot
fig = plt.figure(facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')
ax.axis('off')
ax.set_aspect('equal')

# Coordinates of each point forming a stick figure
# Each row represents (x, y, visibility)
stick_figure_points = np.array([
    [0, -1, 1], [0.4, -0.4, 1], [0, 0.5, 1], [-0.4, -0.4, 1], [0, 0.4, 1],
    [-0.2, 0.2, 1], [0.2, 0.2, 1], [-0.8, -0.8, 1], [0.8, -0.8, 1], [-0.2, -0.4, 1],
    [0.2, -0.4, 1], [0.1, 0.3, 1], [-0.1, 0.3, 1], [-0.1, -0.9, 1], [0.1, -0.9, 1]
])

# Generate the animation
def animate(i):
    ax.clear()
    ax.axis('off')
    ax.set_aspect('equal')
    
    angle = (i % 90) * (np.pi / 180)  # Update angle for oscillatory motion
    amplitude = 0.5 * np.sin(theta + angle)  # Oscillatory amplitude
    height_variation = np.cos(theta - angle)  # Height variation
    
    for coord in stick_figure_points:
        x = coord[0] + amplitude
        y = coord[1] + height_variation
        if coord[2]:
            ax.plot(x, y, 'w.', markersize=10)

theta = np.linspace(0, 2 * np.pi, len(stick_figure_points))

# Create a 3000-frame animation which depicts wave-like motion
anim = animation.FuncAnimation(fig, animate, frames=3000, interval=10, blit=False)
plt.show()
