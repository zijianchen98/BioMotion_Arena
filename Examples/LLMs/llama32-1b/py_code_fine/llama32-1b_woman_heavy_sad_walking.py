
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 0, 0)

# Define the subject and action
SUBJECT = 'woman'
ACTION = 'walking'

# Define the parameters for the animation
FPS = 60
TIME_STEP = 0.01

# Define the point lights
point_lights = []
for i in range(15):
    angle = np.radians(30 + i * 15)
    x = WIDTH / 2 + np.cos(angle) * 200
    y = HEIGHT / 2 + np.sin(angle) * 200
    point_lights.append([x, y, 100])

# Define the camera
camera = {
    'pos': [WIDTH / 2, HEIGHT / 2],
    'lookat': [0, 0, 0],
    'up': [0, 1, 0],
    'near': 0.1,
    'far': 1000
}

# Define the figure and axis
fig, ax = plt.subplots()

# Define the initial points
points = np.zeros((100, 3))
points[0, :] = [WIDTH / 2, HEIGHT / 2, 0]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_aspect('equal')
    ax.set_title(f'{SUBJECT} is {ACTION}')

    # Update the points
    points[i, :] = [WIDTH / 2 + np.cos(np.radians(30 + i * 15)) * 200,
                    HEIGHT / 2 + np.sin(np.radians(30 + i * 15)) * 200,
                    0]

    # Draw the point lights
    for j, point in enumerate(points):
        ax.scatter(point[0], point[1], color=WHITE, s=50, alpha=0.5)

    # Draw the point lights
    for point in point_lights:
        ax.scatter(point[0], point[1], color=POINT_LIGHT_COLOR, s=50, alpha=0.5)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(points), interval=16 * FPS, blit=True, save_count=50)

# Show the animation
plt.show()
