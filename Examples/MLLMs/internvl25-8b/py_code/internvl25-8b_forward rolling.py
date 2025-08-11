
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Define the initial position of the points
points = [(i, 1.0) for i in range(15)]

# Create a point light stimulus
def create_points(num_points):
    points = []
    for _ in range(num_points):
        points.append(ax.text(0.5, 0.5, 'o', ha='center', va='center', fontsize=15, color='white'))
    return points

# Animation function
def update(frame):
    x_values = [point[0] + frame * 0.75 * np.sin(np.pi / 5) for point in points]
    y_values = [point[1] + frame * 0.5 * np.sin(np.pi / 3) for point in points]
    for point, (x, y) in zip(points, zip(x_values, y_values)):
        point.set_position((x, y))
    return points

def main():
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_axis_off()
    points = create_points(15)
    
    ani = animation.FuncAnimation(fig, update, frames=np.arange(150), repeat=True)
    plt.show()

if __name__ == "__main__":
    main()
