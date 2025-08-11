
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_frame(i):
    # Define motion parameters to create a waving hand-like animation
    motion = [
        ([10, 10], 2, 0.5),   # Upper arm
        ([5, 6], 2, 0.5),    # Shoulder
        ([5, 9], 2, 0.5),    # Elbow
        ([5, 11], 2, 0.5),   # Wrist
        ([5, 13], 2, 0.5),   # Hand
        ([5, 15], 2, 0.5),   # Palm
        #[8, 22], 2, 0.5),   # Fingers
    ]

    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_facecolor("k")

    # Initial light positions
    lights = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]

    # Update function
    for (pos, time_to_move, duration) in motion:
        for j, light_position in enumerate(lights):
            radius = (i - j) / duration
            amplitude = np.exp(-np.square(i - j))
            x = pos[0] + time_to_move * np.sin(np.sqrt(2 * amplitude * radius * i))
            y = pos[1] + time_to_move * np.cos(np.sqrt(2 * amplitude * radius * i))
            lights[j] = [x, y]

    # Drawing the lights
    lights = np.array(lights)
    lines = ax.scatter(lights[:, 0], lights[:, 1], s=800, color="w", marker="o")

    return lights

# Animation
ani = animation.FuncAnimation(plt.gcf(), animate_frame, frames=200, interval=100, blit=True)
plt.show()
