
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights
x = [0.5, 2.5, 4.5, 0.5, 2.5, 4.5, 1.5, 2.5, 3.5, 1.5, 2.5, 3.5]
y = [0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 2.5, 2.5, 2.5, 3.5, 3.5, 3.5, 4.5, 4.5, 4.5]

# Plot initial positions
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-0.5, 5.5)
ax.set_xticks([])
ax.set_yticks([])
dots = ax.scatter(x, y, s=100, color='w')

# Animated function to move the dots
def update(frame):
    # Simple up-down jump animation
    x = [0.5, 2.5, 4.5, 0.5, 2.5, 4.5, 1.5, 2.5, 3.5, 1.5, 2.5, 3.5]
    y = [0.5 + frame // 80 * 0.5, 0.5 + frame // 40 * 0.5, 0.5 + frame // 20 * 0.5,
         1.5 + frame // 40 * 0.5, 1.5 + frame // 40 * 0.5, 1.5 + frame // 40 * 0.5,
         2.5 + frame // 40 * 0.5, 2.5 + frame // 40 * 0.5, 2.5 + frame // 40 * 0.5,
         3.5 + frame // 40 * 0.5, 3.5 + frame // 20 * 0.5, 3.5 + frame // 20 * 0.5, 4.5]
    dots.set_offsets(list(zip(x, y)))
    return dots,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(0, 240), blit=True, interval=30, repeat=True)
plt.show()
