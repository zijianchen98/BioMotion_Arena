
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

class SadmanLyingDown:
    def __init__(self):
        self.positions = self.create_positions()

    def create_positions(self):
        positions = [
            (120, 120), (160, 160), (200, 200), (240, 240), (280, 280),
            (320, 320), (360, 360), (400, 400), (440, 440),
            (480, 480), (520, 520), (560, 560),
            (640, 480), (680, 400), (720, 320), (760, 240)
        ]
        return positions

    def update_positions(self, frame):
        positions = self.positions
        next_positions = []
        for position in positions:
            dx = position[0] - 2
            dy = position[1] - 2
            next_positions.append((dx, dy))
        return [(position, position) for position in next_positions]

    def draw_animation(self, frame):
        plt.cla()
        plt.axis('equal')
        plt.axis('off')
        for dy, dx in self.update_positions(frame):
            plt.plot(df, dy / 6.2, 'o')

        if frame == 50:
            plt.title("Animation Completion", fontsize=25, color="yellow")

    def main(self):
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.toolbar.set_visible(False)
        self.anim = animation.FuncAnimation(
            self.fig, 
            self.draw_animation,
            frames=50,
            interval=50,
            blit=True,
            init_func = lambda: self.draw_animation(0))
        
        plt.show()
        
if __name__ == "__main__":
    SadmanLyingDown().main()
