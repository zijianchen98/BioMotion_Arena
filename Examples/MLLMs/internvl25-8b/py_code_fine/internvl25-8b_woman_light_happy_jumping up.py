
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of dots
num_dots = 15

# Set the figure size
fig, ax = plt.subplots(figsize=(5, 8))

# Initialize the positions of the dots
dots = np.zeros((num_dots, 2))
dots = np.array([(x, 0.5 - np.sin(np.linspace(-2 * np.pi, 0, num_dots))) for x in range(num_dots)])

# Set the colormap for the dots
colors = plt.cm.coolwarm(np.linspace(0, 1, num_dots))

# Function to update the positions of the dots
def update(deltat):
    for i in range(num_dots):
        angle = np.sin(np.linspace(0, 2 * np.pi * (np.sqrt((i + 1) / num_dots) * deltat), 3)[i])
        dots[i, 1] = np.sin(angle)
    ax.clear()
    ax.plot(dots[:, 0], dots[:, 1], 'o', c=colors, markersize=2)
    ax.set_xlim([-1, num_dots])
    ax.set_ylim([-1, 1])

# Animation duration
duration = 2

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=1000 / length(frameInterval), frames=frameCount, repeat=False, blit=False, save_count=True, savefig_dpi=100)

# Set the animation size
fig.tight_layout()

# Show the plot
plt.show()
