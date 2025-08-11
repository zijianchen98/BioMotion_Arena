
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    # Define positions for standing, sitting, and lying down
    standing_positions = [
        (0, 1.45),  # head
        (-0.1, 1.35),  # left shoulder
        (0.1, 1.35),  # right shoulder
        (-0.1, 1.05),  # left elbow
        (0.1, 1.05),  # right elbow
        (-0.1, 0.75),  # left wrist
        (0.1, 0.75),  # right wrist
        (-0.1, 0.85),  # left hip
        (0.1, 0.85),  # right hip
        (-0.1, 0.45),  # left knee
        (0.1, 0.45),  # right knee
        (-0.1, 0.05),  # left ankle
        (0.1, 0.05),  # right ankle
        (-0.1, 0.0),  # left toe
        (0.1, 0.0)   # right toe
    ]

    sitting_positions = [
        (0, 1.1),  # head
        (-0.1, 0.9),  # left shoulder
        (0.1, 0.9),  # right shoulder
        (-0.1, 0.6),  # left elbow
        (0.1, 0.6),  # right elbow
        (-0.1, 0.3),  # left wrist
        (0.1, 0.3),  # right wrist
        (-0.1, 0.4),  # left hip
        (0.1, 0.4),  # right hip
        (-0.5, 0.4),  # left knee
        (0.5, 0.4),  # right knee
        (-0.5, 0.0),  # left ankle
        (0.5, 0.0),  # right ankle
        (-0.6, 0.0),  # left toe
        (0.6, 0.0)   # right toe
    ]

    lying_positions = [
        (-0.9, 0),  # head
        (-0.7, 0.05),  # left shoulder
        (-0.7, -0.05),  # right shoulder
        (-1.0, 0.05),  # left elbow
        (-1.0, -0.05),  # right elbow
        (-1.3, 0.05),  # left wrist
        (-1.3, -0.05),  # right wrist
        (-0.2, 0.05),  # left hip
        (-0.2, -0.05),  # right hip
        (0.2, 0.05),  # left knee
        (0.2, -0.05),  # right knee
        (0.6, 0.05),  # left ankle
        (0.6, -0.05),  # right ankle
        (0.7, 0.05),  # left toe
        (0.7, -0.05)   # right toe
    ]

    # Set up the figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.1, 1.6)

    # Create points
    points = [ax.plot([], [], 'o', color='white', markersize=10)[0] for _ in range(15)]

    # Update function for animation
    def update(t):
        if t <= 0.5:
            alpha = t / 0.5
            pos = [(1 - alpha) * standing_positions[i][0] + alpha * sitting_positions[i][0],
                   (1 - alpha) * standing_positions[i][1] + alpha * sitting_positions[i][1]] for i in range(15)
        else:
            alpha = (t - 0.5) / 0.5
            pos = [(1 - alpha) * sitting_positions[i][0] + alpha * lying_positions[i][0],
                   (1 - alpha) * sitting_positions[i][1] + alpha * lying_positions[i][1]] for i in range(15)
        for i, point in enumerate(points):
            point.set_data([pos[i][0]], [pos[i][1]])
        return points

    # Create animation
    anim = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True)

    # Show the plot
    plt.show()
