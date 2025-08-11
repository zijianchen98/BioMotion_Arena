
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = [
    # Head
    {'x': 0, 'y': 10, 'dx': 0, 'dy': 0},
    # Shoulder
    {'x': -2, 'y': 8, 'dx': 0, 'dy': 0},
    {'x': 2, 'y': 8, 'dx': 0, 'dy': 0},
    # Elbow
    {'x': -4, 'y': 6, 'dx': 0, 'dy': 0},
    {'x': 4, 'y': 6, 'dx': 0, 'dy': 0},
    # Wrist
    {'x': -6, 'y': 4, 'dx': 1, 'dy': 0},
    {'x': 6, 'y': 4, 'dx': -1, 'dy': 0},
    # Hand
    {'x': -8, 'y': 2, 'dx': 1, 'dy': 0},
    {'x': 8, 'y': 2, 'dx': -1, 'dy': 0},
    # Hip
    {'x': -2, 'y': 0, 'dx': 0, 'dy': 0},
    {'x': 2, 'y': 0, 'dx': 0, 'dy': 0},
    # Knee
    {'x': -2, 'y': -2, 'dx': 0, 'dy': 0},
    {'x': 2, 'y': -2, 'dx': 0, 'dy': 0},
    # Ankle
    {'x': -2, 'y': -4, 'dx': 0, 'dy': 0},
    {'x': 2, 'y': -4, 'dx': 0, 'dy': 0},
]

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 15)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot
scatter = ax.scatter([point['x'] for point in point_lights], [point['y'] for point in point_lights], c='white', s=10)

# Animation function
def animate(i):
    for point in point_lights:
        point['x'] += point['dx']
        point['y'] += point['dy']
        
        # Waving hand motion
        if point == point_lights[6]:
            point['x'] = -6 + np.sin(i/10) * 2
        elif point == point_lights[7]:
            point['x'] = 6 - np.sin(i/10) * 2
        elif point == point_lights[8]:
            point['x'] = -8 + np.sin(i/10) * 4
        elif point == point_lights[9]:
            point['x'] = 8 - np.sin(i/10) * 4
    
    # Update the plot
    scatter.set_offsets([[point['x'], point['y']] for point in point_lights])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True, interval=50)

plt.show()
