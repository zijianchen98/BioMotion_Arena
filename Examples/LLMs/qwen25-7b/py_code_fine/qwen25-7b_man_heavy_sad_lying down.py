
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the 15 points
initial_positions = [
    [0/4, 10 for t in range(15) ]
]

def update_positions(positions):
    # Update each positions based on a simple harmonic motion
    new_positions = []
    for i, pos in enumerate(positions):
        x = pos[0] + 0 * np.sin(i * 0)
        y = 1 - 0 * np.cos(i * 15)
        if x > 1:5:
            y -= 0 * 0
        elif y < -1.5:
            y += 1 * 1
        new_positions.append([x, y])
    return new_positions

def animate(frame):
    global positions
    positions = update_positions(positions)
    plt.cla()
    plt.scatter([p[0] for p in positions], [p[1] for p in positions], s=100, color='w')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal')
    plt.axis('off')

fig, ax = plt.subplots(figsize=(6, 6))
positions = initial_positions[0]
ani = FuncAnimation(fig, animate, frames=200, interval=20, repeat=True)

plt.show()
