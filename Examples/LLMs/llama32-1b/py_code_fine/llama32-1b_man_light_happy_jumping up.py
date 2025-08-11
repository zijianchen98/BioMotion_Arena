
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
FPS = 60

# Define point light source parameters
POINT_LIGHT_RADIUS = 10
POINT_LIGHT_COLOR = WHITE_COLOR
POINT_LIGHT_SPOT_SIZE = 100

# Define subject parameters
SUBJECT_COLOR = WHITE_COLOR
SUBJECT_SIZE = 50

# Define action parameters
ACTION_SPEED = 5
ACTION_SPEED_MAX = 10

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += ACTION_SPEED / FPS
        self.x = WIDTH / 2 + np.cos(self.angle) * POINT_LIGHT_RADIUS
        self.y = HEIGHT / 2 + np.sin(self.angle) * POINT_LIGHT_RADIUS

def create_subject():
    subject = PointLight(WIDTH / 2, HEIGHT / 2)
    return subject

def create_action():
    action = PointLight(WIDTH / 2 + 100, HEIGHT / 2)
    return action

def create_background():
    background = np.zeros((HEIGHT, WIDTH))
    return background

def draw_subject(subject, background):
    plt.figure(figsize=(5, 5))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.scatter(subject.x, subject.y, color=SUBJECT_COLOR, s=SUBJECT_SIZE)
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    plt.show()

def draw_action(action, background):
    plt.figure(figsize=(5, 5))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.scatter(action.x, action.y, color=WHITE_COLOR, s=POINT_LIGHT_SPOT_SIZE)
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    plt.show()

def main():
    subject = create_subject()
    action = create_action()
    background = create_background()

    fig, ax = plt.subplots()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    def animate(i):
        subject.update()
        action.update()
        ax.clear()
        ax.set_xlim(0, WIDTH)
        ax.set_ylim(0, HEIGHT)
        ax.scatter(subject.x, subject.y, color=SUBJECT_COLOR, s=SUBJECT_SIZE)
        ax.scatter(action.x, action.y, color=WHITE_COLOR, s=POINT_LIGHT_SPOT_SIZE)
        plt.draw()
        plt.pause(0.01)

    ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=20, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
