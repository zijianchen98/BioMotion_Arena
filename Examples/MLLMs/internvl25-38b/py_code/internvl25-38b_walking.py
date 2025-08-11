
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class WalkerAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.lights = plt.scatter([], [])
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_aspect('equal')
        self.ax.set_facecolor('black')
        self.ax.axis('off')
        self.trajectories = self.generate_trajectories()

    def generate_trajectories(self):
        # Define coordinates for 15 points
        points = np.zeros((15, 2))
        
        # Initial position of the points
        points[0] = (5.0, 5.0)     # Head
        points[1] = (4.5, 4.0)     # Left shoulder
        points[2] = (5.5, 4.0)     # Right shoulder
        points[3] = (4.0, 3.0)     # Left elbow
        points[4] = (6.0, 3.0)     # Right elbow
        points[5] = (3.5, 2.0)     # Left hand
        points[6] = (6.5, 2.0)     # Right hand
        points[7] = (5.0, 2.0)     # Left hip
        points[8] = (5.0, 2.0)     # Right hip
        points[9] = (4.5, 1.0)     # Left knee
        points[10] = (5.5, 1.0)    # Right knee
        points[11] = (4.0, 0.0)     # Left foot
        points[12] = (6.0, 0.0)     # Right foot
        points[13] = (4.8, 3.0)     # Left torso point
        points[14] = (5.2, 3.0)     # Right torso point

        trajectories = []
        for i in range(100):
            frame = points.copy()
            # Simulate walking motion
            alpha = 0.1 * np.sin(i * 0.1)
            beta = 0.1 * np.cos(i * 0.1)
            frame[7][0] += 0.02
            frame[8][0] += 0.02
            frame[9][0] += 0.03 + alpha
            frame[10][0] += 0.03 - alpha
            frame[11][0] += 0.05 + beta
            frame[12][0] += 0.05 - beta
            frame[9][1] += -0.03
            frame[10][1] += -0.03
            frame[11][1] += -0.05
            frame[12][1] += -0.05
            trajectories.append(frame)

        return trajectories

    def animate(self, i):
        self.lights.set_offsets(self.trajectories[i])
        return self.lights,

    def show(self):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=len(self.trajectories), interval=50, blit=True)
        plt.show()

if __name__ == "__main__":
    animation = WalkerAnimation()
    animation.show()
