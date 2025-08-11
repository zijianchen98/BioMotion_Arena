
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define parameters
FRICTION = 0.995
GRAVITY = 0.001
FPS = 60

# Define the subject's parameters
SUBJECT_RADIUS = 50
SUBJECT_SPEED = 0.5
SUBJECT_TURN_SPEED = 0.05
SUBJECT_TURN_RADIUS = 20

# Define the action parameters
ACTION_RADIUS = 30
ACTION_SPEED = 0.1
ACTION_TURN_SPEED = 0.01

# Create the figure and axis
fig, ax = plt.subplots()

# Define the point lights
lights = []
for i in range(15):
    angle = i * np.pi / 9
    light_position = (WIDTH // 2 + np.cos(angle) * SUBJECT_RADIUS, HEIGHT // 2 + np.sin(angle) * SUBJECT_RADIUS)
    light_color = WHITE
    light_size = 1
    light = plt.Line2D([0, WIDTH], [0, HEIGHT], color=light_color, linestyle='-', linewidth=light_size, label=f'Light {i+1}')
    ax.add_artist(light)
    lights.append(light)

# Define the figure size
fig.set_size_inches(8, 8)

# Define the axis limits
ax.set_xlim(-WIDTH // 2, WIDTH // 2)
ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)

# Define the initial positions of the subject
subject_x, subject_y = WIDTH // 2, HEIGHT // 2

# Define the initial direction of the subject
subject_angle = 0

# Define the initial velocity of the subject
subject_velocity_x, subject_velocity_y = 0, 0

# Define the animation function
def animate(i):
    global subject_x, subject_y, subject_angle, subject_velocity_x, subject_velocity_y

    # Update the subject's position
    subject_x += subject_velocity_x
    subject_y += subject_velocity_y

    # Apply gravity
    subject_velocity_y += GRAVITY

    # Update the subject's direction
    subject_angle += SUBJECT_TURN_SPEED * subject_velocity_x

    # Limit the subject's direction
    subject_angle = np.clip(subject_angle, -SUBJECT_TURN_RADIUS, SUBJECT_TURN_RADIUS)

    # Update the subject's velocity
    subject_velocity_x = np.sin(subject_angle) * SUBJECT_TURN_SPEED
    subject_velocity_y = -np.cos(subject_angle) * SUBJECT_TURN_SPEED

    # Update the point lights
    for light in lights:
        light.set_x(0)
        light.set_y(0)

    # Update the axis limits
    ax.set_xlim(-WIDTH // 2, WIDTH // 2)
    ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)

    # Update the point lights
    for light in lights:
        light.set_x(subject_x + SUBJECT_RADIUS * np.cos(subject_angle))
        light.set_y(subject_y + SUBJECT_RADIUS * np.sin(subject_angle))

    # Update the figure size
    fig.set_size_inches(8, 8)

    # Draw the axis
    ax.axis('equal')

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=FPS, interval=50, blit=True)

# Show the animation
plt.show()
