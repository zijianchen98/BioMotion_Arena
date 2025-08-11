
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RUNNING_SPEED = 0.5

# Function to generate a random point light
def generate_point_light(x, y, intensity):
    return (x, y, intensity)

# Function to calculate the distance from the point light to a point
def calculate_distance(point_x, point_y, light_x, light_y, light_intensity):
    return ((point_x - light_x) ** 2 + (point_y - light_y) ** 2) ** 0.5

# Function to generate a random point on the circumference of a circle
def generate_random_point():
    angle = random.uniform(0, 2 * np.pi)
    radius = np.random.uniform(0.1, 0.5)
    return (radius * np.cos(angle), radius * np.sin(angle))

# Function to update the plot
def update(frame):
    global running

    # Clear the previous frame
    ax.clear()

    # Set the axis limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    # Set the aspect ratio to be equal
    ax.set_aspect('equal')

    # Initialize the point lights
    point_lights = []

    # Generate 15 point lights
    for i in range(15):
        light_x = WIDTH / 2 + i * (WIDTH / 15)
        light_y = HEIGHT / 2
        light_intensity = 1 - (i / 15)
        point_light = generate_point_light(light_x, light_y, light_intensity)
        point_lights.append(point_light)

    # Generate a happyman with a running action
    happyman_x = WIDTH / 2
    happyman_y = HEIGHT / 2
    running_x = happyman_x + 0.2 * RUNNING_SPEED
    running_y = happyman_y - 0.2 * RUNNING_SPEED
    happyman_points = []
    while running_x < WIDTH and running_y < HEIGHT:
        happyman_point = generate_random_point()
        happyman_points.append(happyman_point)
        running_x += 0.1
        running_y -= 0.1
    happyman_points.append(generate_random_point())

    # Plot the point lights
    for point_light in point_lights:
        ax.add_patch(plt.Circle(point_light, 0.05, edgecolor='black', facecolor='white'))

    # Plot the happyman
    ax.scatter(*zip(happyman_points[::2], happyman_points[1::2]), c='blue', s=10)

    # Plot the running action
    running_points = zip(happyman_points[::2], happyman_points[1::2])
    for point in running_points:
        ax.plot([point[0][0], point[1][0]], [point[0][1], point[1][1]], color='red', linewidth=1)

    # Set the limits and show the plot
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_axis_off()
    plt.show()

# Initialize the plot
fig, ax = plt.subplots()

# Create a point light at the origin
ax.add_patch(plt.Circle((0, 0), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2, HEIGHT)
ax.add_patch(plt.Circle((WIDTH/2, HEIGHT), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2, HEIGHT + 0.1)
ax.add_patch(plt.Circle((WIDTH/2, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 - 0.1, HEIGHT + 0.1)
ax.add_patch(plt.Circle((WIDTH/2 - 0.1, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 + 0.1, HEIGHT + 0.1)
ax.add_patch(plt.Circle((WIDTH/2 + 0.1, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 + 0.1, HEIGHT)
ax.add_patch(plt.Circle((WIDTH/2 + 0.1, HEIGHT), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 - 0.1, HEIGHT)
ax.add_patch(plt.Circle((WIDTH/2 - 0.1, HEIGHT), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2)
ax.add_patch(plt.Circle((WIDTH/2, HEIGHT), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2)
ax.add_patch(plt.Circle((WIDTH/2, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 + 0.1, HEIGHT + 0.1)
ax.add_patch(plt.Circle((WIDTH/2 + 0.1, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 + 0.1, HEIGHT)
ax.add_patch(plt.Circle((WIDTH/2 + 0.1, HEIGHT), 0.1, edgecolor='black', facecolor='white'))

# Create a point light at (WIDTH/2 + 0.1, HEIGHT)
ax.add_patch(plt.Circle((WIDTH/2 + 0.1, HEIGHT + 0.1), 0.1, edgecolor='black', facecolor='white'))

# Set the limits and show the plot
update(0)
