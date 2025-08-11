
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure with a black background
fig, ax = plt.subplots(figsize=(6, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Define the initial positions of the points
points = np.array([
    [0.4, 0.8], [0.5, 0.8], [0.6, 0.8],
    [0.35, 0.7], [0.45, 0.7], [0.55, 0.7], [0.65, 0.7],
    [0.3, 0.6], [0.4, 0.6], [0.5, 0.6], [0.6, 0.6], [0.7, 0.6],
    [0.35, 0.5], [0.65, 0.5],
    [0.45, 0.4], [0.55, 0.4]
])

# Create scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

def update(frame):
    # Define a sine wave movement for the waving hand effect
    phase = frame / 10
    wave = 0.05 * np.sin(points[:, 0] * 10 - phase)
    
    # Update positions
    points[:, 1] += wave
    scat.set_offsets(points)
    
    # Reset positions to avoid drift
    points[:, 1] = np.clip(points[:, 1], 0.4, 0.8)
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
