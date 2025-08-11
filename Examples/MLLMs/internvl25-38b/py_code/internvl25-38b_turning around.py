
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
n_points = 15

# Time parameter
t = np.linspace(0, 2 * np.pi, 100)

# Coordinates for the points representing human figure while turning
x_coords = [
    np.cos(t),                   # Center
    np.cos(t) + 0.5 * np.sin(t),  # Right shoulder
    np.cos(t) - 0.5 * np.sin(t),  # Left shoulder
    np.cos(t) + 0.7 * np.cos(t),   # Right hip
    np.cos(t) - 0.7 * np.cos(t),   # Left hip
    np.cos(t) + 0.3 * np.sin(t),  # Right elbow
    np.cos(t) - 0.3 * np.sin(t),  # Left elbow
    np.cos(t) + 0.5 * np.cos(t),   # Right knee
    np.cos(t) - 0.5 * np.cos(t),   # Left knee
    np.cos(t) + 0.3 * np.sin(t) + 0.4 * np.cos(t),  # Right wrist
    np.cos(t) - 0.3 * np.sin(t) - 0.4 * np.cos(t),  # Left wrist
    np.cos(t) + 0.5 * np.sin(t) + 0.4 * np.sin(t),  # Right ankle
    np.cos(t) - 0.5 * np.sin(t) - 0.4 * np.sin(t),  # Left ankle
    np.cos(t) + 0.2 * np.sin(t) + 0.2 * np.cos(t),  # Head
    np.cos(t)                         # Center (repeated for smoothness)
]

y_coords = [
    np.sin(t),                   
    np.sin(t) + 0.5 * np.cos(t),   
    np.sin(t) - 0.5 * np.cos(t),   
    np.sin(t) - 0.7 * np.sin(t),   
    np.sin(t) + 0.7 * np.sin(t),   
    np.sin(t) - 0.5 * np.sin(t),   
    np.sin(t) + 0.5 * np.sin(t),   
    np.sin(t) - 0.5 * np.sin(t),   
    np.sin(t) + 0.5 * np.sin(t),   
    np.sin(t) - 0.5 * np.sin(t) - 0.4 * np.sin(t),  
    np.sin(t) + 0.5 * np.sin(t) + 0.4 * np.sin(t),  
    np.sin(t) - 0.7 * np.sin(t) + 0.4 * np.cos(t),  
    np.sin(t) + 0.7 * np.sin(t) - 0.4 * np.cos(t),  
    np.sin(t) + 0.2 * np.cos(t),  
    np.sin(t)                       
]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

sc = ax.scatter([], [], s=50, c='white')

def init():
    sc.set_offsets(np.c_[[], []])
    return sc,

def update(num):
    x = np.array([x[num] for x in x_coords])
    y = np.array([y[num] for y in y_coords])
    sc.set_offsets(np.c_[x, y])
    return sc,

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, repeat=True)

plt.show()
