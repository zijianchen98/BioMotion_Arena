
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define initial positions of the lights to form a sad man sitting down
positions = [
    (0.5, 0.2), (0.45, 0.3), (0.55, 0.3),  # Head
    (0.4, 0.45), (0.4, 0.6), (0.5, 0.55),  # Body
    (0.45, 0.6), (0.55, 0.6), (0.47, 0.65), (0.53, 0.65),  # Legs
    (0.3, 0.55), (0.35, 0.45), (0.65, 0.45), (0.6, 0.55),  # Arms
    (0.4, 0.5), (0.6, 0.5)  # Feet
]

positions = np.array(positions)

# Animation function
def update(frame):
    fig.clear()
    for i in range(len(positions)):
        x, y = positions[i]
        # Simple oscillation to simulate the sitting motion
        if i < 2:  # Head
            y += 0.02 * np.sin(frame / 10)
        elif 2 <= i < 4:  # Body
            y += 0.01 * np.sin(frame / 20)
        elif 4 <= i < 10:  # Legs
            y += 0.03 * np.sin(frame / 15) * (1 if i % 2 == 0 else -1)
        elif 10 <= i < 14:  # Arms
            x += 0.01 * np.sin(frame / 20) * (1 if i % 2 == 0 else -1)
        elif i == 14:  # Feet
            x += 0.01 * np.cos(frame / 20)
        pos[i] = (x, y)
    
    # Plot the points
    x_data, y_data = zip(*pos)
    plt.scatter(x_data, y_data, color='white', s=50)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

# Initialize position variable
pos = positions.copy()

# Create figure and animate
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=False)
plt.show()
