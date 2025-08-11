
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_facecolor('black')

# Define the coordinates for the 15 point lights
points = [
    (0.25, 0.65, 0.8), (0.75, 0.65, 0.8), 
    (0.25, 0.35, 0.5), (0.75, 0.35, 0.5), 
    (0.25, 0.05, 0.2), (0.75, 0.05, 0.2), 

    (0.25, 0.75, 0.8), (0.75, 0.75, 0.8), 
    (0.25, 0.25, 0.5), (0.75, 0.25, 0.5),

    (0.25, 0.1, 0.2), (0.75, 0.1, 0.2), 
    (0.25, 0.95, 0.8), (0.75, 0.95, 0.8), 
    (0.25, 0.45, 0.5), (0.75, 0.45, 0.5), 

    (0.25, 0.3, 0.4), (0.75, 0.3, 0.4)
]

# Function to update the position of the point lights
def update(frame):
    coords = np.array(points)
    new_coords = coords + np.linspace([0, 0, 0], [0, 0, 0], 60) * frame / 60
    for c, pos in zip(range(15), new_coords):
        ax.plot(pos[0], pos[1], pos[2], 'o').set_size(50 * np.exp(-0.1 * abs(pos[1] - 0.3)))

# Animate the figure
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 60), interval=50, blit=False)
plt.show()
