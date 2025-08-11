
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointLight({self.x}, {self.y})"

def create_point_light(point_light):
    return PointLight(point_light.x, point_light.y)

def create_black_background():
    return np.ones((WIDTH, HEIGHT), dtype=np.uint8)

def create_white_point_lights(num_lights):
    return [create_point_light(np.random.uniform(0, WIDTH), np.random.uniform(0, HEIGHT)) for _ in range(num_lights)]

def animate_point_light(point_light, frame):
    x, y = point_light.x, point_light.y
    angle = np.random.uniform(0, 2 * np.pi)
    point_light.x = x + np.cos(angle) * 10
    point_light.y = y + np.sin(angle) * 10
    return PointLight(point_light.x, point_light.y)

def main():
    # Create a black background
    black_background = create_black_background()
    white_point_lights = create_white_point_lights(15)
    fig, ax = plt.subplots()
    ax.set_facecolor(BLACK)
    ax.imshow(black_background, cmap='gray')
    ax.set_axis_off()

    # Initialize point lights
    point_lights = [animate_point_light(white_point_lights[i], frame) for i, frame in enumerate(range(15))]

    def update(frame):
        ax.clear()
        ax.set_facecolor(BLACK)
        ax.imshow(black_background, cmap='gray')
        for point_light in point_lights:
            ax.add_patch(plt.Circle((point_light.x, point_light.y), 2, color=POINT_LIGHT_COLOR))
        ax.set_axis_off()
        return ax

    # Animate the point lights
    ani = animation.FuncAnimation(fig, update, frames=range(15), interval=20)

    plt.show()

if __name__ == "__main__":
    main()
