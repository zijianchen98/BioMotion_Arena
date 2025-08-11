
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 0.5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Function to update animation frame
def update(frame):
    ax.clear()
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Example static positions for demonstration
    positions = np.array([
        [0.1, 0.2], [0.2, 0.1], [0.3, 0.2], [0.4, 0.3],
        [0.5, 0.4], [0.6, 0.3], [0.7, 0.2], [0.8, 0.1],
        [0.9, 0.2], [1.0, 0.3], [1.1, 0.2], [1.2, 0.1],
        [1.3, 0.2], [1.4, 0.3], [1.5, 0.2]
    ])
    
    # Plot points as white dots
    ax.plot(positions[:, 0], positions[:, 1], 'bo', color='white')
    
    # Animate walking motion with slow movement
    for i in range(len(positions)):
        positions[i][0] -= 0.01
        positions[i][1] += np.sin(frame/10.0 + i/2.0) / 50.0
    
    return fig,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show plot
plt.show()
