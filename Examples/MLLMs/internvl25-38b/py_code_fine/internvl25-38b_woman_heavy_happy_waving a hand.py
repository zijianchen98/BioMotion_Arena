
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame, points):
    angle = np.pi / 4 * np.sin(frame / 20)
    translation_x = frame % 50
    translation_y = 10 * np.sin(frame / 20)

    for i, point in enumerate(points):
        if i == 1:  # Assuming index 1 represents the waving hand
            # Update the position of the waving hand
            point[0] = 0.3 * np.cos(angle) + translation_x
            point[1] = 0.3 * np.sin(angle) + translation_y
        else:
            # Other points can gently move to simulate body shifting
            point[0] = 0.1 * np.sin(frame / 10) + translation_x
            point[1] = 0.1 * np.cos(frame / 10) + translation_y

    scatter.set_offsets(points)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-50, 50)
ax.set_ylim(-10, 30)
ax.axis('off')

# Create 15 white point-lights
points = np.random.rand(15, 2) * 10 - 5  # Initialize points randomly around center
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, func=update, frames=200, fargs=(points,), interval=50)

plt.show()
