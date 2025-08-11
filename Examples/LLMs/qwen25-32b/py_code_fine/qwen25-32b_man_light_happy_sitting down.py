
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the lights for sitting down motion
def get_positions(t):
    # Simplified model for sitting down motion
    # t is time in seconds
    amplitude = 0.5
    frequency = 1
    phase = np.pi / 4
    
    positions = np.zeros((15, 2))
    
    # Head
    positions[0] = [0, 1]
    
    # Shoulders
    positions[1] = [-0.2, 0.8]
    positions[2] = [0.2, 0.8]
    
    # Elbows
    positions[3] = [-0.4, 0.6]
    positions[4] = [0.4, 0.6]
    
    # Hands
    positions[5] = [-0.6, 0.4]
    positions[6] = [0.6, 0.4]
    
    # Hips
    positions[7] = [-0.2, 0.2]
    positions[8] = [0.2, 0.2]
    
    # Knees
    positions[9] = [-0.4, 0]
    positions[10] = [0.4, 0]
    
    # Feet
    positions[11] = [-0.6, -0.2]
    positions[12] = [0.6, -0.2]
    
    # Additional points to enhance realism
    positions[13] = [-0.3, 0.5]
    positions[14] = [0.3, 0.5]
    
    # Apply sinusoidal motion to simulate sitting down
    positions[:, 1] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    
    return positions

# Setup the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes

dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(t):
    x, y = get_positions(t).T
    dots.set_data(x, y)
    return dots,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2, 120), 
                    init_func=init, blit=True, interval=40)

plt.show()
