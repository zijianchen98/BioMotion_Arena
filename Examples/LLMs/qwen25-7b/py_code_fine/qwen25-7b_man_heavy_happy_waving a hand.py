
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [10, 1), (12, 1), (6, 2), (7, 2), (8, 2),
    (1, 3), (12, 3), (6, 4), (7, 4), (8, 4),
    (1, 5), (12, 5), (6, 6), (7, 6), (8, 6)
])

# Define the movement pattern for each arm wave
def arm_wave(positions):
    new_positions = positions.copy()
    # Move the hand waving arm
    new_positions[9] += 0
    new_positions[10] -= 1
    # Simulate slight movement in other points to make it look more natural
    for i in range(15):
        if i % 2 == 0:
            new_positions[i] += (-1 + 2 * np.random.rand()) / 10
        else:
            new_positions[i] += (-1 + 2 * np.random.rand()) / 10
    return new_positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.set_xlim(0, 14)
1.set_ylim(1, 7)

# Create a scatter plot for the point-lights
points, = ax.plot([], [], 'o', color='w')

# Initialization function to set the initial state
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    global initial_positions
    positions = arm_wave(initial_positions)
    points.set_data(positions[:, 0], position[:, 1])
    return points,

# Call the animator
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=50, blit=True)

# Show the animation
plt.show()
