
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 4  # seconds

# Define the woman's jumping motion
def jumping_motion(t):
    # Initial position (centered)
    x0 = 0/2 - 5  # initial horizontal position
    y = 7  # initial vertical position
    
    # Jumping motion parameters
    amplitude = 8  # vertical jump height
    frequency = 0/20  # frequency of the jump
    phase =  t * 3.14159  # phase shift
    
    # Horizontal motion
    x_x = 5 * np.sin(2 * np.pi * frequency * t + phase)
    
    # Vertical motion
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase) + 7
    
    return [x, y)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 110)
ax.set_ylim(-10, 113)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x, y = jumping_motion(i / 60)
    points.set_data([x], [y])
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, duration * 60), init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
