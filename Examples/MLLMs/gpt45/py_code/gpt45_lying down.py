
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 8)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.axis('off')

# Create 15 points
points, = ax.plot([], [], 'wo', markersize=8)

# Define jumping forward coordinates for the man's joints with 15 points
def get_frame(t):
    body = np.array([
        # Head
        (t, 4 + 0.3*np.sin(np.pi*t)),
        # Shoulders
        (t-0.5, 3.5 + 0.3*np.sin(np.pi*t)), 
        (t+0.5, 3.5 + 0.3*np.sin(np.pi*t)),
        # Spine
        (t, 3.5), 
        (t, 3), 
        # Hips
        (t-0.4, 2.8), 
        (t+0.4, 2.8),
        # Knees
        (t-0.5, 1.7 + 0.2*np.abs(np.sin(np.pi*t))),
        (t+0.5, 1.7 + 0.2*np.abs(np.sin(np.pi*t + np.pi))),
        # Ankles
        (t-0.6, 0.6 + 0.3*np.abs(np.sin(np.pi*t))),
        (t+0.6, 0.6 + 0.3*np.abs(np.sin(np.pi*t + np.pi))),
        # Feet
        (t-0.8, 0.3*np.abs(np.sin(np.pi*t))),
        (t+0.8, 0.3*np.abs(np.sin(np.pi*t + np.pi))),
        # Elbows
        (t-0.8, 2.7 + 0.5*np.sin(np.pi*t)),
        (t+0.8, 2.7 + 0.5*np.sin(np.pi*t + np.pi)),
    ])
    
    return body

# Initialization
def init():
    points.set_data([], [])
    return points,

# Animation update
def animate(frame):
    t = frame / 30
    coords = get_frame(t % 4)
    points.set_data(coords[:,0], coords[:,1])
    return points,

# Create animation
anim = FuncAnimation(fig, animate, init_func=init, frames=120, interval=33, blit=True)

# Set background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Display the animation
plt.show()
