
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_point_light(subject, action, n_frames=100):
    fig = plt.figure(figsize=(4, 4))
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_facecolor('black')

    def init():
        points = np.zeros((n_frames, 2))
        for i in range(n_frames):
            points[i] = np.random.uniform(-5, 10, 2)
        return [plt.plot(points[i][0], points[i][1], 'w', markersize=10)[0] for i in range(n_frames)]

    def update(i):
        if action == 'jumping forward':
            points[i][0] += 0.1  # Move forward
            points[i][1] -= 0.1  # Jump up
        elif action == 'walking forward':
            points[i][0] += 0.05  # Move forward at a slower pace
        else:
            raise ValueError("Invalid action")
        return [plt.plot(points[i][0], points[i][1], 'w', markersize=10)[0]]

    ani = animation.FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True)

    plt.show()

animate_point_light('sadwoman', 'jumping forward')
