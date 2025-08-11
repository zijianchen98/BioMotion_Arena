
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
points = 15

# Initial positions of the points
positions = [(random.randint(10, 80), random.randint(0, 100)) for _ in range(points)]

fig, ax = plt.subplots()
scatter = plt.scatter(*zip(*positions), color='white', s=100)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xticks([])
ax.set_yticks([])

def update(frame):
    global positions
    new_positions = []
    for x, y in positions:
        # Define the motion of the points here
        new_x = x + random.choice([-1, 0, 1])
        new_y = y + random.choice([-1, 0, 1])
        new_positions.append((new_x, new_y))
    positions = new_positions
    scatter.set_offsets(new_positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
