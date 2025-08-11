
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights (approximating a jumping man)
positions = {
    'head': [4, 0],
    'shoulders': [[3, 1], [5, 1]],
    'elbows': [[2.5, 2], [3.5, 2], [4.5, 2], [5.5, 2]],
    'hands': [[2.25, 3], [3.75, 3], [4.25, 3], [5.75, 3]],
    'hips': [[3, 2], [5, 2]],
    'knees': [[2.5, 3], [3.5, 3], [4.5, 3], [5.5, 3]],
    'feet': [[2, 4], [4, 4], [5, 4], [6, 4]]
}

def init():
    """Initialize the plot."""
    for part, coords in positions.items():
        if isinstance(coords[0], list):
            for coord in coords:
                scat = ax.scatter(coord[0], coord[1], color='white')
        else:
            scat = ax.scatter(coords[0], coords[1], color='white')

def animate(i):
    """Animate the point-lights."""
    amplitude = 0.5 * (i % 20) / 20
    for part, coords in positions.items():
        if isinstance(coords[0], list):
            for coord in coords:
                coord[1] += amplitude
        else:
            coords[1] += amplitude

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 6)
ax.set_facecolor('black')
plt.axis('off')

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=70, blit=False, repeat=True)

plt.show()
