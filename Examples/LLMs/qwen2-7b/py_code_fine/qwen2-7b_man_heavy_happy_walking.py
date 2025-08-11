
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def draw_happy_man():
    x = [0, 1, 1, 0, -1, -1, -1]
    y = [0, 0, 1, 1, 1, 0, -1]
    plt.figure(figsize=(5, 4))
    plt.plot(x, y, 'o-', color='white', markersize=10)
    plt.axis('off')
    plt.axis('equal')
    plt.show()

class HappyManAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_axis_off()
        self.line, = self.ax.plot([], [], 'o-', lw=2, color='white')

    def update(self, i):
        theta = 2 * np.pi / 15 * i
        x = np.cos(theta)
        y = np.sin(theta)
        self.line.set_data([x], [y])
        return self.line,

    def animate(self):
        self.anim = animation.FuncAnimation(
            self.fig, self.update, frames=np.arange((, 15),
            interval=200, blit=True)
        plt.show()

if __name__ == "__main__":
    draw_happy_man()
    anim = HappyManAnimation()
    anim.animate()
