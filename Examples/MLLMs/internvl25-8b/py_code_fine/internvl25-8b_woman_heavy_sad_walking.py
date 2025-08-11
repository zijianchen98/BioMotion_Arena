
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SadWomanWalking:
    def __init__(self, frame_num, key_points):
        """
        Initialize the animation parameters.

        Parameters:
        - frame_num: int, total number of frames for the animation.
        - key_points: array of shape (15, 2), where each row contains the x, y coordinate of a key point.
        """
        self.frame_num = frame_num
        self.key_points = key_points
        self.fig, self.ax = plt.subplots()
        self.ax.set_axis_off()
        self.stimulus = np.zeros((self.frame_num, 15, 2))

    def init_stimulus(self):
        """
        Initialize the stimulus animation frame.
        """
        self.stimulus[0, :, :] = 1
        return self.stimulus[0]

    def update_stimulus(self, frame):
        """
        Update the stimulus frame for animation.
        """
        self.stimulus[frame, :, :] = 1
        return self.stimulus[frame]

    def save_animation(self, filename):
        """
        Save the animation to a file.

        Parameters:
        - filename: str, the name of the file to save the animation.
        """
        ani = FuncAnimation(self.fig, self.update_stimulus, frames=self.frame_num, init_func=self.init_stimulus, blit=True)
        ani.save(filename, writer='animation')

fig, ax = plt.subplots()
sw = SadWomanWalking(frame_num=100, key_points=np.random.rand(15, 2))
sw.save_animation('sadwoman_walking_animation.gif')
