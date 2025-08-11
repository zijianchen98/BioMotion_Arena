
import matplotlib.pyplot as plt
import numpy as np
import time

def generate_animation():
    # Create a figure and axis object for the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Function to plot the human in each frame
    def plot_body(frame_number):
        x = [4.5, 5.5, 4.5, 3.5, 2.5, 2.5, 2.5, 4.5, 6.5, 2.5, 6.5, 7.5, 8.5, 9.5, 9.5]
        y = [1, 1, 3, 3, 3, 5, 5, 7, 7, 9, 9, 11, 13, 13, 15]

        weights = [0.5, 0.3, 0.5, 0.5, 1.2, 2.0, 2.5, 3.0, 5.0, 8.0, 10.0, 6.0, 4.0, 2.0, 1.0]

        for i in range(15):
            circle = plt.Circle((x[i], y[i]), radius=0.15 + weights[i] * 0.1, color='white', linewidth=0.5, fill=False)
            ax.add_artist(circle)
        plt.xlim(0, 10)
        plt.ylim(0, 20)

    # Animate the human
    num_frames = 100
    interval = 50
    anim = FuncAnimation(fig, plot_body, frames=num_frames, interval=interval, blit=False)
    plt.show()

from matplotlib.animation import FuncAnimation

generate_animation()
