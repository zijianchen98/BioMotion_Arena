
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAD_WOMAN_SIZE = 100

# Initialize figure and axis
fig, ax = plt.subplots()

# Define point light source
source = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Define sad woman's movement
def sad_woman_move(x, y):
    # Move sad woman's head and torso
    head = np.array([
        x + 10*np.sin(np.linspace(0, 2*np.pi, 100)),
        y + 5*np.cos(np.linspace(0, 2*np.pi, 100))
    ])
    torso = np.array([
        x + 5*np.sin(np.linspace(0, 2*np.pi, 100)),
        y + 10*np.cos(np.linspace(0, 2*np.pi, 100))
    ])

    # Move sad woman's arms
    arm1 = np.array([
        x + 15*np.sin(np.linspace(0, 2*np.pi, 100)),
        y + 5*np.cos(np.linspace(0, 2*np.pi, 100))
    ])
    arm2 = np.array([
        x + 15*np.sin(np.linspace(0, 2*np.pi, 100)),
        y + 5*np.cos(np.linspace(0, 2*np.pi, 100))
    ])

    # Return sad woman's position
    return head, torso, arm1, arm2

# Initialize plot
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')
ax.set_axis_off()

# Initialize point lights
points = []
for i in range(15):
    point = np.array([
        WIDTH / 2 + i * (WIDTH / 15),
        HEIGHT / 2 + i * (HEIGHT / 15)
    ])
    points.append(point)

# Animation function
def animate(i):
    global points

    # Clear previous points
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Draw sad woman
    ax.scatter(*sad_woman_move(0, 0).astype(int), s=SAD_WOMAN_SIZE, c='r')

    # Draw white point lights
    for point in points:
        ax.scatter(*point, s=1, c='w')

    # Draw sad woman's arms
    arm1 = sad_woman_move(point[0], point[1])
    arm2 = sad_woman_move(point[0], point[1] + 10)
    ax.scatter(*arm1, s=5, c='w')
    ax.scatter(*arm2, s=5, c='w')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
