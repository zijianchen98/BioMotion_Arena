
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights
num_lights = 15

# Define the time steps
time_steps = 100

# Define the positions of the lights in a walking cycle
def get_positions(t):
    positions = np.zeros((num_lights, 2))
    
    # Head
    positions[0] = [0, 1]
    
    # Shoulders
    positions[1] = [-0.5, 0.75]
    positions[2] = [0.5, 0.75]
    
    # Arms
    positions[3] = [-0.8, 0.6 + 0.1 * np.sin(t * 2 * np.pi)]
    positions[4] = [0.8, 0.6 + 0.1 * np.sin(t * 2 * np.pi + np.pi)]
    
    # Hips
    positions[5] = [-0.3, 0.25]
    positions[6] = [0.3, 0.25]
    
    # Legs
    positions[7] = [-0.5, -0.1 + 0.1 * np.sin(t * 2 * np.pi)]
    positions[8] = [-0.5, -0.5 + 0.1 * np.sin(t * 2 * np.pi)]
    positions[9] = [0.5, -0.1 + 0.1 * np.sin(t * 2 * np.pi + np.pi)]
    positions[10] = [0.5, -0.5 + 0.1 * np.sin(t * 2 * np.pi + np.pi)]
    
    # Feet
    positions[11] = [-0.5, -0.6 + 0.2 * np.sin(t * 2 * np.pi)]
    positions[12] = [-0.5, -1.0 + 0.2 * np.sin(t * 2 * np.pi)]
    positions[13] = [0.5, -0.6 + 0.2 * np.sin(t * 2 * np.pi + np.pi)]
    positions[14] = [0.5, -1.0 + 0.2 * np.sin(t * 2 * np.pi + np.pi)]
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes

# Create points
points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    positions = get_positions(i / time_steps)
    x = positions[:, 0]
    y = positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
anim = FuncAnimation(fig, animate, init_func=init,
                     frames=time_steps, interval=50, blit=True)

plt.show()
