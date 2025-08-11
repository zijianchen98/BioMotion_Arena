
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 50], [10, 40], [20, 40], [30, 40],
    [5, 30], [15, 30], [25, 30], [35, 30],
    [10, 20], [20, 20],
    [10, 10], [20, 10],
    [15, 0],
    [10, -10], [20, -10]
])


def update(frame_num, points, line):
    # Simulate bowing motion.  This is a simplified example.  More sophisticated
    # biomechanical models would create a more realistic animation.
    amplitude = 10  # Adjust for bowing intensity
    frequency = 0.1  # Adjust for bowing speed
    phase_shift = np.pi/2

    new_positions = np.copy(initial_positions)
    new_positions[:, 1] += amplitude * np.sin(2 * np.pi * frequency * frame_num + phase_shift)


    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-20, 50), ylim=(-20, 60))
ax.set_facecolor('black')  # Set background to black

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(points,),
                              frames=100, interval=50, blit=True)

plt.axis('off')
plt.show()

