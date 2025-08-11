
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
dots, = ax.plot([], [], 'wo', markersize=10)

# Joint positions for a jumping motion
initial_positions = np.array([
    [-0.2, 0.8], [0, 0.8], [0.2, 0.8],
    [-0.3, 0.6], [-0.1, 0.6], [0.1, 0.6], [0.3, 0.6],
    [-0.2, 0.4], [0, 0.4], [0.2, 0.4],
    [-0.25, 0.2], [-0.15, 0.2], [0.15, 0.2], [0.25, 0.2],
    [0, -0.5], [0, -0.7]
])

def init():
    dots.set_data([], [])
    return dots,

def animate(t):
    # Calculate displacement due to jumping
    y_displacement = 0.5 * np.sin(np.pi * t / 10)
    
    # Apply displacement to the joints
    positions = initial_positions.copy()
    positions[:, 1] += y_displacement
    
    # Slow down to simulate heavy weight
    positions[:, 1] *= 0.8
    
    dots.set_data(positions[:, 0], positions[:, 1])
    return dots,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=range(20), init_func=init, blit=True, interval=100, repeat=True)

plt.axis('off')
plt.show()
