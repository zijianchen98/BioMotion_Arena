
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the lights for a running sadwoman
def get_light_positions(t):
    # Simplified model of a running sadwoman
    # 15 points representing different parts of the body
    # This is a placeholder function. Realistic motion would require more complex calculations.
    x = [np.sin(t), np.cos(t), np.sin(t + np.pi / 2), np.cos(t + np.pi / 2),
         np.sin(t + np.pi), np.cos(t + np.pi), np.sin(t + 3 * np.pi / 2), np.cos(t + 3 * np.pi / 2),
         np.sin(t + np.pi / 4), np.cos(t + np.pi / 4), np.sin(t + 5 * np.pi / 4), np.cos(t + 5 * np.pi / 4),
         np.sin(t + 3 * np.pi / 4), np.cos(t + 3 * np.pi / 4), np.sin(t + 7 * np.pi / 4)]
    y = [np.cos(t), np.sin(t), np.cos(t + np.pi / 2), np.sin(t + np.pi / 2),
         np.cos(t + np.pi), np.sin(t + np.pi), np.cos(t + 3 * np.pi / 2), np.sin(t + 3 * np.pi / 2),
         np.cos(t + np.pi / 4), np.sin(t + np.pi / 4), np.cos(t + 5 * np.pi / 4), np.sin(t + 5 * np.pi / 4),
         np.cos(t + 3 * np.pi / 4), np.sin(t + 3 * np.pi / 4), np.cos(t + 7 * np.pi / 4)]
    return np.array(x), np.array(y)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for better visual clarity

dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(i):
    t = i / 10.0  # Time in seconds
    x, y = get_light_positions(t)
    dots.set_data(x, y)
    return dots,

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=100, interval=50, blit=True)

plt.show()
