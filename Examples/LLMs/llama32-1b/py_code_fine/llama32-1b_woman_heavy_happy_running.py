
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
RUNNING_COLOR = (0.8, 0.8, 0.8)

class PointLight:
    def __init__(self, x, y, z, intensity):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity

    def draw(self, ax):
        circle = plt.Circle((self.x, self.y), 0.05, color=WHITE_COLOR, alpha=0.5)
        ax.add_artist(circle)

def run_simulation():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define points for the subject's body
    body_points = [
        (WIDTH // 2, HEIGHT // 2 - 50),  # Head
        (WIDTH // 2, HEIGHT // 2 + 50),  # Eye 1
        (WIDTH // 2, HEIGHT // 2 - 50),  # Eye 2
        (WIDTH // 2 + 50, HEIGHT // 2),   # Left shoulder
        (WIDTH // 2 - 50, HEIGHT // 2),   # Right shoulder
        (WIDTH // 2, HEIGHT // 2 + 50),  # Left elbow
        (WIDTH // 2, HEIGHT // 2 - 50),  # Right elbow
        (WIDTH // 2 + 50, HEIGHT // 2),   # Left hip
        (WIDTH // 2 - 50, HEIGHT // 2),   # Right hip
        (WIDTH // 2, HEIGHT // 2 + 50),  # Left knee
        (WIDTH // 2, HEIGHT // 2 - 50),  # Right knee
        (WIDTH // 2 + 50, HEIGHT // 2),   # Left ankle
        (WIDTH // 2 - 50, HEIGHT // 2),   # Right ankle
    ]

    # Define points for the subject's limbs
    limb_points = [
        (WIDTH // 2, HEIGHT // 2 - 100),  # Left arm
        (WIDTH // 2 + 50, HEIGHT // 2 - 100),  # Right arm
        (WIDTH // 2, HEIGHT // 2 + 100),  # Left leg
        (WIDTH // 2 + 50, HEIGHT // 2 + 100),  # Right leg
    ]

    # Create a point light source at the center of the figure
    light = PointLight(WIDTH // 2, HEIGHT // 2, 0, 100)

    # Set the axis limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')

    # Function to update the plot
    def update(frame):
        ax.clear()
        ax.set_xlim(0, WIDTH)
        ax.set_ylim(0, HEIGHT)
        ax.set_aspect('equal')

        # Draw the subject's body
        for point in body_points:
            ax.add_artist(plt.Circle((point[0], point[1]), 0.05, color=WHITE_COLOR, alpha=0.5))

        # Draw the subject's limbs
        for point in limb_points:
            ax.add_artist(plt.Circle((point[0], point[1]), 0.05, color=WHITE_COLOR, alpha=0.5))

        # Draw the point light source
        light.draw(ax)

        # Draw the subject's weight
        weight = np.random.rand(3)
        weight = weight / np.linalg.norm(weight) * 100
        ax.plot([WIDTH // 2, WIDTH // 2], [HEIGHT // 2 - 50 + weight[0] * 100, HEIGHT // 2 + 50 - weight[1] * 100], color=BLACK_COLOR)

        # Update the plot
        plt.draw()
        plt.pause(0.01)

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

    # Show the animation
    plt.show()

run_simulation()
