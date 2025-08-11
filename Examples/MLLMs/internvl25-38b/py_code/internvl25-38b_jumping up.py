
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define the point lights
n_dots = 15
dots = [ax.plot([], [], 'o', color='white', ms=5)[0] for _ in range(n_dots)]

# Initial positions and velocities for a jumping motion
initial_positions = np.array([
    [5, 5], [4.5, 6], [5.5, 6], [4, 7], [5, 7], [6, 7], [5.5, 8], [4.5, 8],
    [4, 9], [5, 9], [6, 9], [4.8, 10], [5.2, 10], [4.6, 11], [5.4, 11]
])
velocities = np.array([
    [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5],
    [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5], [0, 0.5]
])

# Define the update function for the animation
def update(frame):
    global initial_positions, velocities
    new_positions = initial_positions + frame * velocities
    
    # Apply gravity effect to make the jump more realistic
    for i in range(n_dots):
        if new_positions[i, 1] > 9:
            velocities[i, 1] = -velocities[i, 1] * 0.8
        elif new_positions[i, 1] < 5:
            velocities[i, 1] = -velocities[i, 1]
    
    for i, dot in enumerate(dots):
        dot.set_data(new_positions[i])
        
    return dots

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(20), blit=True, interval=100)

plt.show()
