
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HAND_LENGTH = 200

# Define a function to generate a point light source
def point_light(x, y, intensity):
    return intensity * np.array([x, y, 1])

# Define a function to calculate the direction vector of the light source
def direction_vector(x, y):
    return np.array([x - WIDTH // 2, y - HEIGHT // 2, 0])

# Define a function to generate the hand motion
def hand_motion(x, y, angle):
    hand_length = HAND_LENGTH
    hand_x = x + np.sin(angle) * hand_length
    hand_y = y - np.cos(angle) * hand_length
    return point_light(hand_x, hand_y, 1)

# Define the animation function
def animate(i):
    global x, y, angle
    # Set the initial position and angle of the light source
    x, y = WIDTH // 2, HEIGHT // 2
    angle = np.radians(np.random.uniform(0, 360))

    # Draw the background
    plt.imshow(BLACK, cmap='gray')
    plt.axis('off')

    # Draw the point lights
    for _ in range(15):
        plt.scatter(x, y, s=100, c='white', alpha=0.5)
        plt.arrow(x, y, np.cos(angle) * 10, np.sin(angle) * 10, head_width=5, head_length=10, color='white')
        x += np.cos(angle) * 0.5
        y -= np.sin(angle) * 0.5

    # Draw the hand motion
    plt.scatter(x, y, s=100, c='white', alpha=0.5)
    plt.arrow(x, y, np.cos(angle) * 10, np.sin(angle) * 10, head_width=5, head_length=10, color='white')
    x += np.cos(angle) * 0.5
    y -= np.sin(angle) * 0.5

    # Update the plot
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    plt.show()

# Generate the initial position and angle of the light source
x, y = WIDTH // 2, HEIGHT // 2
angle = np.radians(np.random.uniform(0, 360))

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=10)

# Display the animation
plt.show()
