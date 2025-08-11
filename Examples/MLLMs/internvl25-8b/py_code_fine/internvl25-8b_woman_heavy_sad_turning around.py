
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.ndimage import uniform_filter1d

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))
points[0], points[-1] = 15, 25
points[0:7], points[7:14], points[14:] = (
    15 - np.linspace(5, 0, num_points - 1),
    15 - np.linspace(-5, 0, num_points - 7),
    15 - np.linspace(0, 10, num_points - 14),
)

# Define the background
background = np.full((50, 50), 0)

# Animation function
def update(frame):
    positions = points.copy()
    positions[0] = 15 + 5 * np.sin(2 * np.pi / 60 * frame)
    positions[7] = 15 + 5 * (1 / 7) * np.sin(2 * np.pi / 60 * frame) - 5 * (6 / 7) * np.cos(2 * np.pi / 60 * frame)
    positions[14] = 15 + 5 * np.cos(2 * np.pi / 60 * frame)
    
    background.fill(0)
    background[:15] = 255
    
    smoothed_positions = uniform_filter1d(positions[:, 0], size=3) * 50
    background[smoothed_positions.astype(int)] = 255
    
    return background, points.flatten()

# Create the animation
animation = FuncAnimation(plt.gcf(), update, frames=range(60), blit=True, interval=50)

# Hide axes and show the animation
plt.axis('off')
plt.show()
