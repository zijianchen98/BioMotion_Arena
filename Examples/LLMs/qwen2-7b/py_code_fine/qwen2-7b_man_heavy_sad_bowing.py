
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to simulate the motion of a single point light
def simulate_point_light_motion(t):
    # Parameters for the motion ( can be adjusted for different motions
    amplitude = 0.5
    frequency = 0.1
    phase_shift = 0.5 * t

    x = amplitude * np.sin(((frequency * t) + phase_shift)
    y = -amplitude * np.cos((frequency * t) + phase_shift)

    return x, y

# Function to update the animation frame
def update(frame):
    global xs, ys
    xs = [simulate_point_light_motion(frame / 10)[0] for _ in range(15]
    ys = [simulate_point_light_motion(frame / 10)[1] for _ in range(15]

    # Plotting the points
    for i in range(15:
        plt.scatter(xs[i], ys[i], color='white')

    # Clearing the axes for the next frame
    plt.cla()

# Main function to create and run the animation
def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')

    global xs, ys
    xs, ys = [], []

    ani = FuncAnimation(fig, update, frames=np.arange(0, 1000, blit=False, interval=20)
    plt.show()

if __name__ == '__main__':
    main()
