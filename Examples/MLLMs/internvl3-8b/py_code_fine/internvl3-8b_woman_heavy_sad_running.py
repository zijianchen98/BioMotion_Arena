
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as Animation

# Define the positions of the point-light stimulus
def generate_points():
    x = np.array([1, 10, 10, 1, 1])
    y = np.array([1, 1, 8, 8, 3])
    return x, y

def update_point(num, x, y):
    if num % 50 == 0:
        return (np.append(x[1:], x[0])-0.1, np.append(y[1:], y[0]+3)), \
               (np.append(x[1:], x[0]), np.append(y[1:], y[0]))
    else:
        return np.append(x[:num%50], x[num%50]-1), np.append(y[:num%50], y[num%50]-3), \
               np.append(x[num%50:], x[(num//50)*10]), np.append(y[num%50:], y[(num//50)*10])

def animate():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    points, new_points = generate_points()
    
    def animate(num):
        points, new_points = update_point(num, points[0], points[1])
        ax.plot(points[0], points[1], 'o', markersize=15, color='white', lw=2)
        ax.plot(new_points[0], new_points[1], '--', color='white')
    
    ani = Animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)
    plt.show()

if __name__ == "__main__":
    animate()
