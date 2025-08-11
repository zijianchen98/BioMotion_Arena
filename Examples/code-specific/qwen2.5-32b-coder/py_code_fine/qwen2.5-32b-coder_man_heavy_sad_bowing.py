
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
ax.set_aspect('equal')

# Initial positions of the points
points = np.zeros((NUM_POINTS, 2))

# Create scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

# Define the bowing motion
def bowing_motion(t):
    # Parameters for the bowing motion
    amplitude = 0.3
    frequency = 0.5
    phase_shift = np.linspace(0, 2*np.pi, NUM_POINTS)
    
    # Calculate positions
    x_positions = np.sin(phase_shift + t * frequency) * amplitude
    y_positions = -np.cos(phase_shift + t * frequency) * amplitude
    
    # Adjust for the head position
    y_positions -= 0.5
    
    # Adjust for the center of mass
    y_positions -= 0.2
    
    return x_positions, y_positions

# Update function for animation
def update(frame):
    t = frame / FPS
    x, y = bowing_motion(t)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

# Show plot
plt.show()
