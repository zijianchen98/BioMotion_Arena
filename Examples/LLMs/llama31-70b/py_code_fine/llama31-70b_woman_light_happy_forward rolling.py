
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
lights = np.array([
    [0, 0],  # head
    [-0.2, 0.2], [0.2, 0.2],  # shoulders
    [-0.3, 0.4], [0.3, 0.4],  # elbows
    [-0.4, 0.6], [0.4, 0.6],  # hands
    [0, -0.2],  # hips
    [-0.2, -0.4], [0.2, -0.4],  # knees
    [-0.3, -0.6], [0.3, -0.6],  # ankles
    [-0.4, -0.8], [0.4, -0.8],  # toes
])

# Define the motion parameters
num_frames = 100
dt = 0.1

# Define the motion functions
def head(t):
    return np.array([0, np.sin(t)])

def shoulders(t):
    return np.array([[-0.2, 0.2 + np.sin(t)], [0.2, 0.2 + np.sin(t)]])

def elbows(t):
    return np.array([[-0.3, 0.4 + np.sin(t) * 0.5], [0.3, 0.4 + np.sin(t) * 0.5]])

def hands(t):
    return np.array([[-0.4, 0.6 + np.sin(t) * 0.2], [0.4, 0.6 + np.sin(t) * 0.2]])

def hips(t):
    return np.array([0, -0.2 + np.sin(t) * 0.1])

def knees(t):
    return np.array([[-0.2, -0.4 + np.sin(t) * 0.2], [0.2, -0.4 + np.sin(t) * 0.2]])

def ankles(t):
    return np.array([[-0.3, -0.6 + np.sin(t) * 0.3], [0.3, -0.6 + np.sin(t) * 0.3]])

def toes(t):
    return np.array([[-0.4, -0.8 + np.sin(t) * 0.1], [0.4, -0.8 + np.sin(t) * 0.1]])

# Define the animation function
def animate(i):
    t = i * dt
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Plot the point-lights
    ax.plot(*head(t), 'o', markersize=5, color='white')
    ax.plot(*shoulders(t).T, 'o', markersize=5, color='white')
    ax.plot(*elbows(t).T, 'o', markersize=5, color='white')
    ax.plot(*hands(t).T, 'o', markersize=5, color='white')
    ax.plot(*hips(t), 'o', markersize=5, color='white')
    ax.plot(*knees(t).T, 'o', markersize=5, color='white')
    ax.plot(*ankles(t).T, 'o', markersize=5, color='white')
    ax.plot(*toes(t).T, 'o', markersize=5, color='white')

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

plt.show()
