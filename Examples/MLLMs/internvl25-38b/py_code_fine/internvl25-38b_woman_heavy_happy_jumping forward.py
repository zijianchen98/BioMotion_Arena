
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frame_rate = 30  # frames per second
duration = 4  # seconds

# Generate time array
t = np.linspace(0, duration, frame_rate * duration)

# Define trajectories for the points
def trajectory1(t):
    return 0.3 * np.sin(2 * np.pi * t) + 0.5

def trajectory2(t):
    return 0.5 * np.sin(2 * np.pi * t) + 0.5

def trajectory3(t):
    return 0.7 * np.sin(2 * np.pi * t) + 0.5

def trajectory4(t):
    return 0.1 * np.sin(2 * np.pi * t) + 0.5

def trajectory5(t):
    return 0.9 * np.sin(2 * np.pi * t) + 0.5

def trajectory6(t):
    return 0.3 * np.cos(2 * np.pi * t) + 0.5

def trajectory7(t):
    return 0.5 * np.cos(2 * np.pi * t) + 0.5

def trajectory8(t):
    return 0.7 * np.cos(2 * np.pi * t) + 0.5

def trajectory9(t):
    return 0.1 * np.cos(2 * np.pi * t) + 0.5

def trajectory10(t):
    return 0.9 * np.cos(2 * np.pi * t) + 0.5

trajectories = [
    trajectory1(t),
    trajectory2(t),
    trajectory3(t),
    trajectory4(t),
    trajectory5(t),
    trajectory6(t),
    trajectory7(t),
    trajectory8(t),
    trajectory9(t),
    trajectory10(t),
    t / duration,
    (0.5 * t / duration) + 0.25,
    (0.75 * t / duration) + 0.1,
    (0.25 * t / duration) + 0.4,
    (0.1 * t / duration) + 0.3
]

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

points = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(num_points)]

# Initialization function
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation function
def animate(i):
    for j, point in enumerate(points):
        point.set_data(j / (num_points - 1), trajectories[j][i])
    return points

# Create animation
ani = animation.FuncAnimation(
    fig, animate, frames=len(t), init_func=init, blit=True, repeat=False)

# Save or display animation
plt.show()
