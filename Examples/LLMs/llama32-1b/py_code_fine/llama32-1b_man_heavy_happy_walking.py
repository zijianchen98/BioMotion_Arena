
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Define subject and action
SUBJECT = 'happyman'
ACTION = 'walking'

# Define parameters
WALKING_SPEED = 2.0
STEP_SIZE = 100
MAX_STEPS = 100

# Create figure and axis
fig, ax = plt.subplots()

# Initialize axis
x = np.linspace(0, WIDTH, 100)
y = np.linspace(0, HEIGHT, 100)
X, Y = np.meshgrid(x, y)

# Define light positions
LIGHTS = []
for i in range(15):
    angle = i * np.pi / 8
    x = WIDTH / 2 + 200 * np.cos(angle)
    y = HEIGHT / 2 + 200 * np.sin(angle)
    LIGHTS.append((x, y))

# Define light colors
LIGHT_COLORS = []
for i in range(15):
    color = LIGHT_COLOR
    for j in range(15):
        color += np.array([1, 0, 0]) * (0.8 - j / 15)
    LIGHT_COLORS.append(color)

# Initialize plot
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Function to draw point light
def draw_point_light(x, y, color):
    ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=False, color=color))

# Function to update plot
def update(frame):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    
    # Draw lights
    for i, (x, y) in enumerate(LIGHTS):
        draw_point_light(x, y, LIGHT_COLORS[i])
    
    # Draw subject
    ax.scatter(WIDTH / 2, HEIGHT / 2, color=WHITE, s=100)
    
    # Draw steps
    for i in range(MAX_STEPS):
        x = WIDTH / 2 + 200 * np.cos(i * np.pi / MAX_STEPS)
        y = HEIGHT / 2 + 200 * np.sin(i * np.pi / MAX_STEPS)
        draw_point_light(x, y, LIGHT_COLOR[i % 15])
    
    # Update plot
    plt.draw()

# Create animation
ani = animation.FuncAnimation(fig, update, frames=MAX_STEPS, interval=10)

plt.show()
