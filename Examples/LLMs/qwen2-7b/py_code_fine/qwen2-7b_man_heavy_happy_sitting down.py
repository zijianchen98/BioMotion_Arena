
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def animate_point_light():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(projection='3d'

    # Set up the background
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.set_facecolor('black')

    # Animation parameters
    num_lights = 15
    duration = 100
    fps = 30
    light_positions = [np.random.uniform(-50, 50, 3) for _ in range(num_lights)]

    def update(frame):
        for i, light_pos in enumerate(light_positions):
            angle = frame / fps * 2 * np.pi
            x = np.cos(angle) * light_pos[0] + np.sin(angle) * light_pos[1]
            y = -np.sin(angle) * light_pos[0] + np.cos(angle) * light_pos[1]
            z = light_pos[2]
            light_positions[i] = [x, y, z]
            ax.scatter(x, y, z, color='white')

    ani = FuncAnimation(fig, update, frames=np.arange(0, duration * fps, blit=False)

    plt.show()

if __name__ == '__main__':
    animate_point_light()
