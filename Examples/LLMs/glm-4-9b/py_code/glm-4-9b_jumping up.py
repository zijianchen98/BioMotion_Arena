
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_lights = 15
duration = 200  # Total animation frames
fps = 30  # Frames per second
black_background = np.array([0, 0, 0])
white_lights = np.array([1, 1, 1])
jump_height = 1.0
jump_time = 2 * np.pi  # Period of the jump in seconds
person_shape = [(0, 0), (0.1, -0.2), (0.2, -0.2), (0.2, -0.4), 
                (0.3, -0.4), (0.3, -0.6), (0.1, -0.6), (0.1, -0.8), 
                (-0.1, -0.8), (-0.2, -0.6), (-0.2, -0.4), (-0.3, -0.4), 
                (-0.3, -0.2), (-0.2, -0.2), (-0.1, -0.2)]

def get_jumping_position(t):
    """Return the (x, y) position of the person at time t."""
    if t < np.pi:
        y = jump_height * np.sin(t)
    else:
        y = jump_height * np.sin(t) - jump_height
    return y

def update(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-1.0, jump_height + 0.2)
    ax.set_facecolor(black_background)
    ax.axis('off')
    
    t = frame / fps
    y = get_jumping_position(t)
    
    # Draw the person
    person = person_shape.copy()
    person = [(px, py + y) for px, py in person]
    for x, y in person:
        ax.add_patch(Circle((x, y), 0.02, color='white'))
    
    # Draw the lights in a circle around the person
    light_radius = 0.1
    angles = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)
    radius = 0.2
    for angle in angles:
        light_x = radius * np.cos(angle)
        light_y = radius * np.sin(angle) + y
        ax.add_patch(Circle((light_x, light_y), 0.02, color=white_lights))
        
    return ax,

fig, ax = plt.subplots()
ax.set_aspect('equal')
ani = FuncAnimation(fig, update, frames=duration, interval=1000/fps, blit=True)
plt.show()
