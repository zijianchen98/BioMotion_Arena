
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

points = []
points_init_pos = [(30 + i*2, 50) for i in range(15)]
points_color = 'white'
points_size = 4

for pos in points_init_pos:
    circle = plt.Circle(pos, radius=points_size, color=points_color)
    points.append(circle)
    ax.add_patch(circle)

def update(frame):
    for i, point in enumerate(points):
        x, y = point.center
        x = (x + 2) % 30 + 30 * (frame // 3 % 2)
        y += 0.5 if frame % 60 < 30 else -0.5
        points[i].center = (x, y)

ani = animation.FuncAnimation(fig, update, frames=range(300), interval=50, blit=False)

plt.axis('off')
plt.show()
