
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    ax.clear()  # This clears previous frames
    x = 5 * np.cos(i/50.0)  # x-coordinate of the dot
    y = 5 * np.sin(i/50.0)  # y-coordinate of the dot
    ax.scatter(x, y, color='white')  # Add a white point at coordinates (x,y)

fig = plt.figure()
ax = plt.axes(xlim=(-6,6), ylim=(-6,6))
anime = animation.FuncAnimation(fig, animate, frames=300, interval=50, repeat=True)
plt.show()
