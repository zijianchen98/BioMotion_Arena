
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SadWomanAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.axis('off')
        self.points, = self.ax.plot([], [], 'wo', markersize=8)

    def init(self):
        self.points.set_data([], [])
        return self.points,

    def update(self, frame):
        t = 0.1 * frame
        x = 8 * np.sin(t/2) * np.sin(t)
        y = -8 * np.cos(t) * np.cos(t/2)
        x += 4 * np.random.rand(15) - 2
        y += 4 * np.random.rand(15) - 2
        self.points.set_data(x, y)
        return self.points,

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=200, init_func=self.init, blit=True, interval=50)
        plt.show()

if __name__ == "__main__":
    sad_woman = SadWomanAnimation()
    sad_woman.animate()
