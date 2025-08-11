
import matplotlib.pyplot as plt
import numpy as np
import time

def sad_woman_hand_wave(size, duration):
    fig, ax = plt.subplots()

    # Create a black background
    ax.set_facecolor('black')

    # Create 15 point-lights
    lights = [plt.Circle((x, y), 0.5, color='white') for x in np.random.rand(15) for y in np.random.rand(15)]

    for light in lights:
        ax.add_patch(light)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    for t in np.arange(0, duration, 0.1):
        for light in lights:
            light.center = np.random.rand(2)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Adding the sadwoman face around the lights
        sad_woman = plt.Circle((0.5, 0.5), size, color='white')
        ax.add_patch(sad_woman)

        # Waving a hand motion
        for light in lights:
            light.center = (0.5, 0.5) + (light.center[0] - 0.5) * np.sin(t * 2 * np.pi) * 0.15

        time.sleep(0.01)

# Run the animation
sad_woman_hand_wave(0.2, 5.0)
plt.show()
