
import numpy as np
import matplotlib.pyplot as plt

# Set figure size for better animation resolution
plt.rcParams["figure.figsize"] = (10, 10)

class PointLightStimulus:
    def __init__(self, num_points=15):
        self.num_points = num_points
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.axis('off')
        self.points = self.initialize_points()
        self.animation = None

    def initialize_points(self):
        points = []
        x = np.linspace(50, 50, self.num_points)
        y = np.linspace(50, 50, self.num_points)

        for xi, yi in zip(x, y):
            points.append(self.ax.scatter(xi, yi, s=300, color='white'))

        return points

    def create_animation(self):
        def roll_animation(i):
            self.ax.clear()
            self.ax.set_xlim(0, 100)
            self.ax.set_ylim(0, 100)
            self.ax.axis('off')

            for point in self.points:
                xpos = self.generate_forward_rolling_position(i, point)
                point.set_offsets((xpos, 0))

            self.fig.canvas.draw_idle()

        self.animation = matplotlib.animation.FuncAnimation(self.fig, roll_animation, frames=100, interval=50, repeat=False)
    
    def generate_forward_rolling_position(self, i, point):
        angle = np.deg2rad((i / 50) * 360)
        xpos = 50 + 50 * np.cos(angle)
        ypos = 50 + 50 * np.sin(angle)
        return xpos, ypos

    def show_animation(self):
        self.create_animation()
        plt.show()

# Run the animation
stimulus = PointLightStimulus()
stimulus.show_animation()
