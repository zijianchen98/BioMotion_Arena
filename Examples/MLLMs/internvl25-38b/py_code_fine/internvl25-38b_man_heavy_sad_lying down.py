
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SadManAnimation:
    def __init__(self, num_frames=100):
        self.num_frames = num_frames
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')

        self.points, = self.ax.plot([], [], 'wo')

    def generate_positions(self, frame):
        positions = np.array([
            (0.5, 0.5),  # Head
            (0.45, 0.5), (0.55, 0.5),  # Shoulders
            (0.4, 0.65), (0.6, 0.65),  # Hands
            (0.5, 0.75),  # Elbows
            (0.45, 0.85), (0.55, 0.85),  # Hips
            (0.4, 0.95), (0.6, 0.95),  # Knees
            (0.35, 1.0), (0.65, 1.0),  # Feet
            (0.5, 0.6),  # Neck
            (0.3, 0.7),  # Left arm
            (0.7, 0.7),  # Right arm
            (0.4, 0.9),  # Left leg
            (0.6, 0.9)   # Right leg
        ])
        
        # Introduce minor variation for realism
        positions += np.random.normal(0, 0.005, positions.shape)
        
        return positions

    def init(self):
        self.points.set_data([], [])
        return self.points,

    def animate(self, frame):
        x, y = self.generate_positions(frame).T
        self.points.set_data(x, y)
        return self.points,

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=self.num_frames, init_func=self.init, blit=True, repeat=True)
        plt.show()

if __name__ == "__main__":
    animation = SadManAnimation()
    animation.run()
