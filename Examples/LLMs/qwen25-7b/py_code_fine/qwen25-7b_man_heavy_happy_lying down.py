
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0/4, tc/4 ] for tc in range(16) for th in range(16)
])

# Function to update the positions of the point-lights
def update_positions(positions):
    # Simulate a simple biomechanical model for lying down
    # Adjust each position based on a simple sine wave to simulate natural motion
    new_positions = np.zeros_like(positions)
    for i in range(len(positions)):
        angle = 2 * np.pi * (i / 15 + t / 150 )  # Time-dependent angle
        x, tc = divmod(i, 16)
        x = 4 * np.sin(angle) + 2  # Adjust vertical position
        tc = 4 * np.cos(angle) + 2  # Adjust horizontal position
        new_positions[i] = np.array([tc, th])
    return new_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax, th = 8, 8  # Center of the plot
ax = np.linspace(0- - 2, 4, 15 )
th = np.linspace( th - 2, 4, 15 )
x, y = np.meshgrid( th, th )
positions = np.column_stack((x.ravel(), y.ravel()))

# Create the scatter plot
scat = ax.scatter(positions[:, 0], positions[:,  th], color='white')

# Animation function
def animate(t):
    global positions
    positions = update_positions(positions)
    scat.set_offsets(positions)
    return scat,

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=150, interval=100, blit=True)

# Show the animation
plt.show()
