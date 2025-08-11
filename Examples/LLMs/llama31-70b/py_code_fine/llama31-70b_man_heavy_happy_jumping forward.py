
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
lights = np.array([
    [0, 0],  # Head
    [-0.2, 0.3], [-0.2, -0.3],  # Left arm
    [0.2, 0.3], [0.2, -0.3],  # Right arm
    [0, 0.5],  # Torso
    [-0.1, 0.7], [-0.1, 0.9],  # Left upper leg
    [0.1, 0.7], [0.1, 0.9],  # Right upper leg
    [-0.2, 1.1], [-0.2, 1.3],  # Left lower leg
    [0.2, 1.1], [0.2, 1.3],  # Right lower leg
    [-0.3, 0.1], [0.3, 0.1]  # Hands
])

# Define the motion parameters
fps = 30
duration = 2  # seconds
num_frames = int(fps * duration)

# Define the motion functions
def head(t):
    return np.array([0, 0.1 * np.sin(2 * np.pi * t)])

def arm(t, side):
    angle = 2 * np.pi * t
    return np.array([side * 0.2 * np.sin(angle), 0.3 * np.cos(angle)])

def leg(t, side):
    angle = 2 * np.pi * t
    return np.array([side * 0.1 * np.sin(angle), 0.4 * np.cos(angle)])

def torso(t):
    return np.array([0, 0.05 * np.sin(2 * np.pi * t)])

def hand(t, side):
    angle = 2 * np.pi * t
    return np.array([side * 0.3 * np.sin(angle), 0.1 * np.cos(angle)])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter(lights[:, 0], lights[:, 1], s=10, c='white')

# Animation function
def animate(t):
    global points
    points.remove()
    
    # Update the positions of the point-lights
    positions = np.array([
        head(t),
        arm(t, -1), arm(t + 0.5, -1),
        arm(t, 1), arm(t + 0.5, 1),
        torso(t),
        leg(t, -1), leg(t + 0.5, -1),
        leg(t, 1), leg(t + 0.5, 1),
        leg(t + 1, -1), leg(t + 1.5, -1),
        leg(t + 1, 1), leg(t + 1.5, 1),
        hand(t, -1), hand(t, 1)
    ])
    
    # Add the point-lights
    points = ax.scatter(positions[:, 0], positions[:, 1], s=10, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 // fps)

plt.show()
