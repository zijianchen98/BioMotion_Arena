
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 15.5)
ax.set_ylim(0, 4)
ax.set_aspect('equal')

class SadWomanLyingDown:
    def __init__(self):
        self.point = plt.Circle((10, 2), 0.5, color='white', r=0.5)
        self.ax = ax
        self.frame = 0
        self.pos = np.zeros((15, 2))
        self.pos[0] = [10.0, 1.0]
        self.pos[1:6] = [10.0, 1.0]
        self.pos[7:13] = [10.0, 1.0]
        self.pos[14] = [9.5, 1.0]

        self.pos_shift = np.array([np.cos(0), np.sin(0)])
        self.pos_shift /= np.linalg.norm(self.pos_shift)

    def animate(self, i):
        self.frame += 1
        for j in range(15):
            self.pos[j] += self.pos_shift
            self.points[j].set_center(self.pos[j])

        if i >= 20:
            return False
        return True

    def init(self):
        self.points = [plt.Circle(pt, 0.5, color='white', r=0.5) for pt in self.pos]
        return self.points

# Create the animation
sadwoman = SadWomanLyingDown()
ani = animation.FuncAnimation(fig, sadwoman.animate, init_func=sadwoman.init, frames=30, interval=200, blit=True)

# Show the plot
plt.close()
