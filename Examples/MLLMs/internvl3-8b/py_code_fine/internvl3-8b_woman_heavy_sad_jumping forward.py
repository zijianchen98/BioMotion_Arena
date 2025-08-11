
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial position of the woman
x = 5
y = 2

# Define the position of the woman at different frames
frame_points = [
    ((x, y), (x-1, y+1), (x+1, y+1), (x-2, y+1), (x+2, y+1)),
    ((x, y), (x-1, y+2), (x+1, y+2), (x-2, y+2), (x+2, y+2)),
    ((x, y), (x-1, y+3), (x+1, y+3), (x-2, y+3), (x+2, y+3)),
    ((x-1, y-2), (x+1, y-2), (x-2, y+3), (x+2, y+3)),
    ((x, y), (x-1, y-3), (x+1, y-3), (x-2, y+3), (x+2, y+3)),
    ((x, y), (x-1, y-4), (x+1, y-4), (x-2, y+3), (x+2, y+3)),
    ((x, y), (x-1, y-5), (x+1, y-5), (x-1, y-3), (x+1, y-3)),
]

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    for item in frame_points[i]:
        ax.scatter(item[0], item[1], color='white', s=50)

ani = animation.FuncAnimation(fig, animate, frames=len(frame_points), interval=100, repeat=True)
plt.show()
