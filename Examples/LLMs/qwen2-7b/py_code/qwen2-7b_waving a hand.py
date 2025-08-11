
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False,
xlim=(-50, 100), ylim=(-10, 10),
xmargin=0.0, ymargin=0.0)
ax.set_aspect('equal')

# Create the white points
points = np.zeros((15, 2))
for i in range(15:
    points[i] = [np.random.randint(-40, 60), np.random.randint(-50, 50)]

def animate(i):
    global points
    
    # Update the positions of the points based on a simple physics model
    # For realistic movement
    for j in range(15:
        points[j][0] += np.random.normal((-1, 1)  # horizontal movement
        points[j][1] += np.random.normal((-0.5, 0.2))  # vertical movement
        
        # Limit the movement within the plot boundaries
        if points[j][0] > 100:
            points[j][0] = 99
        elif points[j][0] < -100:
            points[j][0] = -99
            
        if points[j][1] > 10:
            points[j][1] = 9
        elif points[j][1] < -10:
            points[j][1] = -9
            
    ax.clear()
    ax.set_xlim((-100, 100))
    ax.set_ylim((-10, 10))
    
    ax.set_aspect('equal')
    ax.plot(points[:, 0], points[:, 1], 'o', color='white')
    ax.add_patch(plt.Circle((0, 0), radius=5, facecolor='black', edgecolor='none')
    
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()

