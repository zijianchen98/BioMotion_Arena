
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0 / 14 * 10 for t in range(15) ] for t in range(15)
])

def update_light_positions(frame, positions, points):
    # Update the positions based on a simple biomechanical model
    for i in range(15):
        positions[i] += np.random.normal(scale=0.1)  # Add some noise for natural movement
        if positions[i] > 1 or positions[i] < 0:
            positions[i] -= np.random.normal(scale=0.1)  # Bounce back if it goes out of bounds
    
    for point, pos in zip(points, positions):
        point.set_data(pos)
    
    return points

fig, ax = plt.subplots()
ax, ax.plot(initial_positions[0], 'o', color='white')
ax, ax.set_xlim(0, 1)
ax, ax.set_ylim(0, 1)
ax, ax.set_aspect('equal')
ax, ax.axis('off')

ani = animation.FuncAnimation(fig, update_light_positions, fargs=(initial_positions, lights), interval=10ms, frames=150)

plt.show()
