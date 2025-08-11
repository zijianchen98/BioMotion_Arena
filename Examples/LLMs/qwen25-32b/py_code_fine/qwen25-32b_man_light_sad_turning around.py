
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
FRAMES = FPS * DURATION

# Generate time array
t = np.linspace(0, 2 * np.pi, FRAMES)

# Function to calculate positions of points
def get_positions(t):
    # Define positions for a turning around motion
    positions = np.zeros((NUM_POINTS, 2))
    
    # Head
    positions[0] = [np.cos(t), np.sin(t)]
    
    # Shoulders
    positions[1] = [np.cos(t) + 0.2, np.sin(t) - 0.1]
    positions[2] = [np.cos(t) - 0.2, np.sin(t) - 0.1]
    
    # Elbows
    positions[3] = [np.cos(t) + 0.4, np.sin(t) - 0.2]
    positions[4] = [np.cos(t) - 0.4, np.sin(t) - 0.2]
    
    # Hands
    positions[5] = [np.cos(t) + 0.6, np.sin(t) - 0.3]
    positions[6] = [np.cos(t) - 0.6, np.sin(t) - 0.3]
    
    # Hips
    positions[7] = [np.cos(t) + 0.1, np.sin(t) - 0.4]
    positions[8] = [np.cos(t) - 0.1, np.sin(t) - 0.4]
    
    # Knees
    positions[9] = [np.cos(t) + 0.2, np.sin(t) - 0.6]
    positions[10] = [np.cos(t) - 0.2, np.sin(t) - 0.6]
    
    # Feet
    positions[11] = [np.cos(t) + 0.3, np.sin(t) - 0.8]
    positions[12] = [np.cos(t) - 0.3, np.sin(t) - 0.8]
    
    # Additional points to enhance motion
    positions[13] = [np.cos(t) + 0.5, np.sin(t) - 0.5]
    positions[14] = [np.cos(t) - 0.5, np.sin(t) - 0.5]

    return positions.T

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'wo', markersize=5)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    x, y = get_positions(t[i])
    line.set_data(x, y)
    return line,

# Create animation
ani = FuncAnimation(fig, animate, frames=FRAMES, init_func=init, blit=True, interval=1000/FPS)

plt.show()
