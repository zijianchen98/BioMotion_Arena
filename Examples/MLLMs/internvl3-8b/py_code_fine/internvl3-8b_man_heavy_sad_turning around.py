
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, ax):
        ax.plot(self.x, self.y, 'o', color='white', markersize=10)

class SadmanTurning:
    def __init__(self):
        self.point_lights = [PointLight(random.randint(0, 10), random.randint(0, 10)) for _ in range(15)]
    
    def update_positions(self):
        for light in self.point_lights:
            theta = random.uniform(0, 2 * 3.1415)
            light.x = 5 * (0.8 * (1 - 0.1 * random.random()) * random.random() + 0.5 * random.random()) * 0.01 * random.random() * 4 * math.cos(theta) + light.x
            light.y = 5 * (0.8 * (1 - 0.1 * random.random()) * random.random() + 0.5 * random.random()) * 0.01 * random.random() * 4 * math.sin(theta) + light.y
                
    def animate(self, frame, fig, ax):
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        self.update_positions()
        for light in self.point_lights:
            light.draw(ax)

fig, ax = plt.subplots()
sadman = SadmanTurning()

ani = animation.FuncAnimation(fig, sadman.animate, frames=200, fargs=(fig, ax), interval=100)

plt.show()
