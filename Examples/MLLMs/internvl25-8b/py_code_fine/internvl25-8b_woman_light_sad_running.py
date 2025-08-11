
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the visual style
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Number of points
num_points = 15

# Initial positions
points = np.array([
    [-0.2, 0.9], [-0.1, 0.8], [0.0, 0.7],
    [0.05, 0.65], [0.1, 0.6], [0.15, 0.55],
    [0.2, 0.5], [0.2, 0.45], [0.2, 0.4],
    [0.2, 0.35], [0.22, 0.3], [0.25, 0.25],
    [0.27, 0.2], [0.3, 0.15], [0.3, 0.1]
])

# Angle array
angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)

# Function to animate frames
def animate(frame):
    ax.clear()
    
    # Update positions
    for i, angle in enumerate(angles):
        x = np.cos(angle + frame) * points[i, 0]
        y = np.sin(angle + frame) * points[i, 1]
        ax.plot(x, y, 'o', color='white', markersize=5, clip_on=False)
        
    ax.set_rmax(1)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 100), interval=50)

plt.show()
