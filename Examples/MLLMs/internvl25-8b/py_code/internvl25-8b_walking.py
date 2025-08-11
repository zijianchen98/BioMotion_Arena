
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class PointLightStimulus:
    def __init__(self, num_points=15):
        self.num_points = num_points
        self.positions = np.random.rand(num_points, 2)

    def update(self, frame):
        self.positions = self.positions + (np.cos(frame / 100) - np.sin(frame / 100), np.sin(frame / 100) + np.cos(frame / 100))
        return self.positions

def main():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    point_light_stimulus = PointLightStimulus()

    ani = animation.FuncAnimation(fig, point_light_stimulus.update, frames=range(100), blit=True, interval=50, repeat=True)
    
    plt.show()

if __name__ == "__main__":
    main()
