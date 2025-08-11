
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PointLightAnimator:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.axis('off')
        self.point_lights, = self.ax.plot([], [], 'wo', markersize=4)
        self.time = 0

    def init_animation(self):
        self.point_lights.set_data([], [])
        return self.point_lights,

    def update_animation(self, frame):
        self.time = frame / 50.0
        t = self.time
        # Parameters for the sadwoman bowing motion
        x_offsets = np.cos(2 * np.pi * np.random.rand(15) + t) * 5
        y_offsets = np.sin(2 * np.pi * np.random.rand(15) + t) * 3 - 8 + 10 * np.exp(-t)

        # Simulating the bowing motion
        x = x_offsets
        y = y_offsets - 5 * np.sin(0.5 * np.pi * t)  # Bowing downwards

        self.point_lights.set_data(x, y)
        return self.point_lights,

    def animate(self):
        anim = FuncAnimation(self.fig, self.update_animation, frames=200,
                              init_func=self.init_animation, blit=True, interval=50)
        plt.show()

# Create and run the animator
animator = PointLightAnimator()
animator.animate()
