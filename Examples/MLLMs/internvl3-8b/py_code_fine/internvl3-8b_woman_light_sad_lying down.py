
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial position of the points
initial_positions = np.array([
    [25, 75], [30, 70], [35, 66], [40, 62], [45, 60], 
    [25, 56], [30, 52], [35, 48], [40, 46], [45, 40], 
    [35, 68], [30, 73], [25, 64], [35, 58], [40, 52]
])

def update_positions(positions):
    # Simulate natural motion (e.g., small random movements)
    return positions + np.random.uniform(-0.5, 0.5, positions.shape)

def animate(frame, positions, scatter):
    positions = update_positions(positions)
    scatter.set_offsets(positions)
    return scatter,

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

# Create a scatter plot with the initial positions
scat = ax.scatter(*initial_positions.T, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, fargs=(initial_positions, scat), interval=100, blit=True)

# Show the animation
plt.show()
