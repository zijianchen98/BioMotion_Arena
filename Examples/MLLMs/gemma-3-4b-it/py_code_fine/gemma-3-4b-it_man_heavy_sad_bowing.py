
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_sadman_bowing():
    """
    Generates a point-light animation of a sadman bowing with heavy weight.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        # Generate random positions within a reasonable range
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-0.8, 0.8)
        z = np.random.uniform(-0.2, 0.2) 

        points.append([x, y, z])

    light_sources = []
    for i in range(15):
        light_sources.append([x, y, z])

    light = LightSource(ax, color='white')
    light_sources.append(light)
    
    ani = animation.FuncAnimation(fig, update, fargs=(light_sources,),
                                  interval=20, blit=True, repeat=True)

    plt.show()


class LightSource:
    def __init__(self, ax, color='white', radius=0.05):
        self.ax = ax
        self.color = color
        self.radius = radius
        self.x = 0
        self.y = 0
        self.z = 0

    def draw(self):
        self.ax.scatter(self.x, self.y, s=self.radius*100, color=self.color)

def update(light_sources, i):
    for light in light_sources:
        # Simulate movement - this is a very basic example
        light.x = np.random.uniform(-0.05, 0.05)
        light.y = np.random.uniform(-0.05, 0.05)
        light.z = np.random.uniform(-0.02, 0.02)
        
        light.draw()
        
if __name__ == '__main__':
    animate_sadman_bowing()
