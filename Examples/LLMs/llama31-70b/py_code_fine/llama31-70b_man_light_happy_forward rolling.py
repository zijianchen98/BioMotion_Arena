
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for a person rolling forward
# These are based on the work by Johansson (1973) and are approximate
point_lights = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.3],  # Left shoulder
    [0.6, 0.3],  # Right shoulder
    [0.4, 0.2],  # Left elbow
    [0.6, 0.2],  # Right elbow
    [0.4, 0.1],  # Left wrist
    [0.6, 0.1],  # Right wrist
    [0.5, 0.4],  # Hip
    [0.45, 0.35],  # Left knee
    [0.55, 0.35],  # Right knee
    [0.45, 0.25],  # Left ankle
    [0.55, 0.25],  # Right ankle
    [0.4, 0.15],  # Left toe
    [0.6, 0.15],  # Right toe
    [0.5, 0.05]  # Body center
])

# Define the movement parameters
num_frames = 100
dt = 0.1
time = np.arange(0, num_frames * dt, dt)

# Define the movement functions
def head(t):
    return np.array([0.5, 0.5 + 0.1 * np.sin(t)])

def shoulders(t):
    return np.array([[0.4, 0.3 + 0.05 * np.sin(t)],
                     [0.6, 0.3 + 0.05 * np.sin(t)]])

def elbows(t):
    return np.array([[0.4, 0.2 + 0.1 * np.sin(t)],
                     [0.6, 0.2 + 0.1 * np.sin(t)]])

def wrists(t):
    return np.array([[0.4, 0.1 + 0.15 * np.sin(t)],
                     [0.6, 0.1 + 0.15 * np.sin(t)]])

def hip(t):
    return np.array([0.5, 0.4 + 0.05 * np.sin(t)])

def knees(t):
    return np.array([[0.45, 0.35 + 0.1 * np.sin(t)],
                     [0.55, 0.35 + 0.1 * np.sin(t)]])

def ankles(t):
    return np.array([[0.45, 0.25 + 0.15 * np.sin(t)],
                     [0.55, 0.25 + 0.15 * np.sin(t)]])

def toes(t):
    return np.array([[0.4, 0.15 + 0.2 * np.sin(t)],
                     [0.6, 0.15 + 0.2 * np.sin(t)]])

def body_center(t):
    return np.array([0.5, 0.05 + 0.05 * np.sin(t)])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the initial point-light locations
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=10, c='white')

# Animation function
def animate(i):
    t = time[i]
    points.set_offsets(np.array([
        head(t),
        shoulders(t)[0],
        shoulders(t)[1],
        elbows(t)[0],
        elbows(t)[1],
        wrists(t)[0],
        wrists(t)[1],
        hip(t),
        knees(t)[0],
        knees(t)[1],
        ankles(t)[0],
        ankles(t)[1],
        toes(t)[0],
        toes(t)[1],
        body_center(t)
    ]))

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

plt.show()
