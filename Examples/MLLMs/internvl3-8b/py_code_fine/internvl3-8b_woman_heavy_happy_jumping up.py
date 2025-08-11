
# Import necessary libraries
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights
def get_positions():
    # Positions based on example image (a simple representation)
    positions = [
        [np.random.randint(50), np.random.randint(20)] for _ in range(5)
    ]
    return positions

def update_positions(positions):
    # Simulate a natural jumping motion
    for i in range(5):
        x, y = positions[i]
        y = 20 * np.sin(x/50 + i*0.5) + 10
        positions[i] = [x, int(y)]
    return positions

def animate(i, artist, positions):
    positions = update_positions(positions)
    artist.set_data(np.array(positions)[:, 0], np.array(positions)[:, 1])
    return artist,

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Place point-lights
positions = get_positions()
scatter = ax.scatter(np.array(positions)[:, 0], np.array(positions)[:, 1], color='white')

# Create animation
ani = FuncAnimation(
    fig, animate, frames=None, fargs=(scatter, positions), interval=50, repeat=True
)

plt.show()
