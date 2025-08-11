
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class SadManWaving:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_facecolor('black')
        self.points = [plt.Circle((x, y), 0.2, color='white') for x, y in self.get_initial_positions()]
        for point in self.points:
            self.ax.add_patch(point)
        self.frames = 100

    def get_initial_positions(self):
        return [
            (5, 9), (4, 8), (6, 8), (4.5, 7), (5.5, 7),
            (5, 6), (4, 5), (6, 5), (4, 4), (6, 4),
            (5, 3), (4.5, 2), (5.5, 2), (5, 1), (5, 0)
        ]

    def update(self, frame):
        theta = np.linspace(0, np.pi * 2, len(self.points), endpoint=False)
        amplitude = 0.5
        height = 0.5
        for i, point in enumerate(self.points):
            if i < 4:
                if i == 0:
                    point.set_center((5 + amplitude * np.sin(frame * 0.1), 9))
                else:
                    point.set_center((5 + amplitude * np.sin(frame * 0.1 + theta[i-1]), 9 - i * height))
            else:
                point.set_center((point.get_center()[0], point.get_center()[1]))

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=self.frames, interval=50, blit=False)
        plt.show()

animation_instance = SadManWaving()
animation_instance.animate()
