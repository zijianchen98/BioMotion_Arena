
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def update_position(frame):
    global angle
    angle += np.random.uniform(5, 10)  # Incremental rotation
    x = 15 * np.cos(np.deg2rad(angle))  # Rotating position
    y = 15 * np.sin(np.deg2rad(angle))  # Rotating position
    fig.clear()
    ax.plot(x, y, 'bo')  # Plot the point as a blue dot
    ax.set_xlim(-20, 20)  # Limit the x and y to -20 to 20
    ax.set_ylim(-20, 20)  # Limit the x and y to -20 to 20
    fig.suptitle(f"Frame: {frame + 1}")

fig, ax = plt.subplots()
ax.set_aspect('equal')
fig.show()
angle = 0
start = time.time()

try:
    frames = 100  # Number of frames for the animation
    for i in range(frames):
        update_position(i)
        plt.pause(0.1)
except KeyboardInterrupt:
    pass
finally:
    print(f"'Animation' took {time.time() - start:.2f} seconds.")
